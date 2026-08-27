# PFGuide Architecture

## Overview

PFGuide is a full-stack prototype designed to demonstrate a simpler citizen journey for understanding confusing PF claim statuses and deciding what to do next.

The system consists of:

- A React + Vite frontend for the citizen experience
- A FastAPI backend for application logic and API endpoints
- Service-layer logic for claim, explanation, and grievance workflows
- Synthetic JSON data used instead of real citizen or government data

```text
Citizen
   ↓
React + Vite Frontend
   ↓
API Service Layer
   ↓
FastAPI Routes
   ↓
Application / Explanation / Grievance Services
   ↓
Synthetic JSON Data
```

The frontend and backend are deployed separately and communicate through HTTP API requests.

No live EPFO or government system is accessed.

---

## 1. Frontend Architecture

The frontend is built with React and Vite.

Its responsibility is to guide the citizen through the complete journey:

```text
Welcome
   ↓
Start Demo
   ↓
Claim Overview
   ↓
Claim Explanation
   ↓
Actionable Next Steps
   ↓
Grievance Draft
   ↓
Review and Edit
   ↓
Simulated Submission
   ↓
Success + Synthetic Reference Number
```

The frontend includes:

- Page-based citizen flow
- Dedicated API communication layer
- Loading states
- Error states
- Retry behavior
- Responsive styling
- Clear notices that data and submissions are synthetic

The design keeps one clear primary action available at each major stage.

---

## 2. Backend Architecture

The backend is built using FastAPI.

Its responsibility is to expose API endpoints and coordinate the application logic required for the prototype.

```text
HTTP Request
   ↓
FastAPI Route
   ↓
Service Logic
   ↓
Synthetic Data Access
   ↓
Structured Response
   ↓
Frontend
```

The backend handles:

- Synthetic demo authentication
- Claim and application lookup
- Claim status retrieval
- Plain-language explanation generation
- Actionable next-step guidance
- Grievance draft generation
- Simulated grievance submission
- Synthetic reference number generation

Pydantic models are used for structured request and response validation.

---

## 3. Claim Explanation Flow

A core goal of PFGuide is to transform a claim status into an understandable explanation.

```text
Synthetic Claim Data
   ↓
Application Service
   ↓
Claim Status
   ↓
Explanation Logic
   ↓
What Happened?
   ↓
Why Did It Happen?
   ↓
What Can I Do Now?
   ↓
Citizen-Friendly Response
```

The explanation flow uses deterministic structured application logic.

No external AI service or live government data is required for the prototype.

---

## 4. Grievance Flow

If the citizen still needs assistance after reviewing the explanation and next steps, PFGuide continues the journey through a simulated grievance flow.

```text
Citizen
   ↓
Request Grievance Draft
   ↓
Grievance Service
   ↓
Generate Editable Draft
   ↓
Citizen Reviews and Edits
   ↓
Simulated Submission
   ↓
Synthetic Reference Number
```

The grievance is not sent to EPFO, any government agency, or any external service.

The reference number is generated only within the prototype.

---

## 5. Data Architecture

PFGuide uses synthetic JSON data.

The prototype intentionally simulates:

- Users
- Claim information
- Claim statuses
- Verification details
- Grievance data
- Grievance submissions
- Reference numbers

```text
Synthetic JSON Files
        ↓
Data / Service Layer
        ↓
FastAPI Responses
        ↓
React Frontend
```

No real citizen information is required to use the prototype.

---

## 6. Deployment Architecture

The application is deployed as separate frontend and backend services.

```text
Citizen Browser
      ↓
Deployed React + Vite Frontend
      ↓ HTTPS API Requests
Deployed FastAPI Backend
      ↓
Synthetic JSON Data
```

Environment configuration is used to provide the frontend with the backend API base URL.

CORS configuration allows the deployed frontend to communicate with the backend.

---

## 7. Error Handling and Resilience

The prototype includes handling for common request failures.

```text
Citizen Action
      ↓
API Request
   ↙       ↘
Success     Failure
  ↓            ↓
Next Step    Error State
                 ↓
               Retry
```

This allows the citizen to recover from temporary request failures instead of reaching a dead end.

The frontend also includes loading states while asynchronous operations are in progress.

---

## 8. Safety and Mock Boundaries

PFGuide intentionally avoids direct integration with live public-service systems.

The prototype:

- Does not connect to EPFO
- Does not connect to any live government system
- Does not process real PF account information
- Does not use real Aadhaar or PAN information
- Does not process real passwords or OTPs
- Does not process payments
- Does not submit real grievances

All claim information, user information, grievance data, submissions, and reference numbers are synthetic.

These boundaries allow the complete citizen journey to be demonstrated without exposing sensitive information or interacting with production government systems.

---

## 9. Future Production Architecture

A production implementation could retain the same citizen-facing architecture while replacing the synthetic data layer with authorized and secure integrations.

```text
Citizen
   ↓
Secure Authentication
   ↓
PFGuide Citizen Experience
   ↓
Secure Backend Services
   ↓
Authorized Government APIs
   ↓
Official Public-Service Systems
```

A production system would additionally require:

- Authorized API access
- Explicit citizen consent
- Strong authentication
- Encryption in transit and at rest
- Data minimization
- Role-based access control
- Audit logging
- Rate limiting
- Monitoring
- Incident response
- Human escalation for uncertain or sensitive cases

## Summary

PFGuide separates the citizen experience, backend application logic, and synthetic data layer so that the complete journey can be tested safely.

The architecture supports the main prototype flow from claim understanding to simulated grievance submission while clearly separating working functionality from mocked government dependencies.
