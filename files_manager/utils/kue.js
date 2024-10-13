// utils/kue.js
const kue = require('kue');

// Create a Kue job queue
const queue = kue.createQueue();

queue.on('error', (err) => {
  console.error('Kue error:', err);
});

module.exports = queue;
