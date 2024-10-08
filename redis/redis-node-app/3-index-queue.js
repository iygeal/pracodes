const kue = require('kue');
const queue = kue.createQueue();

// Create a job
const job = queue
  .create('email', {
    title: 'Welcome email for new user',
    to: 'user@email.com',
    template: 'welcome-email',
  })
  .save((err) => {
    if (err) {
      console.error('Error saving job:', err);
    } else {
      console.log('Job saved:', job.id);
    }
  });

// Process jobs from the queue

queue.process('email', (job, done) => {
  console.log('Processing job:', job.data);

  // Simulate email sending delay
  setTimeout(() => {
    console.log(`Email sent to: ${job.data.to}`);
    done(); // Mark the job as done
  }, 2000);
});


kue.app.listen(3000);
console.log('Kue UI running on port 3000');