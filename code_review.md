# Code Review (Video + Notes)

**Video:** _(Add your link here — YouTube/Vimeo/Drive)_  

This informal code review explains existing functionality, analyzes improvement areas, and walks through the planned enhancements. The audience is peers/manager; the goal is clarity over heavy technical detail.

## A. Existing Functionality
- **CS 350 Thermostat:** Sensor read (AHT20/I2C), state modes (OFF/HEAT/COOL), LEDs + LCD updates, UART logging cadence.
- **CS 465 MEAN App:** SPA routing, login workflow, trips listing, edit trip form; REST API consuming MongoDB.

## B. Code Analysis (improvement targets)
- Structure & readability (modularity, naming)
- Logic & efficiency (state machine clarity, non-blocking timers, pagination)
- Testing & observability (mockable interfaces, logging)
- Security (auth checks, input validation, least-privilege DB operations)
- Commenting & docs

## C. Enhancement Plan (and outcomes alignment)
- **Design & Engineering (CS 350):** module split, LCD/UART services, robust button handling.
- **Algorithms & Data (CS 350):** hysteresis and timer-based scheduling to stabilize control.
- **Databases (CS 465):** schema validation, indexes, protected routes, pagination.
