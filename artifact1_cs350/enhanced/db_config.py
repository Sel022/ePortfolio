# db_config.py
from pymongo import MongoClient

def get_db():
    # Replace with your MongoDB connection string
    client = MongoClient("mongodb://localhost:27017/")
    db = client["thermostat_db"]
    return db

