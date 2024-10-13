const redis = require('redis');

const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
  console.log('Connected to Redis');
});

client.on('error', (err) => {
  console.log('Error connecting to Redis:', err);
});

// Connect to Redis server
client.connect();

module.exports = client;