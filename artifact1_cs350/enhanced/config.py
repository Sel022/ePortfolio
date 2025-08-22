# General configuration for the enhanced thermostat

# --- Control ---
DEFAULT_SETPOINT_F = 72.0
HYSTERESIS_F = 1.0         # +/- deadband to avoid rapid toggling
SENSOR_PERIOD_S = 1.0
LCD_TOGGLE_PERIOD_S = 2.0
UART_PERIOD_S = 30.0
DB_PERIOD_S = 30.0

# --- Pins ---
PIN_BTN_STATE = "D21"
PIN_BTN_UP    = "D22"
PIN_BTN_DOWN  = "D27"

PIN_LED_RED   = "D18"
PIN_LED_BLUE  = "D24"

PIN_LCD_RS    = "D26"
PIN_LCD_EN    = "D19"
PIN_LCD_D4    = "D13"
PIN_LCD_D5    = "D6"
PIN_LCD_D6    = "D5"
PIN_LCD_D7    = "D11"
LCD_COLS = 16
LCD_ROWS = 2

# --- Database (MongoDB) ---
# Example: "mongodb+srv://user:pass@cluster.mongodb.net/?retryWrites=true&w=majority"
MONGO_URI = "mongodb://localhost:27017"   # change to your Atlas URI if needed
MONGO_DB = "snhu_cs350"
MONGO_COLL = "thermostat_logs"

# config.py
from pymongo import MongoClient

def get_db():
    """
    Connects to MongoDB and returns the database object.
    Update the connection string if using MongoDB Atlas or remote server.
    """
    client = MongoClient("mongodb://localhost:27017/")  
    db = client["thermostat_db"]
    return db
