# How Codex Was Used to Build PFGuide

## Overview

PFGuide was built through an iterative development workflow using Codex as a meaningful development tool.

Codex was used throughout the project to help design, implement, test, review, and improve the prototype.

It was not added only for documentation or submission purposes.

## Areas Where Codex Was Used

### 1. Project Architecture

Codex assisted with planning the application structure, including:

- Backend organization
- API routes
- Data models
- Service layer
- Mock data handling
- Frontend structure
- Component separation

The project was organized into separate backend, frontend, documentation, and test areas.

### 2. Backend Development

Codex assisted with implementing and reviewing the FastAPI backend.

This included work around:

- Claim data retrieval
- Claim explanation responses
- Grievance draft generation
- Simulated grievance submission
- Request and response schemas
- Synthetic mock data
- Error handling

The prototype intentionally avoids live government systems and uses synthetic data.

### 3. Frontend Development

Codex was used to help build the React and Vite frontend.

The frontend includes:

- Welcome screen
- Claim overview
- Plain-language claim explanation
- Actionable next steps
- Editable grievance draft
- Simulated submission success screen
- Loading states
- Error states
- Retry behavior
- Mobile-responsive styling

### 4. Testing and Verification

Codex assisted with reviewing the end-to-end citizen journey and identifying implementation issues.

Backend regression testing was run using pytest.

The backend test suite passed:

11 passed

The React frontend was also built successfully using:

npm run build

The production build completed successfully.

### 5. Iterative Improvement

The development process involved repeated review and refinement.

Examples include:

- Improving the citizen journey
- Clarifying synthetic-data disclosures
- Reviewing whether unused routes were necessary
- Improving frontend usability
- Verifying API behavior
- Testing the grievance flow
- Checking production frontend builds

## Human Decisions

Codex assisted with implementation, but product decisions remained intentional.

Key decisions included:

- Focusing on PF claim-status confusion as the problem
- Designing the experience around simple questions
- Using mock data instead of sensitive information
- Avoiding live government integrations
- Making simulated behavior clearly visible
- Prioritizing the complete citizen journey over an admin interface

## Conclusion

Codex was used as part of the actual development workflow for planning, implementation, debugging, testing, and refinement of PFGuide.

The final prototype represents an iterative human-and-Codex development process rather than an existing project with a minimal AI-related addition.