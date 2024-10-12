const express = require('express');
const app = express();
const port = 3000;

// Middleware for parsing JSON
app.use(express.json());

// Routes
app.get('/', (req, res) => {
  res.json({ message: 'Welcome to the Files Manager API.' });
});

const filesRoute = require('./routes/files');
app.use('/files', filesRoute);

const authRoute = require('./routes/auth');
app.use('/auth', authRoute);

// Start the express server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
