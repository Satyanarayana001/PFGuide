# PFGuide

PFGuide is a prototype that helps citizens understand confusing PF claim statuses and take the right next step.

> **Demo prototype:** All claim information shown in PFGuide is synthetic. PFGuide is not an official government service and does not connect to EPFO.

## Live Demo

- **Frontend:** https://pf-guide-43dtgn8qw.vercel.app
- **Backend API:** https://pfguide-api.onrender.com/docs
- **GitHub Repository:** https://github.com/Satyanarayana001/PFGuide

## The Problem

Indian public-service portals often provide users with a claim status, but the status alone may not clearly explain what happened or what the citizen should do next.

For example, a citizen may see a status such as:

- **Verification Review**
- **Employer verification incomplete**

These messages can leave the citizen with several unanswered questions:

- What happened to my claim?
- Why does the claim need attention?
- What action should I take next?
- Where can I get help if the issue remains unresolved?

The challenge is not only accessing the status. The challenge is understanding it and knowing the next step.

## The Solution

PFGuide redesigns this part of the citizen journey around three simple questions:

1. **What happened?**
2. **Why did it happen?**
3. **What can I do now?**

Instead of leaving the citizen with a technical or unclear status, PFGuide converts synthetic claim information into a simple explanation and actionable next steps.

If the citizen still needs help, the prototype prepares an editable simulated grievance draft. After simulated submission, the user receives a synthetic reference number.

## Citizen Journey

```text
Start Demo
    ↓
View Claim Status
    ↓
Understand the Claim
    ↓
See What Happened
    ↓
Understand Why
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

## What Works Today

The complete prototype journey works end-to-end:

- Demo login using synthetic user data
- Claim/application lookup
- Claim status overview
- Plain-language explanation
- Actionable next steps
- Editable simulated grievance draft
- Simulated grievance submission
- Synthetic grievance reference number
- Deployed frontend and backend

The frontend communicates with the backend through deployed API endpoints.

## What Is Mocked

The following are intentionally simulated:

- User accounts
- PF claim information
- Claim statuses
- Verification details
- Grievance drafts
- Grievance submissions
- Reference numbers

No request is sent to EPFO or any government system.

## Design Considerations

PFGuide is designed around a simple citizen journey with:

- Clear, plain-language explanations
- One primary action at each stage
- Mobile-friendly responsive layout
- Lightweight React frontend
- Clear loading and error states
- Synthetic data instead of sensitive personal information
- No requirement for real Aadhaar, PAN, OTP, password, payment, or PF account information

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

## Architecture

```text
Citizen
   ↓
React + Vite Frontend
   ↓
FastAPI Backend
   ↓
Application / Explanation / Grievance Services
   ↓
Synthetic JSON Data
```

For more details, see:

- `docs/architecture.md`

## Run Locally

### Backend

```powershell
cd backend
.\venv\Scripts\python.exe -m uvicorn main:app --reload
```

The backend runs at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### Frontend

```powershell
cd frontend
npm install
npm run dev
```

Create a `.env` file inside the `frontend` directory:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Testing

### Backend

Run:

```powershell
cd backend
pytest
```

Verified result:

```text
11 passed
```

### Frontend

Build the production frontend:

```powershell
cd frontend
npm run build
```

The production build completed successfully.

## Safety and Mock Data

All claim information, users, grievance submissions, and reference numbers are synthetic.

PFGuide:

- Does not connect to EPFO
- Does not connect to any live government system
- Is not an official government service
- Does not use real Aadhaar numbers
- Does not use real PAN information
- Does not collect passwords or OTPs
- Does not process payments
- Does not access real PF account data

Synthetic data is used deliberately because production access to government systems and personal citizen information would be unsafe and unavailable for a hackathon prototype.

## Future Direction

A production version would require:

- Secure authentication
- Explicit citizen consent
- Authorized government API integrations
- Strong privacy and data-protection controls
- Audit logging
- Rate limiting and monitoring
- Secure grievance-routing workflows
- Human review where automated guidance is uncertain

The current prototype focuses on proving a simpler and clearer citizen experience without accessing real government data.

## Codex Usage

Codex was used as a meaningful part of the development workflow to help build and refine the prototype across the frontend, backend, testing, debugging, documentation, and deployment workflow.

Detailed information is available in:

- `docs/codex-usage.md`

## Documentation

Additional project documentation:

- `docs/architecture.md`
- `docs/codex-usage.md`
- `docs/demo-script.md`
- `docs/product-spec.md`
- `docs/submission-summary.md`
