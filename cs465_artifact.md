# Artifact 2 — CS 465: MEAN Full-Stack Travel Booking App

![Login Page](assets/mean-login.png)  
![Trips List](assets/mean-trips.png)  
![Edit Trip](assets/mean-edit-trip.png)  

---

## 📖 Brief Description (What/When)
A **MEAN stack** single-page application (SPA) for travel booking with **Angular** frontend, **Express/Node.js** backend, and **MongoDB** database persistence.  
Features include user login, viewing trips, and editing trips.  

- **Technologies:** Angular, Express, Node.js, MongoDB, JWT/Session, HTTP Client, Routing  
- **Core features:** Authenticated login, trips listing, trip edit/create, API consumption via Angular services, RESTful backend  
- **Original course:** CS 465 – Full-Stack Development  

---

## 💡 Why This Artifact?
This artifact was chosen because it demonstrates **database design and integration**, applied from **CS 340 Database Management** into a full-stack application.  
The enhancements show secure schema validation, indexing, pagination, and error handling — turning a functional prototype into a more production-ready system.  

---

## 🔧 Enhancements Implemented

### 1. Databases (from CS 340)
- Schema design with validation & sanitization  
- Pre-save checks in Mongoose models  
- Indexed fields (e.g., slug) for query optimization  
- Added pagination in GET endpoints for scalability  
- Centralized error middleware  

### 2. Security & API Hardening
- Protected sensitive routes with **requireAuth** middleware  
- Enforced least-privilege access (users can only create/manage their own trips)  
- Sanitized inputs before DB operations  
- Standardized status codes & error responses  

### 3. Frontend Enhancements
- Angular services now support **pagination parameters**  
- Integrated auth tokens into HTTP requests  
- Improved error feedback in the UI  

---

## 🔎 Reflection
- **What I learned:** Database schema design and indexes reduce bugs and improve performance. Pagination ensures scalability, and strong authentication provides security.  
- **Challenges:** Coordinating Angular guards with backend middleware; handling pagination without breaking UI.  
- **Feedback Applied:** Clearer API docs, improved error messages, standardized DTOs.  

---

## 🎯 Outcomes Met
- **Databases:** schema, indexing, validation, safe query patterns  
- **Software Design & Engineering:** modular backend, Angular services  
- **Security Mindset:** authenticated routes, sanitized inputs  
- **Professional Communication:** improved UX docs & messages  

---

👉 *Next: [Code Review](code_review.md)*  
