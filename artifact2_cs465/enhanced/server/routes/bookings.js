const express = require('express');
const { body, param } = require('express-validator');
const Booking = require('../models/Booking');
const Trip = require('../models/Trip');
const { requireAuth } = require('../middleware/auth');
const { validateOrFail } = require('../middleware/validate');

const router = express.Router();

// POST /api/bookings
router.post(
  '/',
  requireAuth,
  body('tripId').isMongoId(),
  body('guests').optional().isInt({ min: 1 }).toInt(),
  validateOrFail,
  async (req, res, next) => {
    try {
      const trip = await Trip.findById(req.body.tripId);
      if (!trip) return res.status(404).json({ message: 'Trip not found' });

      const booking = await Booking.create({
        userId: req.user.id,
        tripId: trip._id,
        guests: req.body.guests || 1
      });
      res.status(201).json(booking);
    } catch (err) { next(err); }
  }
);

// GET /api/bookings/me
router.get('/me', requireAuth, async (req, res, next) => {
  try {
    const mine = await Booking.find({ userId: req.user.id }).populate('tripId');
    res.json(mine);
  } catch (err) { next(err); }
});

// DELETE /api/bookings/:id
router.delete(
  '/:id',
  requireAuth,
  param('id').isMongoId(),
  validateOrFail,
  async (req, res, next) => {
    try {
      const booking = await Booking.findById(req.params.id);
      if (!booking) return res.status(404).json({ message: 'Booking not found' });
      if (String(booking.userId) !== req.user.id) return res.status(403).json({ message: 'Forbidden' });

      await booking.deleteOne();
      res.json({ ok: true });
    } catch (err) { next(err); }
  }
);

module.exports = router;

