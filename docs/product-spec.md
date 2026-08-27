# PFGuide — Product Specification

## 1. Problem

Understanding the status of a Provident Fund (PF) claim can be difficult for citizens using digital public services.

A claim status may contain terms such as:

- Verification Review
- Employer verification incomplete
- Processing
- Action Required

The citizen may be able to see the status but still not understand:

- What the current status means
- Why the claim needs attention or is delayed
- What action should be taken next
- Where to seek help if the issue remains unresolved

The problem is therefore not only access to claim information. The problem is turning a status into something understandable and actionable.

This can create confusion, repeated searching, and unnecessary effort while navigating a public-service journey.

## 2. Target User

PFGuide is designed for Indian citizens who have submitted a PF-related claim and find the status or next steps difficult to understand.

The prototype particularly considers citizens who:

- Have limited experience with digital government services
- Primarily use mobile devices
- Prefer simple and direct language
- May use slower or unreliable internet connections
- Need clear guidance instead of unexplained technical status messages

## 3. Product Goal

The goal of PFGuide is to demonstrate a simpler citizen experience for understanding a claim and deciding what to do next.

The experience is organized around three questions:

1. **What happened?**
2. **Why did it happen?**
3. **What can I do now?**

If the citizen still needs assistance, PFGuide continues the journey by preparing an editable simulated grievance draft.

The goal is not to replace an official government portal. The prototype demonstrates how a confusing part of a public-service journey could be redesigned to be clearer and easier to use.

## 4. Complete Citizen Journey

The main journey is:

1. Open PFGuide.
2. Start the demo using synthetic data.
3. View the current claim status.
4. See the important claim information.
5. Choose to understand the claim.
6. Read a plain-language explanation of what happened.
7. Understand why the claim needs attention.
8. Review actionable next steps.
9. Prepare a simulated grievance draft if additional help is needed.
10. Review and edit the grievance draft.
11. Submit the grievance within the prototype.
12. Receive a synthetic reference number.
13. Restart the journey if required.

The main citizen journey is designed to work from start to finish rather than stopping at a static interface or isolated screen.

## 5. Core User Experience

PFGuide reduces complexity by giving the citizen one clear next step at each stage.

Instead of presenting only a technical status, the experience provides:

- A clear claim overview
- Plain-language explanations
- A distinction between what happened and why it happened
- Actionable next steps
- An editable grievance draft instead of a blank starting point
- Clear feedback after simulated submission
- A synthetic reference number

This creates a progression from **status → understanding → action → further help**.

## 6. Usability and Accessibility Considerations

The prototype is designed with real-world digital constraints in mind.

Key considerations include:

- Mobile-responsive layout
- Simple and direct language
- Clear visual hierarchy
- One primary action at each stage
- Lightweight frontend implementation
- Loading states for asynchronous requests
- Error states when requests fail
- Retry behavior
- Clear disclosure of simulated behavior

The design aims to reduce cognitive load for citizens with different levels of digital experience.

## 7. What Works Today

The working prototype includes:

- React and Vite frontend
- FastAPI backend
- Synthetic demo authentication
- Synthetic claim and application data
- Claim status retrieval
- Plain-language claim explanations
- Actionable next-step guidance
- Simulated grievance draft generation
- Editable grievance submission
- Synthetic grievance reference numbers
- Loading states
- Error handling
- Retry behavior
- Mobile-responsive interface
- Connected frontend and backend deployment

The complete primary journey can be tested end-to-end.

## 8. Product and System Design

The application separates the citizen-facing interface from the backend logic.

```text
Citizen
   ↓
React + Vite Frontend
   ↓
FastAPI API Routes
   ↓
Application / Explanation / Grievance Logic
   ↓
Synthetic JSON Data
```

The frontend communicates with the backend through API endpoints.

This structure makes it possible to demonstrate the complete product journey while keeping sensitive or unavailable integrations safely mocked.

## 9. What Is Mocked

The following are intentionally simulated:

- User identity
- PF claim information
- Claim statuses
- Claim processing
- Employer verification details
- Grievance draft generation
- Grievance submission
- Reference numbers
- Government-system interactions

PFGuide does not connect to EPFO or any live government system.

No real Aadhaar numbers, PAN information, passwords, OTPs, payment information, or PF account data are used.

All synthetic behavior is intentionally disclosed to the user.

## 10. Safety and Privacy

The prototype avoids collecting or processing sensitive citizen information.

Synthetic data is used because a production public-service integration would require appropriate authorization, security controls, and privacy protections.

A production implementation should include:

- Official authorization and approved API access
- Secure authentication
- Explicit citizen consent
- Data minimization
- Encryption in transit and at rest
- Role-based access controls
- Audit logging
- Rate limiting
- Monitoring and incident response
- Secure error handling
- Privacy and data-protection compliance

## 11. Future Scalability

A future production version could integrate with authorized systems while keeping the same citizen-centered explanation flow.

Possible future improvements include:

- Authorized government API integrations
- Real claim retrieval with citizen consent
- Secure grievance-routing workflows
- Multiple Indian language support
- Accessibility testing and improvements
- Human support escalation for uncertain cases
- Monitoring and service reliability controls

The current prototype intentionally focuses on validating the product experience without requiring access to real government systems or sensitive personal data.

## 12. Success Criteria

PFGuide succeeds as a prototype if a citizen can:

1. Understand the current claim status.
2. Understand why attention may be required.
3. Identify a clear next action.
4. Continue to a grievance flow when additional help is needed.
5. Complete the simulated journey from start to finish.
6. Clearly understand which data and actions are synthetic.

The prototype is designed to demonstrate that public-service status information can be transformed into a clearer, more understandable, and more actionable citizen journey.
