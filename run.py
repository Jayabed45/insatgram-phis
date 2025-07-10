#!/usr/bin/env python3
"""
Instagram Login Server - Startup Script
This script installs dependencies and starts the Flask server
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Error installing dependencies")
        return False
    return True

def start_server():
    """Start the Flask server"""
    print("Starting Instagram Login Server...")
    print("Server will be available at: http://localhost:5000")
    print("API endpoint: http://localhost:5000/api/login")
    print("Logs endpoint: http://localhost:5000/api/logs")
    print("\nPress Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == "__main__":
    print("Instagram Login Server Setup")
    print("=" * 30)
    
    if install_requirements():
        start_server()
    else:
        print("Failed to install dependencies. Please check your Python environment.") 