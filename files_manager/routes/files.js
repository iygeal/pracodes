const express = require('express');
const router = express.Router();
const filesController = require('../controllers/filesController');

// Define route for getting all files
router.get('/', filesController.listAllFiles);

module.exports = router;
