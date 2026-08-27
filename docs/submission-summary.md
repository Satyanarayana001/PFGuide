# PFGuide — Submission Summary

## The Problem

PFGuide addresses a usability problem faced by citizens using digital public services: a claim status may be visible, but its meaning and the next action are often unclear.

A citizen may see a status such as:

- **Verification Review**
- **Employer verification incomplete**

Without additional explanation, the citizen may not know:

- What happened to the claim
- Why the claim needs attention
- What action should be taken next
- How to seek help if the issue remains unresolved

The problem is therefore not only checking a status. It is understanding the status and completing the next step with confidence.

## The Solution

PFGuide redesigns this part of the citizen journey around three simple questions:

1. **What happened?**
2. **Why did it happen?**
3. **What can I do now?**

The prototype presents a synthetic PF claim, explains the status in plain language, and provides actionable next steps.

If the citizen still needs assistance, PFGuide continues the journey by preparing an editable simulated grievance draft. The citizen can review and edit the draft, submit it within the prototype, and receive a synthetic reference number.

## Complete Citizen Journey

```text
Start Demo
    ↓
View Claim Status
    ↓
Understand What Happened
    ↓
Understand Why It Happened
    ↓
Get Actionable Next Steps
    ↓
Prepare a Grievance Draft
    ↓
Review and Edit
    ↓
Simulated Submission
    ↓
Receive Synthetic Reference Number
```

The main citizen journey works from start to finish and can be tested through the deployed application.

## Why PFGuide Is Easier

PFGuide focuses on reducing confusion rather than simply displaying more information.

Key product choices include:

- Plain-language explanations instead of unexplained status labels
- Clear separation between what happened, why it happened, and what to do next
- One primary action at each stage of the journey
- An editable grievance draft instead of asking the citizen to start from a blank form
- Clear disclosure when an action is simulated
- Responsive design for mobile users
- Loading states, error states, and retry behavior

The goal is to make the next step understandable for citizens with different levels of digital experience.

## What Works Today

The working prototype includes:

- Synthetic demo login
- Claim and application lookup
- Claim status overview
- Plain-language claim explanation
- Actionable next steps
- Editable grievance draft
- Simulated grievance submission
- Synthetic grievance reference number
- Connected frontend and backend deployment

The backend test suite was verified with:

```text
11 passed
```

The frontend production build was also completed successfully.

## Technology and End-to-End Design

PFGuide uses:

- **Frontend:** React, Vite, JavaScript, CSS
- **Backend:** Python, FastAPI, Pydantic
- **Data:** Synthetic JSON data

The deployed frontend communicates with the deployed backend through API endpoints.

The prototype therefore demonstrates both the citizen-facing interface and the supporting backend flow rather than only a static design or admin interface.

## Codex Usage

Codex was a meaningful part of the development workflow.

It was used throughout planning, architecture, backend development, frontend implementation, debugging, testing, documentation, deployment, and iterative refinement.

The project was developed through an iterative human-and-Codex workflow rather than adding Codex only for submission purposes.

Detailed documentation is available in:

```text
docs/codex-usage.md
```

## Mock Data and Limitations

All user accounts, claim information, statuses, grievance submissions, and reference numbers are synthetic.

PFGuide:

- Does not connect to EPFO
- Does not connect to any live government system
- Is not an official government service
- Does not use real Aadhaar, PAN, OTP, passwords, payment information, or PF account data

These limitations are intentional and clearly disclosed because real government integrations and citizen data would require authorization, security controls, consent, and production-grade infrastructure.

## How It Could Scale Safely

A production implementation would require:

- Authorized government API integrations
- Secure authentication
- Explicit citizen consent
- Privacy and data-protection controls
- Encryption and secure data handling
- Audit logging
- Rate limiting and monitoring
- Secure grievance-routing workflows
- Human review where automated guidance is uncertain

The current prototype focuses on demonstrating a simpler citizen experience without accessing real government systems or sensitive personal information.

## Summary

PFGuide demonstrates how a confusing public-service claim status can be transformed into a clearer end-to-end citizen journey.

Instead of stopping at a status label, the prototype helps the citizen understand what happened, why it happened, what to do next, and how to prepare a request for further help when needed.

The complete journey works using synthetic data, while all mocked behavior and production limitations are clearly disclosed.
