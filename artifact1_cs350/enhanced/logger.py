# logger.py
import time
from db_config import get_db

db = get_db()
logs = db["logs"]

def write_log(state, temp, setpoint):
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "state": state,
        "temperature": temp,
        "setpoint": setpoint
    }
    logs.insert_one(log_entry)
    print(f"[DB LOGGED] {log_entry}")

