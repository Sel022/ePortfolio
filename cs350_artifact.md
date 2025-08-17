# Artifact 1 — CS 350: Smart Thermostat (Raspberry Pi)

![Thermostat Overview](assets/thermostat-overview.jpg)

## Brief Description (What/When)
A Raspberry Pi-based smart thermostat that reads room temperature (AHT20 over I2C), displays status on a 16×2 LCD, and uses two LEDs (red/blue) to indicate **HEAT/COOL**. Three buttons manage **OFF / HEAT / COOL** modes and adjust the setpoint. The system logs telemetry via **UART** for monitoring.

- **Technologies:** Raspberry Pi GPIO/I2C/UART, Python, LCD (16×2), LEDs + buttons  
- **Core features:** Sensor read, state machine control, LED PWM feedback, LCD updates, UART logging  
- **Original course:** CS 350 – Emerging Systems Architectures and Technologies

![Wiring Diagram / Breadboard](assets/thermostat-wiring.jpg)
![LCD + LEDs in action](assets/thermostat-lcd.jpg)

---

## Why This Artifact? (Justification)
This artifact showcases embedded **software design and engineering** with real-time constraints and hardware integration, plus **algorithmic control** (state machine, hysteresis). It is a good platform to demonstrate clean modular code, testing hooks, and secure hardware access patterns.

---

## Enhancements Implemented

### 1) Software Design & Engineering
- **Modular architecture:** Split code into modules (e.g., `sensor.py`, `state.py`, `io.py`, `display.py`, `logger.py`, `app.py`), enabling isolated testing and clearer responsibilities.
- **State machine abstraction:** OFF/HEAT/COOL encapsulated with transitions, guards, and handlers.
- **LCD + UART services:** Dedicated interfaces for status display and periodic telemetry (e.g., every 30s) for diagnostics.
- **Testability:** Dependency injection for sensor + IO layers (mockable PIN/SERIAL interfaces).
- **Error handling:** Graceful handling for I2C read errors and debounced button input.

### 2) Algorithms & Data Structures
- **Hysteresis control:** Avoid rapid toggling around the setpoint by using a small deadband (e.g., ±0.5–1.0°).  
- **Time-based duties:** Scheduled UART logging and LCD switching (clock vs. status/temperature) with non-blocking timers.  
- **Finite-state logic:** Deterministic transitions with explicit entry/exit behaviors for LED PWM effects.

---

## Reflection (Process, Challenges, Feedback)
- **What I learned:** Designing embedded applications benefits from **state isolation**, **debounced inputs**, and **non-blocking timing**. A small hysteresis greatly improves user experience.
- **Challenges:** Managing concurrent concerns (buttons, display, logging) without threads—solved via timed tasks and clear update loops.
- **Feedback incorporation:** Increased code comments, standardized naming, and added a “safe-off” routine for GPIO cleanup.
- **Outcomes met:** 
  - **Design & Engineering:** modularization, test hooks, error handling.  
  - **Algorithms & Data:** state machine + hysteresis trade-offs and timing logic.  
  - **Security mindset:** validated inputs, ensured safe GPIO access, and avoided unsafe blocking IO.

---

## Technical Appendix (Pseudocode snippet)

```text
loop tick:
  now = monotonic()
  if now - last_sensor_read >= SENSOR_PERIOD:
      temp = sensor.read()
      state.update(temp, setpoint)
      last_sensor_read = now

  display.update(now, temp, setpoint, state.mode)

  io.apply_leds(state.mode, temp, setpoint)

  if now - last_uart_log >= LOG_PERIOD:
      logger.write({time, temp, setpoint, state.mode})
      last_uart_log = now

  handle_buttons()  # debounced; adjust setpoint; cycle modes
```
