# Code Reviews

This page provides written reviews for the two enhanced artifacts in my CS 499 ePortfolio.  
Each review explains the **original functionality**, identifies **areas for improvement**, and outlines the **enhancement plan** aligned with program outcomes.  

---

## 🖥️ Code Review – CS 350: Smart Thermostat (Raspberry Pi)

### A. Existing Functionality
The original CS 350 thermostat project used a Raspberry Pi with Python to:  
- Read temperature from an **AHT20 sensor (I2C)**  
- Display time, temperature, and system state on a **16×2 LCD**  
- Indicate HEAT/COOL modes using **PWM-controlled LEDs**  
- Allow user input via three buttons (state toggle, setpoint adjust)  
- Log data periodically through **UART**  

### B. Code Analysis (Improvement Targets)
- **Structure & Readability:** Monolithic file, limited modularity, difficult to test.  
- **Logic & Efficiency:** Lacked hysteresis, making setpoint control noisy. Blocking delays slowed responsiveness.  
- **Error Handling:** No handling for I2C read errors or button bounce.  
- **Testability:** Direct hardware calls made mocking and simulation difficult.  
- **Documentation:** Minimal comments and inconsistent naming.  

### C. Enhancement Plan
- **Software Design & Engineering:** Refactored into modules (`sensor.py`, `state.py`, `io.py`, `display.py`, `logger.py`, `app.py`) for clarity and maintainability.  
- **Algorithms & Data Structures:** Added **hysteresis control** and **non-blocking timers** for smoother control and logging.  
- **Security & Reliability:** Input validation for setpoints, debounced button handling, safe GPIO cleanup.  
- **Professional Practices:** Increased code comments, consistent naming, and clear separation of concerns.  

### Outcome Alignment
- **Design & Engineering:** Improved modularity and test hooks.  
- **Algorithms & Data Structures:** Implemented state machine and timing-based control.  
- **Security Mindset:** Ensured safe access to GPIO and validated user inputs.  
- **Communication:** Code comments and organized architecture improved readability.  

---

## 🌐 Code Review – CS 465: MEAN Full-Stack Travel Booking App

### A. Existing Functionality
The original CS 465 project implemented a MEAN stack application with:  
- **Angular SPA** frontend featuring login, trips list, and trip editing form  
- **Express/Node.js REST API** for serving trips and handling updates  
- **MongoDB** backend for persistent storage  
- Basic CRUD functionality for user trips  

### B. Code Analysis (Improvement Targets)
- **Databases:** Schema definitions were minimal and lacked strong validation.  
- **Security:** No robust authentication/authorization; API routes were open.  
- **Performance:** Trip listing lacked pagination or query optimization.  
- **Error Handling:** Responses were inconsistent and lacked centralized handling.  
- **Frontend:** No HTTP interceptors or route guards to protect user navigation.  

### C. Enhancement Plan
- **Databases:** Added stronger **schemas with validation and sanitization**, as well as **indexes** for common queries.  
- **Security:** Implemented **JWT-based authentication**, protected routes, and Angular `AuthInterceptor` for attaching tokens.  
- **Performance:** Added **pagination** and query limits for trips list.  
- **Error Handling:** Centralized error middleware in Express and consistent HTTP status codes.  
- **Frontend:** Introduced Angular **route guards** and improved UI feedback on errors.  

### Outcome Alignment
- **Databases:** Demonstrated proper schema design, validation, and indexing.  
- **Security Mindset:** Enforced authentication and safe API patterns.  
- **Design & Engineering:** Integrated client and server cleanly with documented APIs.  
- **Communication:** Clear API documentation and frontend/backend consistency improved maintainability.  

---

## 🎯 Closing Note
Together, these reviews demonstrate the process of evaluating original code, identifying key areas for improvement, and applying enhancements that align with the **CS program outcomes**:  
- **Software Design & Engineering**  
- **Algorithms & Data Structures**  
- **Databases**  
- **Security**  
- **Professional Communication**  

These reviews, along with the enhanced codebases, show my ability to critically analyze, improve, and communicate about real-world software systems.
