# Artifact 2 — CS 465: MEAN Full-Stack Travel Booking App

![Login Page](assets/mean-login.png)
![Trips List](assets/mean-trips.png)
![Edit Trip](assets/mean-edit-trip.png)

## Brief Description (What/When)
A **MEAN** stack single-page application for travel booking with **Angular** (SPA), **Express/Node.js** API, and **MongoDB** for persistence. Features include login, viewing trips, and editing trips.

- **Technologies:** Angular, Express, Node.js, MongoDB, JWT/Session (as implemented), HTTP Client, Routing
- **Core features:** Authenticated login, trips listing, trip edit/create, API consumption via Angular services, RESTful backend
- **Original course:** CS 465 – Full Stack Development

---

## Why This Artifact? (Justification)
This artifact demonstrates the **Databases** enhancement category, including schema design, validation, indexing, and secure API operations. It also shows front-to-back integration (SPA routing, HTTP services, and backend controllers) with deployability.

---

## Enhancements Implemented

### Databases (MongoDB) + API Hardening
- **Schema design:** `users`, `trips`, `bookings` with clear fields, required constraints, and reference integrity where appropriate.
- **Validation & Sanitization:** Server-side checks for inputs, consistent error responses, and stricter route protection for create/update/delete.
- **Indexes & Performance:** Index common query fields (e.g., `trips.slug`, `bookings.userId`) and apply pagination to list routes.
- **Auth considerations:** Protect sensitive routes; use token/session checks before DB ops; minimize data exposure in responses.
- **Error handling:** Centralized error middleware; standardized status codes and messages.

---

## Reflection (Process, Challenges, Feedback)
- **What I learned:** Thoughtful schema definitions and validation reduce UI errors and simplify business logic. Indexes + pagination keep the UI responsive.
- **Challenges:** Coordinating Angular route guards and backend authorization; resolved by unifying auth logic and returning consistent 401/403 responses.
- **Feedback incorporation:** Clearer API docs, improved DTOs, and better error messages for UX.
- **Outcomes met:** 
  - **Databases:** schema, indexing, validation, and safe query patterns.  
  - **Communication:** clean API docs and consistent HTTP semantics.  
  - **Security mindset:** authenticated routes, sanitized inputs, principle of least privilege.

---

## Example (Express route sketch)

```js
// trips.controller.js (sketch)
router.get('/api/trips', requireAuth, async (req, res, next) => {
  try {
    const page = Math.max(1, parseInt(req.query.page || '1', 10));
    const limit = Math.min(50, Math.max(1, parseInt(req.query.limit || '10', 10)));
    const cursor = Trip.find({}).sort({ startDate: 1 }).skip((page-1)*limit).limit(limit);
    const [items, total] = await Promise.all([cursor.exec(), Trip.countDocuments()]);
    res.json({ items, page, pages: Math.ceil(total/limit), total });
  } catch (err) { next(err); }
});
```
