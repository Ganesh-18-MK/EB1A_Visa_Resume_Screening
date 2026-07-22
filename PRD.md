# 📋 Product Requirements Document (PRD)

# EB1A Resume Screener

**Project Name:** EB1A Resume Screener

**Project Owner:** Steve

**Prepared By:** Development Team

**Version:** 1.0

**Status:** Draft

**Target Completion:** 3 Weeks (MVP)

---

# 1. Project Overview

## Purpose

The EB1A Resume Screener is an AI-powered web application designed to automate the initial screening process for Employment-Based First Preference (EB1A) visa applicants.

The platform enables candidates to upload their resume, complete an eligibility questionnaire, and submit their application for evaluation.

The system analyzes the submitted information using OCR, Resume Parsing, a Knowledge Base, and Claude AI to generate an eligibility recommendation. The evaluation results are presented through an Admin Dashboard for immigration specialists to review.

The objective is to reduce manual effort, improve consistency, and streamline the client qualification process.

---

# 2. Business Problem

The current screening process is manual and requires immigration specialists to review every resume individually.

This approach creates several challenges:

- Time-consuming resume reviews
- Inconsistent evaluations
- Delayed response to applicants
- No centralized application management
- Difficult to scale as application volume increases

The organization requires an automated screening solution that assists specialists while maintaining final human review.

---

# 3. Project Objectives

The project aims to:

- Automate initial resume screening.
- Reduce manual review effort.
- Standardize eligibility evaluation.
- Improve lead qualification.
- Centralize applicant information.
- Provide AI-assisted recommendations.
- Enable administrators to monitor all applications from one dashboard.

---

# 4. Proposed Solution

Develop a web-based application where candidates can:

- Upload their resume
- Complete an eligibility questionnaire
- Submit their application

The system will:

- Extract resume content
- Parse resume information
- Analyze questionnaire responses
- Evaluate eligibility using a Knowledge Base
- Generate AI recommendations using Claude AI
- Store application data in PostgreSQL
- Display results in an Admin Dashboard

The platform is intended to assist immigration specialists and not replace legal decision-making.

---

# 5. Project Scope

## In Scope

### Candidate Portal

- Resume Upload
- Eligibility Questionnaire
- Application Submission

### Resume Processing

- OCR
- Resume Parsing
- Structured JSON Generation

### AI Evaluation

- Knowledge Base Evaluation
- Claude AI Integration
- Eligibility Recommendation
- Missing Criteria Identification

### Admin Dashboard

- Candidate List
- Resume Viewer
- Questionnaire Viewer
- AI Recommendation Viewer
- Search & Filters
- Status Management

### Database

- Candidate Information
- Resume Data
- Questionnaire Responses
- AI Evaluation Results
- Application Status

---

## Out of Scope (MVP)

The following features are excluded from the MVP and may be considered in future releases.

- User Authentication
- Email Notifications
- SMS Notifications
- Candidate Login
- Mobile Application
- Bulk Resume Upload
- Analytics Dashboard
- Multi-language Resume Support
- Audit Logs

---

# 6. User Roles

## Candidate

Responsibilities

- Upload Resume
- Complete Questionnaire
- Submit Application

---

## Administrator

Responsibilities

- View Submitted Applications
- Review Resume
- Review Questionnaire
- View AI Evaluation
- Update Candidate Status

---

## Immigration Specialist

Responsibilities

- Review AI Recommendation
- Validate Candidate Eligibility
- Make Final Decision

---

# 7. Functional Requirements

### Candidate Portal

- Upload resumes (PDF initially)
- Complete eligibility questionnaire
- Submit application

---

### Resume Processing

- Extract text using OCR
- Parse resume information
- Identify education, work experience, publications, awards, patents, certifications, and skills
- Generate structured candidate profile

---

### Knowledge Base

The system shall compare candidate information against predefined EB1A eligibility criteria.

The Knowledge Base will be configurable and expandable without requiring application code changes.

---

### AI Evaluation

The system shall:

- Analyze resume content
- Analyze questionnaire responses
- Match candidate profile against the Knowledge Base
- Generate eligibility recommendation
- Provide explanation for recommendation
- Identify missing evidence

---

### Admin Dashboard

The administrator shall be able to:

- View all submitted applications
- Search candidates
- Filter applications
- Open resume
- View questionnaire responses
- Review AI recommendation
- Update application status

---

# 8. Non-Functional Requirements

### Performance

- Resume upload should complete within acceptable response time.
- AI evaluation should process efficiently for MVP-scale usage.

### Security

- Secure storage of candidate data
- API key protection
- Secure database access

### Scalability

The architecture should support future expansion without major redesign.

### Maintainability

The application should follow a modular architecture for easier maintenance and feature additions.

---

# 9. User Workflow

```text
Candidate

↓

Upload Resume

↓

Answer Questionnaire

↓

Submit Application

↓

OCR Processing

↓

Resume Parsing

↓

Knowledge Base Evaluation

↓

Claude AI Analysis

↓

Eligibility Recommendation

↓

Store Results

↓

Admin Dashboard Review
```

---

# 10. Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Programming Language | Python |
| OCR | Tesseract OCR |
| PDF Processing | PyMuPDF |
| Resume Parsing | spaCy |
| AI | Claude API |
| Database | PostgreSQL |
| Version Control | GitHub |
| Project Tracking | Jira |

---

# 11. Deliverables

The MVP will include:

- Candidate Portal
- Resume Upload Module
- Eligibility Questionnaire
- OCR Engine
- Resume Parser
- Knowledge Base
- Claude AI Integration
- PostgreSQL Database
- Admin Dashboard
- REST API
- Project Documentation

---

# 12. Project Timeline

| Week | Deliverables |
|------|--------------|
| Week 1 | Project Setup, Candidate Portal, Resume Upload, Questionnaire, Database |
| Week 2 | OCR, Resume Parsing, Knowledge Base, Claude AI Integration |
| Week 3 | Admin Dashboard, Testing, Bug Fixes, Deployment |

---

# 13. Success Criteria

The project will be considered successful if:

- Candidates can successfully submit resumes.
- Questionnaire responses are stored correctly.
- Resume information is extracted accurately.
- AI generates eligibility recommendations.
- Administrators can review all applications through the dashboard.
- Manual screening effort is reduced.

---

# 14. Assumptions & Constraints

## Assumptions

- Applicants will upload readable PDF resumes.
- Claude AI API will be available during evaluation.
- Knowledge Base content will be maintained by the business team.

## Constraints

- Initial release targets approximately 50 applicants per month.
- AI recommendations assist reviewers but do not replace legal judgment.
- MVP delivery timeline is three weeks.

---

# 15. Conclusion

The EB1A Resume Screener will streamline the initial eligibility assessment process by combining OCR, resume parsing, a configurable Knowledge Base, and Claude AI into a single platform.

The solution will improve operational efficiency, standardize candidate evaluations, and provide administrators with a centralized interface for managing applicant submissions.

The modular architecture also allows the platform to be expanded with additional features in future releases.

---

# Appendix A

## Infrastructure Recommendation & Budget Comparison

Please refer to the attached document:

**CCIP_Overview.pdf**

This document contains:

- Infrastructure Recommendation
- Google Cloud Run vs Google Compute Engine comparison
- Budget Comparison
- Implementation Support
- Cost Estimation
- Deployment Recommendation

This document is considered part of this PRD.
