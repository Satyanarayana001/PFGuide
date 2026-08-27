# How Codex Was Used to Build PFGuide

## Overview

PFGuide was built through an iterative development workflow in which Codex was used as a meaningful development assistant throughout the project.

Codex contributed to planning, implementation, debugging, testing, documentation, and refinement of both the backend and frontend.

It was part of the actual development process rather than being added only for the hackathon submission.

## 1. Project Planning and Architecture

Codex assisted in breaking the prototype into a clear application structure.

This included planning:

- FastAPI backend routes
- Request and response models
- Service-layer responsibilities
- Synthetic JSON data handling
- Frontend application structure
- React component separation
- Error and loading states
- Test organization
- Documentation structure

The resulting project was organized into separate backend, frontend, test, mock-data, and documentation areas.

## 2. Backend Development

Codex was used while implementing and refining the FastAPI backend.

This included assistance with:

- Demo authentication using synthetic data
- Claim and application lookup
- Claim status responses
- Plain-language explanation logic
- Actionable next-step responses
- Grievance draft generation
- Simulated grievance submission
- Synthetic reference number generation
- Pydantic request and response schemas
- Error handling
- Mock JSON data access

During development, unused functionality was also reviewed and removed where it was not necessary for the citizen journey.

The backend intentionally avoids live EPFO or government integrations.

## 3. Frontend Development

Codex assisted in building the React and Vite frontend that supports the complete citizen journey.

This included:

- Welcome screen
- Demo entry flow
- Claim overview
- Plain-language claim explanation
- Actionable next steps
- Editable grievance draft
- Simulated grievance submission
- Success screen with synthetic reference number
- Loading states
- Error states
- Retry behavior
- API integration
- Mobile-responsive styling

The frontend was designed so that the citizen moves through one clear primary action at each stage.

## 4. Debugging and Deployment

Codex was used during debugging and deployment-related work.

This included reviewing:

- API connectivity between frontend and backend
- Environment variable configuration
- CORS configuration for the deployed frontend
- Route and import issues
- Git changes and project structure
- Production build behavior

The backend and frontend were then deployed separately and tested as a connected application.

## 5. Testing and Verification

Codex assisted with reviewing the implementation and identifying areas that required verification.

Backend regression tests were executed using:

```powershell
pytest
```

Verified result:

```text
11 passed
```

The frontend production build was also verified using:

```powershell
npm run build
```

The production build completed successfully.

The deployed citizen journey was then tested from start to finish:

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
Prepare Grievance Draft
    ↓
Edit Draft
    ↓
Simulated Submission
    ↓
Synthetic Reference Number
```

## 6. Iterative Improvement

The project was developed through repeated implementation, testing, review, and refinement.

Examples of iterative improvements included:

- Simplifying the citizen journey
- Improving claim explanations
- Adding actionable next steps
- Adding loading and error states
- Making synthetic behavior clear
- Removing unnecessary functionality
- Improving frontend usability
- Testing API connectivity
- Resolving deployment issues
- Verifying the production frontend build
- Testing the complete deployed journey

## Human Decisions

Codex assisted with development, but the core product decisions were intentionally made around the hackathon problem.

Key decisions included:

- Focusing on PF claim-status confusion as the citizen problem
- Designing the experience around three simple questions:
  1. What happened?
  2. Why did it happen?
  3. What can I do now?
- Prioritizing a complete citizen journey instead of an admin interface
- Using synthetic data instead of sensitive personal information
- Avoiding live EPFO or government integrations
- Clearly disclosing simulated behavior
- Keeping the interface simple and mobile-friendly

## Conclusion

Codex was used as a meaningful part of the actual PFGuide development workflow across planning, architecture, backend implementation, frontend development, debugging, testing, deployment, and iterative refinement.

The final prototype represents an iterative human-and-Codex development process. Codex was not added as a superficial feature for submission purposes; it was used throughout the process of building and improving the working prototype.
