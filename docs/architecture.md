# PFGuide Phase 1 Architecture

```text
React + Vite Frontend
        ↓
FastAPI Routes
        ↓
Service Layer
        ↓
Synthetic JSON Data
```

PFGuide is a full-stack prototype with a React/Vite frontend and a FastAPI backend. The frontend handles the citizen journey, while the backend provides synthetic application data, explanations, grievance drafts, and simulated grievance submissions.

No live EPFO or government system is accessed. All user, application, and grievance data in this prototype is synthetic.

## Phase 2 Explanation Flow

```text
Synthetic Application Data
        ↓
Application Service
        ↓
Explanation Service
        ↓
Citizen-Friendly Response
```

Phase 2 uses deterministic structured logic and no external AI service. It turns synthetic application statuses into clear explanations and actionable next steps.

## Phase 3 Mock Grievance Flow

```text
Citizen
        ↓
Grievance Draft Endpoint
        ↓
Grievance Service
        ↓
Synthetic JSON Storage
        ↓
Synthetic Reference Number
```

Grievance submission is fully simulated. No grievance is sent to EPFO, any government agency, or any external service.

## Phase 4 Frontend Journey

```text
Welcome
  ↓
Claim Overview
  ↓
Claim Explanation
  ↓
Grievance Draft
  ↓
Simulated Submission Success
```

The React frontend communicates with the FastAPI backend through a dedicated API layer. The interface includes loading states, error handling, retry behavior, mobile-responsive styling, and clear notices that all data and submissions are synthetic.

The complete citizen journey can be completed from start to finish without accessing a live government system.
