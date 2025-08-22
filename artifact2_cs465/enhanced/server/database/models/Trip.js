// server/models/trip.js
const mongoose = require('mongoose');

const tripSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String, required: true },
  startDate: { type: Date, required: true },
  endDate: { type: Date, required: true },
  price: { type: Number, required: true, min: 0 },
  slug: { type: String, required: true, unique: true, index: true }
}, { timestamps: true });

module.exports = mongoose.model('Trip', tripSchema);
