const mongoose = require('mongoose');

const tripSchema = new mongoose.Schema({
  title: { type: String, required: true, trim: true },
  slug:  { type: String, required: true, unique: true, index: true },
  destination: { type: String, required: true, index: true },
  startDate: { type: Date, required: true, index: true },
  endDate:   { type: Date, required: true },
  price: { type: Number, required: true, min: 0 },
  description: { type: String, required: true, maxlength: 2000 },
  createdBy: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true }
}, { timestamps: true });

tripSchema.pre('save', function(next) {
  if (this.endDate < this.startDate) {
    return next(new Error('End date cannot be earlier than start date'));
  }
  next();
});

module.exports = mongoose.model('Trip', tripSchema);

