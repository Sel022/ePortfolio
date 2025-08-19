import time
from datetime import datetime, timezone
from pymongo import MongoClient, ASCENDING
from pymongo.errors import PyMongoError

class Telemetry:
    def __init__(self, mongo_uri: str, db_name: str, coll_name: str):
        self._client = MongoClient(mongo_uri, serverSelectionTimeoutMS=3000)
        self._db = self._client[db_name]
        self._coll = self._db[coll_name]
        # Minimal schema expectations (document shape)
        # Create index on timestamp for efficient time-range queries
        self._coll.create_index([("ts", ASCENDING)], name="ts_idx", background=True)

    def log(self, state_name: str, temp_f: float, setpoint_f: float):
        doc = {
            "ts": datetime.now(timezone.utc),
            "state": state_name,
            "tempF": round(float(temp_f), 2),
            "setpointF": round(float(setpoint_f), 1),
        }
        try:
            self._coll.insert_one(doc)
        except PyMongoError as e:
            # Fallback to console; don't crash runtime
            print(f"[DB WARN] insert failed: {e}")

def uart_log(state_name: str, temp_f: float, setpoint_f: float):
    print(f"{state_name.lower()},{temp_f:.1f},{int(setpoint_f)}")

