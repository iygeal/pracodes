const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

async function connectRedis() {
  try {
    await client.connect();
    console.log('Connected to Redis...');

    // Set some keys
    await client.set('key1', 'value1');
    await client.set('key2', 'value2');
    await client.set('key3', 'value3');

    // Retrieve the keys
    const value1 = await client.get('key1');
    const value2 = await client.get('key2');
    const value3 = await client.get('key3');

    console.log('key1:', value1);
    console.log('key2:', value2);
    console.log('key3:', value3);

    // Delete a key
    await client.del('key1');
    console.log('Deleted key1');

    // Try to Get the deleted key
    const value1AfterDelete = await client.get('key1');
    console.log('key1 after delete:', value1AfterDelete);

    // Close the Redis connection
    await client.quit();
  } catch (err) {
    console.error('Redis error:', err);
  }
}

connectRedis();
