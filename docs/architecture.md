# PFGuide Phase 1 Architecture

```text
Future React Frontend
        ↓
FastAPI Routes
        ↓
Service Layer
        ↓
Synthetic JSON Data
```

The FastAPI application exposes health, synthetic demo-login, and synthetic
application-lookup endpoints. Routes handle HTTP concerns, while services load
the JSON mock data.

No live EPFO or government system is accessed. All user and application data in
this prototype is synthetic.

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

Phase 2 uses deterministic structured logic and no external AI service. It
turns synthetic application statuses into clear explanations and actionable
next steps.

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

Grievance submission is fully simulated. No grievance is sent to EPFO, any
government agency, or any external service.
