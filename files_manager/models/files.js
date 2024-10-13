const mongoose = require('mongoose');

const fileSchema = new mongoose.Schema({
  name: { type: String, required: true },
  path: { type: String, required: true },
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  permission: { type: String, enum: ['public', 'private'], default: 'private' },
  createdAt: { type: Date, default: Date.now },
});

module.exports = mongoose.model('File', fileSchema);