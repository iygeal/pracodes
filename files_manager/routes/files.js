// routes/files.js
const express = require('express');
const authMiddleware = require('../middleware/auth');
const router = express.Router();
const filesController = require('../controllers/filesController');

// Protect the route with the authMiddleware
router.get('/', authMiddleware, filesController.listAllFiles);

// Create new file (for now, we'll just simulate file upload)
router.post('/files', async (req, res) => {
  const { name, path, userId } = req.body;

  try {
    const file = new File({ name, path, userId });
    await file.save();
    res.status(201).json({ message: 'File uploaded successfully', file });
  } catch (error) {
    res.status(500).json({ error: 'File upload failed' });
  }
});

router.get('/files', async (req, res) => {
  try {
    const files = await File.find();
    res.status(200).json(files);
  } catch (error) {
    res.status(500).json({ error: 'Could not retrieve files' });
  }
});

router.put('/files/:id/permission', async (req, res) => {
  const { id } = req.params;
  const { permission } = req.body;

  try {
    const file = await File.findByIdAndUpdate(
      id,
      { permission },
      { new: true }
    );
    if (!file) {
      return res.status(404).json({ error: 'File not found' });
    }
    res.status(200).json({ message: 'Permission updated', file });
  } catch (error) {
    res.status(500).json({ error: 'Permission update failed' });
  }
});

// New code for kue queue

const queue = require('../utils/kue');

// Simulate image upload route and create background job for thumbnail generation
router.post('/upload', async (req, res) => {
  const { name, path, userId } = req.body;

  try {
    const file = new File({ name, path, userId });
    await file.save();

    // Create a job for generating a thumbnail
    const job = queue
      .create('thumbnail', {
        fileId: file._id,
        name: file.name,
      })
      .save((err) => {
        if (err) return res.status(500).json({ error: 'Job creation failed' });
        console.log(`Job created: ${job.id}`);
        res
          .status(201)
          .json({
            message: 'File uploaded successfully, thumbnail generation started',
            jobId: job.id,
          });
      });
  } catch (error) {
    res.status(500).json({ error: 'File upload failed' });
  }
});

module.exports = router;
