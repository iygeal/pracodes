const jwt = require('jsonwebtoken');
const jwtSecret = 'your_jwt_secret';

const authMiddleware = (req, res, next) => {
  const token = req.header('Authorization')?.replace('Bearer ', '');

  if (!token) {
    return res.status(401).json({ error: 'Access denied. No token provided.' });
  }

  try {
    const decoded = jwt.verify(token, jwtSecret);
    req.user = decoded; // Attach user information to the request
    next(); // Pass to the next middleware or route handler
  } catch (error) {
    res.status(400).json({ error: 'Invalid token' });
  }
};

module.exports = authMiddleware;
