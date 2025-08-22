# logger.py
from config import get_db
import datetime

def write_log(state, temperature, setpoint):
    """
    Writes a log entry into the MongoDB 'logs' collection.
    """
    db = get_db()
    logs = db["logs"]
    log_entry = {
        "timestamp": datetime.datetime.utcnow(),
        "state": state,
        "temperature": temperature,
        "setpoint": setpoint
    }
    logs.insert_one(log_entry)
    print("[DB] Log saved:", log_entry)
