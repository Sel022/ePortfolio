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


# Code Review — CS 465 MEAN Full-Stack Travel Booking App

This code review covers the **original CS465 travel booking application** and the **enhanced version with database and security improvements**.  
The goal is to highlight functionality, improvement areas, and rationale for enhancements.

---

## A. Existing Functionality
- **Client (Angular)**  
  - Login page with form validation.  
  - Trips list with navigation to detail pages.  
  - Edit trip form for updating trip information.  
  - Angular services consume REST API.  

- **Server (Node.js/Express)**  
  - API routes for users and trips.  
  - MongoDB persistence for travel booking data.  
  - Basic error handling.  

---

## B. Code Analysis (Improvement Targets)
1. **Structure & Readability**  
   - Client services lacked centralized auth handling.  
   - Server controllers mixed logic and error responses.  

2. **Database Layer**  
   - Minimal schema constraints; risk of invalid data.  
   - No indexes → performance issues with large datasets.  

3. **Security**  
   - Missing route protection.  
   - No sanitization of inputs → injection risk.  
   - Password handling simplistic.  

4. **Performance & UX**  
   - No pagination on trips endpoint (all results returned).  
   - Client-side auth state not persisted.  

5. **Documentation**  
   - Limited inline comments and API route docs.  

---

## C. Enhancements Implemented
- **Databases**: Defined `users`, `trips`, `bookings` schemas with validation (required fields, types). Added indexes to `trips.slug` and `bookings.userId`.  
- **Security**: Implemented JWT authentication, added an Angular `AuthInterceptor` to auto-attach tokens, and protected server routes.  
- **API & Server**: Added centralized error-handling middleware, standardized JSON error responses, and secured update/delete operations.  
- **Client**: Integrated Angular route guards, improved TripService with typed DTOs, added booking feature consuming new API endpoints.  
- **Performance**: Implemented pagination on `/api/trips` route to avoid loading all records.  

---

## D. Outcomes Alignment
- **Databases**: Stronger schema enforcement, indexing, validation.  
- **Security Mindset**: Authentication, authorization, sanitized inputs, least-privilege DB ops.  
- **Software Design & Engineering**: Modularization of controllers, improved client services.  
- **Communication**: Documented API endpoints and improved error messages.  

---

## E. Reflection
Through this review, I learned the importance of **consistent security practices across front and back end**. Adding database validation and token-based authentication reduced both runtime errors and potential vulnerabilities. Feedback from peers was incorporated into the enhanced API docs and DTOs.  

The final system is more secure, performant, and professional, demonstrating my ability to **design and enhance full-stack applications** with industry best practices.

