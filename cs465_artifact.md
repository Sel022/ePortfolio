# Artifact 2 — CS 465: MEAN Full-Stack Travel Booking App

![Login Page](assets/mean-login.png)  
![Trips List](assets/mean-trips.png)  
![Edit Trip](assets/mean-edit-trip.png)

---

## 📌 Brief Description (What/When)
This artifact is a **MEAN stack single-page travel booking application** developed in **CS 465 – Full Stack Development**.  
The project consists of an **Angular client** and a **Node.js/Express server** with **MongoDB** persistence.  

- **Technologies:** Angular, Express, Node.js, MongoDB, JWT, HTTP Client, Angular Routing  
- **Core Features (original):** Login workflow, view trips, edit trips, API consumption via Angular services  
- **Enhanced Features:** Database schema validation, JWT-based authentication, Angular `AuthInterceptor`, route guards, pagination, error handling, and secure queries  

---

## 🎯 Why This Artifact?
I chose this artifact because it highlights my ability to **design, enhance, and secure full-stack applications**, showcasing the **Databases** and **Security Mindset** outcomes.  
Enhancing this app gave me practical experience in **schema validation**, **REST API design**, and **front-to-back authentication**.  

---

## 🔧 Enhancements Implemented
- **Databases (MongoDB):**  
  - Added schema validation, required constraints, and field typing.  
  - Introduced indexes (`trips.slug`, `bookings.userId`) for scalability.  
  - Implemented pagination for trips listing.  

- **Security:**  
  - JWT-based authentication in server routes.  
  - Angular `AuthInterceptor` for attaching tokens to requests.  
  - Route guards in Angular to protect secure pages.  
  - Input sanitization and principle of least privilege in DB operations.  

- **API & Backend:**  
  - Centralized error middleware for cleaner responses.  
  - Standardized status codes and DTOs for consistency.  

- **Frontend (Angular):**  
  - Improved TripService with typed responses.  
  - Added BookingService consuming new API endpoints.  
  - Better UX with consistent error handling and form validation.  

---

## 💡 Reflection (Process, Challenges, Feedback)
- **What I learned:** Secure API design requires thinking across **client and server**. Schema enforcement prevents invalid data, while JWT and guards ensure only authenticated users can access sensitive operations.  
- **Challenges:** Syncing Angular route guards with backend token checks — solved by unifying auth logic.  
- **Feedback incorporated:** Clearer API docs, improved DTO definitions, and more user-friendly error messages.  
- **Outcomes met:**  
  - **Databases:** schema validation, indexing, safe queries  
  - **Security Mindset:** authentication, authorization, input sanitization  
  - **Software Design & Engineering:** modular server controllers and Angular services  
  - **Communication:** API docs, comments, and professional markdown  

---

## 📂 Supporting Files
- [Original Code (Client + Server)](artifact2_CS465/original_code/)  
- [Enhanced Code (Client + Server + DB/Security Enhancements)](artifact2_CS465/enhanced_code/)  
- [Narrative Document (DOCX)](Artifact2_CS465_Narrative.docx)  
- [Code Review (Markdown)](artifact2_CS465/code_review_cs465.md)  

---

## 📌 Capstone Outcomes Alignment
This artifact demonstrates my achievement of the following program outcomes:  
- **Databases:** improved schemas, indexes, and queries  
- **Security Mindset:** secure API design and authorization  
- **Software Design & Engineering:** maintainable full-stack structure  
- **Professional Communication:** professional documentation and review  

---

👉 *Next: [Code Review](artifact2_CS465/code_review_cs465.md)*  
