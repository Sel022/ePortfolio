const express = require('express');
const { body } = require('express-validator');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const { validateOrFail } = require('../middleware/validate');

const router = express.Router();

router.post(
  '/register',
  body('email').isEmail().withMessage('Valid email required'),
  body('password').isLength({ min: 6 }).withMessage('Password min 6 chars'),
  validateOrFail,
  async (req, res, next) => {
    try {
      const exists = await User.findOne({ email: req.body.email });
      if (exists) return res.status(400).json({ message: 'Email already registered' });

      const user = new User(req.body);
      await user.save();
      res.status(201).json({ id: user._id, email: user.email });
    } catch (err) { next(err); }
  }
);

router.post(
  '/login',
  body('email').isEmail(),
  body('password').isString(),
  validateOrFail,
  async (req, res, next) => {
    try {
      const user = await User.findOne({ email: req.body.email });
      if (!user) return res.status(401).json({ message: 'Invalid credentials' });

      const ok = await user.comparePassword(req.body.password);
      if (!ok) return res.status(401).json({ message: 'Invalid credentials' });

      const token = jwt.sign({ id: user._id, email: user.email }, process.env.JWT_SECRET, { expiresIn: '8h' });
      res.json({ token });
    } catch (err) { next(err); }
  }
);

module.exports = router;

