const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');

// Simple login route
router.post('/login', (req, res) => {
  const { username } = req.body;
  if (username) {
    // Create a token (in real apps, validate the username/password from db)
    const token = jwt.sign({ username }, 'your_secrete_key', {
      expiresIn: '1h',
    });
  }
  return res.status(400).json({ message: 'Username is required' });
});

module.exports = router;
