// server.js
import express from 'express';

const app = express();
app.use(express.json());

let users = [{ id: 1, name: 'John Doe' }];

// Get all users
app.get('/users', (req, res) => {
  res.status(200).json(users);
});

// Add a new user
app.post('/users', (req, res) => {
  const newUser = { id: users.length + 1, name: req.body.name };
  users.push(newUser);
  res.status(201).json(newUser);
});

// Get user by ID
app.get('/users/:id', (req, res) => {
  const user = users.find((u) => u.id === parseInt(req.params.id));
  if (user) {
    res.status(200).json(user);
  } else {
    res.status(404).json({ error: 'User not found' });
  }
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

export default app;
