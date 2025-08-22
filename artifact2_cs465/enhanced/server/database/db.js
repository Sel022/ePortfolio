// db.js - MongoDB connection helper

const mongoose = require('mongoose');

const connectDB = async () => {
  try {
    // MONGO_URI must be defined in your .env file
    const conn = await mongoose.connect(process.env.MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      autoIndex: true, // useful for development
    });

    console.log(`✅ MongoDB Connected: ${conn.connection.host}/${conn.connection.name}`);
  } catch (error) {
    console.error(`❌ MongoDB Connection Error: ${error.message}`);
    process.exit(1); // Exit process on DB failure
  }
};

module.exports = connectDB;

