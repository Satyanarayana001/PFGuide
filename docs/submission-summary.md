# PFGuide — Submission Summary

PFGuide is a prototype that helps Indian citizens understand confusing PF claim statuses and take the right next step.

A common problem with public-service portals is that users may see a status such as "Verification Review" or "Employer verification incomplete" without understanding what happened, why their claim needs attention, or what they should do next.

PFGuide redesigns this experience around three simple questions:

1. What happened?
2. Why did it happen?
3. What can I do now?

The citizen journey starts with a synthetic PF claim and clearly presents the current status and important claim details. The user can then get a plain-language explanation and a list of actionable next steps. If additional help is needed, PFGuide prepares an editable simulated grievance draft. The user can review the draft, submit it within the prototype, and receive a synthetic reference number.

The prototype is built with a React and Vite frontend and a FastAPI backend. Codex was used meaningfully throughout the development process for planning, implementation, debugging, testing, and iterative refinement.

PFGuide is designed with mobile users and varying levels of digital experience in mind. It includes responsive design, loading states, error handling, and retry behavior.

All data and government interactions are synthetic. PFGuide is not an official government service and does not connect to EPFO or any live government system.

The goal is to demonstrate how a confusing claim status can become a clearer, more understandable citizen journey.