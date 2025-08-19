CS-350 Thermostat — Code Review (Original → Enhanced)

Scope & Audience. This review explains functionality, issues, and improvements made to the Module 7 thermostat. Audience: peers/manager; emphasis on clarity, reliability, and maintainability.

A. Existing Functionality (Original)

Hardware: AHT20 (I²C) temp sensor, 16×2 LCD, two PWM LEDs (heat/cool), three buttons (mode/up/down).

Behavior: Reads temperature once at start, then simulates room temp via buttons; cycles modes; toggles LCD lines; fades LEDs; prints UART line ~30s.

Strengths: Clear hardware mapping, straightforward LED feedback, simple state cycling.

B. Issues & Improvement Targets

Single monolithic file → hard to unit-test or extend.

No hysteresis → possible rapid toggling around setpoint.

Blocking LED fades → long time.sleep() loops cause sluggish input/UI.

Sensor sampling: initial snapshot “locks” the temp; no continuous reads.

Buttons: no formal debouncing → false triggers.

Observability: UART only; no structured persistence to analyze trends.

Maintainability/Safety: no GPIO cleanup abstraction; mixed concerns.

C. Enhancement Summary

Design & Engineering: split into modules (app.py, config.py, sensor.py, state.py, io_hw.py, display.py, telemetry.py) for isolation and testing; safe cleanup; named constants.

Algorithms & Data: added hysteresis (+/-1°F) and non-blocking timers for sensor/LCD/logging; deterministic state logic.

Security/Robustness: debounced buttons; exception handling for sensor reads; minimal DB write on failure fallback.

Databases (from CS-340): added MongoDB telemetry with timestamped documents and an index on ts to support analysis/dashboards; consistent schema fields (state, tempF, setpointF).

Observability: kept UART prints and added persistent telemetry for later visualization (Grafana, Aggregation Pipeline, notebooks).

D. Outcome Alignment

Software Design & Engineering: modular architecture; dependency boundaries; testability.

Algorithms & Data Structures: hysteresis, timer scheduling, deterministic FSM.

Databases: MongoDB logging, indexing, structured documents.

Security Mindset: debouncing (input validation), safe GPIO off-path, controlled error handling.

Communication: clear file layout, names, and comments.

E. How to Run (Enhanced)
# On Raspberry Pi
pip3 install adafruit-circuitpython-charlcd adafruit-circuitpython-ahtx0 pymongo
# Set MongoDB in config.py (MONGO_URI). For local DB, install MongoDB or use Atlas URI.
python3 app.py
