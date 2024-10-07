const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Connect to Redis server
async function connectRedis() {
  try {
    await client.connect();
    console.log('Connected to Redis..');

    // Set Hash value in Redis
    await client.hSet('user:1000', {
      name: 'John Doe',
      age: '30',
      email: 'john@example.com',
    });
    console.log('Hash SET: user:1000');

    // Get all fields from the hash
    const user = await client.hGetAll('user:1000');
    console.log('Hash GET:', user);

    // Close the Redis connection
    await client.quit();
  } catch (err) {
    console.error('Redis error:', err);
  }
}

connectRedis();
