# PFGuide — Product Specification

## 1. Problem

Understanding the status of a Provident Fund (PF) claim can be difficult for many citizens.

A claim status may contain terms such as:

- Verification Review
- Employer verification incomplete
- Processing
- Action Required

Users may not clearly understand:

- What the current status means
- Why the claim is delayed
- What action they should take next
- How to ask for help when the issue is not resolved

This creates confusion and unnecessary effort while navigating public-service portals.

## 2. Target User

PFGuide is designed for Indian citizens who have submitted a PF-related claim and find the status or next steps difficult to understand.

The prototype particularly considers users who:

- Have limited experience with digital government services
- Use mobile devices
- Prefer simple and direct language
- May be using slower internet connections
- Need clear guidance instead of technical status messages

## 3. Solution

PFGuide provides a simplified citizen journey that helps a user understand a synthetic PF claim.

The prototype converts a claim status into three simple questions:

1. What happened?
2. Why did it happen?
3. What can I do now?

If the user still needs help, PFGuide prepares an editable simulated grievance draft based on the claim information.

## 4. Complete Citizen Journey

The main journey is:

1. Open PFGuide.
2. Start the demo using synthetic data.
3. View the current claim status.
4. See important claim information.
5. Request a simple explanation.
6. Understand what happened and why.
7. Review actionable next steps.
8. Prepare a simulated grievance draft.
9. Edit the grievance if required.
10. Submit the simulated grievance.
11. Receive a synthetic reference number.

The journey can then be restarted.

## 5. What Makes It Better

PFGuide focuses on reducing confusion.

Instead of presenting only a technical status, it provides:

- Plain-language explanations
- Clear next actions
- A step-by-step journey
- An editable grievance draft
- Mobile-friendly design
- Loading, error, and retry states
- Clear synthetic-data disclosures

The goal is not to replace an official government portal. The goal is to demonstrate how the citizen experience could be made easier to understand.

## 6. What Works Today

The prototype includes:

- React and Vite frontend
- FastAPI backend
- Synthetic claim data
- Claim status retrieval
- Plain-language claim explanations
- Suggested next actions
- Simulated grievance draft generation
- Editable grievance submission
- Synthetic grievance reference numbers
- Loading and error handling
- Mobile-first responsive interface

## 7. What Is Mocked

The following are intentionally simulated:

- User identity
- PF claim information
- Claim processing
- Employer verification
- Grievance submission
- Reference numbers
- Government-system interactions

PFGuide does not connect to EPFO or any live government system.

No Aadhaar numbers, PAN details, passwords, OTPs, payment information, or other sensitive personal data are used.

## 8. Safety and Scale

A real implementation could use secure and officially authorized integrations where available.

Important requirements for a production system would include:

- Official authorization and APIs
- Secure authentication
- Data minimization
- Encryption
- Consent-based access
- Audit logging
- Rate limiting
- Clear error handling
- Accessibility testing
- Support for multiple Indian languages

The current project is a prototype designed to demonstrate the citizen experience safely using synthetic data.