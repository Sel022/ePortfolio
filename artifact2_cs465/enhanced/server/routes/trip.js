const express = require('express');
const { body, param, query } = require('express-validator');
const Trip = require('../models/Trip');
const { requireAuth } = require('../middleware/auth');
const { validateOrFail } = require('../middleware/validate');

const router = express.Router();

// GET /api/trips?page=&limit=
router.get(
  '/',
  requireAuth,
  query('page').optional().isInt({ min: 1 }).toInt(),
  query('limit').optional().isInt({ min: 1, max: 50 }).toInt(),
  validateOrFail,
  async (req, res, next) => {
    try {
      const page = req.query.page || 1;
      const limit = req.query.limit || 10;
      const skip = (page - 1) * limit;

      const [items, total] = await Promise.all([
        Trip.find({}).sort({ startDate: 1 }).skip(skip).limit(limit),
        Trip.countDocuments()
      ]);
      res.json({ items, page, pages: Math.ceil(total / limit), total });
    } catch (err) { next(err); }
  }
);

// POST /api/trips
router.post(
  '/',
  requireAuth,
  body('title').isString().notEmpty(),
  body('slug').isString().notEmpty(),
  body('destination').isString().notEmpty(),
  body('startDate').isISO8601(),
  body('endDate').isISO8601(),
  body('price').isFloat({ min: 0 }),
  body('description').isString().isLength({ min: 1, max: 2000 }),
  validateOrFail,
  async (req, res, next) => {
    try {
      const trip = new Trip({ ...req.body, createdBy: req.user.id });
      await trip.save();
      res.status(201).json(trip);
    } catch (err) { next(err); }
  }
);

// PUT /api/trips/:id
router.put(
  '/:id',
  requireAuth,
  param('id').isMongoId(),
  body('price').optional().isFloat({ min: 0 }),
  validateOrFail,
  async (req, res, next) => {
    try {
      const trip = await Trip.findById(req.params.id);
      if (!trip) return res.status(404).json({ message: 'Trip not found' });
      if (String(trip.createdBy) !== req.user.id) return res.status(403).json({ message: 'Forbidden' });

      Object.assign(trip, req.body);
      await trip.save();
      res.json(trip);
    } catch (err) { next(err); }
  }
);

// DELETE /api/trips/:id
router.delete(
  '/:id',
  requireAuth,
  param('id').isMongoId(),
  validateOrFail,
  async (req, res, next) => {
    try {
      const trip = await Trip.findById(req.params.id);
      if (!trip) return res.status(404).json({ message: 'Trip not found' });
      if (String(trip.createdBy) !== req.user.id) return res.status(403).json({ message: 'Forbidden' });

      await trip.deleteOne();
      res.json({ ok: true });
    } catch (err) { next(err); }
  }
);

module.exports = router;

