const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Connect to Redis server
async function connectRedis() {
  try {
    await client.connect();
    console.log('Connected to Redis..');

    // Set and Get data from Redis
    await client.set('mykey', 'Hello from NodeJS');
    console.log('SET: OK');

    const value = await client.get('mykey');
    console.log('GET:', value);

    // Close the Redis connection
    await client.quit();
  } catch (err) {
    console.error('Redis error:', err);
  }
}

connectRedis();
