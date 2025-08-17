# Artifact 2 — CS 465: MEAN Full-Stack Travel Booking App

![Login Page](assets/mean-login.png)  
![Trips List](assets/mean-trips.png)  
![Edit Trip](assets/mean-edit-trip.png)  

---

## 📌 Brief Description (What/When)
A **MEAN stack** single-page application for travel booking:  
- **Angular** SPA for the frontend  
- **Express/Node.js** REST API for backend logic  
- **MongoDB** for persistence  

**Core Features:**  
- Authenticated login  
- Viewing trips list  
- Editing / creating trips  
- API consumption via Angular services  
- RESTful backend  

**Technologies:** Angular, Express, Node.js, MongoDB, JWT/Session, Angular HTTP Client, Routing  
**Original Course:** CS 465 – Full Stack Development  

---

## ❓ Why This Artifact?
This artifact highlights **Database and Security enhancements**, focusing on:  
- Schema design & validation  
- Indexing & performance optimization  
- Secure API operations (authentication + authorization)  
- Full-stack integration (Angular SPA ↔ Express API ↔ MongoDB)  

It is a strong demonstration of backend hardening combined with frontend interaction in a deployable full-stack application.  

---

## 🔧 Enhancements Implemented

### Databases (MongoDB) + API Hardening
- **Schema Design:** Defined `users`, `trips`, `bookings` with required constraints and relationships  
- **Validation & Sanitization:** Strong input checks, sanitized data, consistent error responses  
- **Indexes & Performance:** Indexed common query fields (`trips.slug`, `bookings.userId`), added **pagination** for large datasets  
- **Authentication & Authorization:** Protected sensitive routes, token/session checks before DB ops, minimized data exposure  
- **Error Handling:** Centralized Express middleware for clean error handling with standardized status codes  

---

## 💡 Reflection (Process, Challenges, Feedback)

- **What I Learned:**  
  - Schema validation prevents inconsistent data and simplifies logic  
  - Indexing + pagination keeps UI responsive with larger datasets  

- **Challenges:**  
  - Coordinating Angular route guards with backend authorization  
  - Solution: Unified auth logic with consistent **401/403 responses**  

- **Feedback Incorporated:**  
  - Clearer API documentation  
  - Improved Data Transfer Objects (DTOs)  
  - User-friendly error messages  

- **Capstone Outcomes Met:**  
  - **Databases:** schema design, validation, indexing, query optimization  
  - **Communication:** consistent REST API + documentation  
  - **Security Mindset:** authenticated routes, sanitized inputs, principle of least privilege  

---

## 🛠️ Example (Express Route Sketch)

```js
// trips.controller.js (sketch)
router.get('/api/trips', requireAuth, async (req, res, next) => {
  try {
    const page = Math.max(1, parseInt(req.query.page || '1', 10));
    const limit = Math.min(50, Math.max(1, parseInt(req.query.limit || '10', 10)));
    const cursor = Trip.find({})
      .sort({ startDate: 1 })
      .skip((page - 1) * limit)
      .limit(limit);

    const [items, total] = await Promise.all([cursor.exec(), Trip.countDocuments()]);
    res.json({ items, page, pages: Math.ceil(total / limit), total });
  } catch (err) {
    next(err);
  }
});
