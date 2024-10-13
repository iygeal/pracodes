// worker.js
const queue = require('./utils/kue');

// Process 'thumbnail' jobs
queue.process('thumbnail', (job, done) => {
  const { fileId, name } = job.data;

  console.log(`Generating thumbnail for file: ${name} (ID: ${fileId})`);

  // Simulate a delay for thumbnail generation
  setTimeout(() => {
    console.log(`Thumbnail generated for file: ${name}`);
    done(); // Notify Kue that the job is done
  }, 3000); // Simulate 3 seconds of processing time
});
