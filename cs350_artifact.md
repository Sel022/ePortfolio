# Artifact 1 — CS 350: Smart Thermostat (Raspberry Pi)

![Thermostat Overview](assets/thermostat-overview.jpg)  
*Raspberry Pi Smart Thermostat with LCD, LEDs, and buttons.*

---

## 📌 Brief Description (What/When)
A Raspberry Pi–based smart thermostat that:  
- Reads room temperature from an **AHT20 sensor (I2C)**  
- Displays time, temperature, and state on a **16×2 LCD**  
- Uses **two LEDs (red/blue)** to indicate HEAT / COOL  
- Provides **three push buttons** to toggle OFF / HEAT / COOL modes and adjust the setpoint  
- Logs telemetry periodically via **UART** for monitoring  

**Technologies:** Raspberry Pi GPIO / I2C / UART, Python, 16×2 LCD, LEDs, buttons  
**Core Features:** Sensor read, state machine control, LED PWM feedback, LCD updates, UART logging  
**Original Course:** CS 350 – Emerging Systems Architectures and Technologies  

---

## ❓ Why This Artifact?
This artifact demonstrates:  
- **Embedded software design & engineering** under real-time constraints  
- **Hardware integration** with sensors, buttons, and displays  
- **Algorithmic control** through a finite-state machine and hysteresis logic  

It is an ideal example of modular design, testing strategies, and applying a security mindset (e.g., safe GPIO access).  

---

## 🔧 Enhancements Implemented

### 1) Software Design & Engineering
- **Modular architecture**: Separated into `sensor.py`, `state.py`, `io.py`, `display.py`, `logger.py`, `app.py`  
- **State machine abstraction**: OFF / HEAT / COOL encapsulated with transitions, guards, and handlers  
- **LCD + UART services**: Dedicated interfaces for display updates and 30s periodic telemetry logging  
- **Testability**: Dependency injection for sensor + IO layers (mockable PIN / SERIAL interfaces)  
- **Error handling**: Graceful handling of I2C errors and debounced button inputs  

### 2) Algorithms & Data Structures
- **Hysteresis control**: Avoided rapid toggling around setpoint with a ±0.5–1.0° deadband  
- **Time-based duties**: Non-blocking timers for UART logging and LCD status switching  
- **Finite-state logic**: Deterministic transitions with explicit entry/exit and LED PWM effects  

---

## 💡 Reflection (Process, Challenges, Feedback)

- **What I Learned:**  
  - Embedded apps benefit from modular state isolation, debounced inputs, and non-blocking timing  
  - A small hysteresis improves user experience by reducing “chatter” around setpoints  

- **Challenges:**  
  - Managing concurrency (buttons, display, logging) without threads → solved via timed tasks and update loops  

- **Feedback Incorporated:**  
  - Increased inline documentation  
  - Standardized naming conventions  
  - Added a “safe-off” routine for GPIO cleanup  

- **Capstone Outcomes Met:**  
  - **Design & Engineering:** modularization, test hooks, robust error handling  
  - **Algorithms & Data:** state machine trade-offs, hysteresis, timing logic  
  - **Security Mindset:** validated inputs, safe GPIO handling, avoided blocking IO  

---

## 🛠️ Technical Appendix (Pseudocode)

```python
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
