# Artifact 2 — CS 465: MEAN Full-Stack Travel Booking App

## Brief Description (What/When)
A **MEAN** stack single-page application for travel booking with **Angular** (SPA), **Express/Node.js** API, and **MongoDB** for persistence. Features include login, viewing trips, and editing trips.

- **Technologies:** Angular, Express, Node.js, MongoDB, JWT/Session  
- **Core features:** Authenticated login, trips listing, trip edit/create, API consumption via Angular services, RESTful backend  
- **Original course:** CS 465 – Full Stack Development  

---

## Why This Artifact? (Justification)
This artifact demonstrates the **Databases** enhancement category, including schema design, validation, indexing, and secure API operations. It also shows full-stack deployment and integration.

---

## Enhancements Implemented
- **Schema Design:** `users`, `trips`, `bookings` with validation.  
- **Validation & Sanitization:** server-side checks, protected routes.  
- **Indexes & Performance:** pagination and indexing on common fields.  
- **Auth considerations:** secure routes, token/session checks, minimal data exposure.  
- **Error handling:** centralized error middleware.  

---

## Reflection
- **What I learned:** Schema definitions and validation simplify logic; indexes + pagination improve UX.  
- **Challenges:** Coordinating Angular guards with backend auth; solved with consistent 401/403 responses.  
- **Feedback incorporation:** Improved API docs, DTOs, and clearer error messages.  
- **Outcomes met:**  
  - Databases  
  - Communication  
  - Security mindset  

---

👉 *Next: [Code Review](code_review.md)*  
