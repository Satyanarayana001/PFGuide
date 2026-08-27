# PFGuide

PFGuide is a prototype that helps citizens understand confusing PF claim statuses and take the right next step.

## The Problem

A citizen may see a status such as **Verification Review** or **Employer verification incomplete** without clearly understanding:

- What happened to the claim
- Why the claim needs attention
- What action should be taken next
- How to ask for help if the issue remains unresolved

## The Solution

PFGuide simplifies the journey around three questions:

1. What happened?
2. Why did it happen?
3. What can I do now?

If the citizen still needs help, the prototype prepares an editable simulated grievance draft and provides a synthetic reference number after simulated submission.

## Citizen Journey

```text
Start Demo
    ↓
View Claim Status
    ↓
Understand the Claim
    ↓
See Why It Happened
    ↓
Get Actionable Next Steps
    ↓
Prepare a Grievance Draft
    ↓
Review and Edit
    ↓
Simulated Submission
    ↓
Synthetic Reference Number
```

## Tech Stack

### Frontend
- React
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- Pydantic
- Synthetic JSON data

## Run Locally

### Backend

```powershell
cd backend
.\venv\Scripts\python.exe -m uvicorn main:app --reload
```

### Frontend

```powershell
cd frontend
npm install
npm run dev
```

The frontend API base URL is configured through:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Testing

Run backend tests:

```powershell
cd backend
pytest
```

Verified result:

```text
11 passed
```

Build the frontend:

```powershell
cd frontend
npm run build
```

## Safety and Mock Data

All claim information, users, grievance submissions, and reference numbers are synthetic.

PFGuide does not connect to EPFO or any live government system and is not an official government service. It does not use real Aadhaar numbers, PAN information, passwords, OTPs, payment information, or real PF account data.

## Documentation

- `docs/architecture.md`
- `docs/codex-usage.md`
- `docs/demo-script.md`
- `docs/product-spec.md`
- `docs/submission-summary.md`
