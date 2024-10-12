const express = require('express');
const redis = require('redis');
const kue = require('kue');

const app = express();
const port = 3000;

// Create a Redis client and a Kue client
const client = redis.createClient();
const queue = kue.createQueue();

// Connect to Redis server
async function connectRedis() {
  try {
    await client.connect();
    console.log('Connected to Redis...');
  } catch (err) {
    console.error('Redis error:', err);
  }
}

connectRedis();

// Middleware to parse JSON
app.use(express.json());

// Route to create a job (e.g., send an email)
app.post('/email', (req, res) => {
  const { to, subject, body } = req.body;

  // Create a job to send an email
  const job = queue
    .create('email', {
      to: to,
      subject: subject,
      body: body,
    })
    .save((err) => {
      if (err) {
        res.status(500).send('Failed to create job');
      } else {
        res.send(`Job ${job.id} created to send email to ${to}`);
      }
    });
});

// Process email jobs
queue.process('email', (job, done) => {
  console.log(`Processing job ${job.id} to send email to: ${job.data.to}`);

  // Simulate email sending delay
  setTimeout(() => {
    console.log(`Email sent to: ${job.data.to}`);
    done(); // Mark task as done
  }, 3000);
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

// Kue UI
kue.app.listen(3001);
console.log('Kue UI running on port 3001');
