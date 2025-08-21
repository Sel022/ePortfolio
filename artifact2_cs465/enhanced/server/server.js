require('dotenv').config();
const express = require('express');
const helmet = require('helmet');
const morgan = require('morgan');
const cors = require('cors');
const mongoose = require('mongoose');

const { errorHandler, notFound } = require('./middleware/error');

const authRoutes = require('./routes/auth');
const tripRoutes = require('./routes/trips');
const bookingRoutes = require('./routes/bookings');

const app = express();

// Security & middleware
app.use(helmet());
app.use(cors({ origin: process.env.CORS_ORIGIN || true }));
app.use(express.json());
app.use(morgan('dev'));

// DB
mongoose.connect(process.env.MONGO_URI, {
  autoIndex: true
}).then(() => console.log('MongoDB connected'))
  .catch(err => console.error('Mongo error:', err.message));

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/trips', tripRoutes);
app.use('/api/bookings', bookingRoutes);

// 404 + error
app.use(notFound);
app.use(errorHandler);

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`API running on :${port}`));

