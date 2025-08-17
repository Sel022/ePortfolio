# Code Review

This informal code review explains existing functionality, analyzes areas for improvement, and walks through the planned enhancements.  
The intended audience is peers and managers, with the goal of **clarity over heavy technical detail**.

---

## A. Existing Functionality

### CS 350 – Smart Thermostat (Raspberry Pi)
- Reads room temperature via **AHT20 sensor (I2C)**  
- Implements system states: **OFF, HEAT, COOL**  
- Provides visual feedback with **LEDs** (red/blue)  
- Displays status and time on **16x2 LCD**  
- Logs state, room temperature, and setpoint via **UART** every 30 seconds  

### CS 465 – MEAN Full-Stack Travel App
- Implements **Single-Page Application (SPA)** routing with Angular  
- Provides **user login workflow** and session handling  
- Displays a **trips listing** with interactive navigation  
- Allows **trip editing** via form  
- REST API integrates with **MongoDB** for data persistence  

---

## B. Code Analysis (Improvement Targets)

- **Structure & Readability**  
  - Improve modularity (separate sensor, display, control logic)  
  - Use meaningful naming conventions  

- **Logic & Efficiency**  
  - Clarify state machine transitions  
  - Introduce **non-blocking timers** to replace fixed delays  
  - Add pagination for large data sets (CS 465)  

- **Testing & Observability**  
  - Create mockable interfaces for hardware components  
  - Strengthen logging for debugging and monitoring  

- **Security**  
  - Enforce authentication/authorization checks (CS 465)  
  - Validate user inputs against injection attacks  
  - Apply **least-privilege operations** on MongoDB  

- **Documentation**  
  - Add consistent commenting across modules  
  - Maintain updated README and developer notes  

---

## C. Enhancement Plan (and Outcomes Alignment)

### CS 350 – Smart Thermostat
- **Software Design & Engineering**: Split project into modules (sensor service, LCD service, UART service); improve button handling for reliability  
- **Algorithms & Data Structures**: Introduce hysteresis and timer-based scheduling to stabilize heating/cooling transitions and avoid rapid switching  

### CS 465 – MEAN Full-Stack Travel App
- **Databases**: Strengthen schema validation; add database indexes for faster lookups; secure API routes with authentication; add pagination for trip queries  

---

## 📺 Code Review Video
👉 [Watch Code Review Video](YOUR_VIDEO_LINK_HERE)  

---

<p align="center">
  <a href="index.md">🏠 Home</a> |
  <a href="cs350_artifact.md">⬅ Previous</a> |
  <a href="cs465_artifact.md">Next ➡</a>
</p>

---


This review connects existing features to identified gaps and defines a clear enhancement path, aligned with the **capstone learning outcomes**.
