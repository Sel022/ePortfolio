
const express = require('express');
const Trip = require('../models/trip');
const { requireAuth } = require('../middleware/auth');
const router = express.Router();

// GET trips with pagination
router.get('/', requireAuth, async (req, res, next) => {
  try {
    const page = Math.max(1, parseInt(req.query.page) || 1);
    const limit = Math.min(50, parseInt(req.query.limit) || 10);

    const [items, total] = await Promise.all([
      Trip.find({}).sort({ startDate: 1 }).skip((page - 1) * limit).limit(limit),
      Trip.countDocuments()
    ]);

    res.json({ items, page, pages: Math.ceil(total / limit), total });
  } catch (err) {
    next(err);
  }
});

// POST new trip (only authenticated users)
router.post('/', requireAuth, async (req, res, next) => {
  try {
    const trip = new Trip({ ...req.body, createdBy: req.user.id });
    await trip.save();
    res.status(201).json(trip);
  } catch (err) {
    next(err);
  }
});

module.exports = router;

