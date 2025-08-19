# Artifact 1 — CS 350: Smart Thermostat (Raspberry Pi)

## Brief Description (What/When)
A Raspberry Pi-based smart thermostat that reads room temperature (AHT20 over I2C), displays status on a 16×2 LCD, and uses two LEDs (red/blue) to indicate HEAT/COOL. Three buttons manage OFF / HEAT / COOL modes and adjust the setpoint. The system logs telemetry via UART for monitoring.

- **Technologies:** Raspberry Pi GPIO/I2C/UART, Python, LCD (16×2), LEDs + buttons  
- **Core features:** Sensor read, state machine control, LED PWM feedback, LCD updates, UART logging  
- **Original course:** CS 350 – Emerging Systems Architectures and Technologies  

---

## Why This Artifact? (Justification)
This artifact showcases embedded software design and engineering with real-time constraints and hardware integration, plus algorithmic control (state machine, hysteresis).  

---

## Enhancements Implemented
1. **Software Design & Engineering**  
   - Modular architecture (split into sensor.py, state.py, io.py, display.py, logger.py, app.py).  
   - State machine abstraction for OFF/HEAT/COOL.  
   - LCD + UART services with periodic telemetry.  
   - Testability via mockable interfaces.  
   - Error handling for I2C reads and button debounce.  

2. **Algorithms & Data Structures**  
   - Hysteresis control to prevent rapid toggling.  
   - Non-blocking timers for UART logging and LCD toggles.  
   - Deterministic state transitions with LED PWM effects.  

---

## Reflection
- **What I learned:** Embedded design benefits from state isolation, debounced inputs, and non-blocking timing.  
- **Challenges:** Managing concurrency without threads; solved via timed tasks.  
- **Feedback incorporation:** Clearer comments, standardized naming, GPIO “safe-off” routine.  
- **Outcomes met:**  
  - Software Design & Engineering  
  - Algorithms & Data Structures  
  - Security mindset with safe GPIO and input validation  

---

👉 *Next: [Artifact 2 – CS 465: MEAN Travel Booking App](cs465_artifact.md)*  
