# 🏛️ System Architecture

# EB1A Resume Screener

**Version:** 1.0

**Document Type:** Technical Architecture

**Project:** EB1A Resume Screener

---

# 1. Overview

The EB1A Resume Screener is an AI-powered web application that automates the initial eligibility assessment of EB1A visa applicants.

The application consists of two primary interfaces:

- Candidate Portal
- Admin Dashboard

The backend processes resumes using OCR and Resume Parsing, combines the extracted information with questionnaire responses, evaluates eligibility using a Knowledge Base and Claude AI, and stores the results in PostgreSQL.

---

# 2. High-Level Architecture

```
                        Candidate
                           │
                           ▼
                Upload Resume & Questionnaire
                           │
                           ▼
                  Streamlit Frontend
                           │
                           ▼
                     FastAPI Backend
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   OCR Engine        Resume Parser     Questionnaire
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                Candidate Profile Builder
                           ▼
                  Knowledge Base Engine
                           ▼
                    Claude AI Analysis
                           ▼
                     PostgreSQL Database
                           ▼
                    Admin Dashboard
```

---

# 3. System Components

## Candidate Portal

The Candidate Portal allows applicants to:

- Upload resumes
- Complete the eligibility questionnaire
- Submit applications

Technology:

- Streamlit

---

## FastAPI Backend

Responsible for:

- API Management
- Business Logic
- File Upload
- AI Integration
- Database Communication

Technology:

- FastAPI

---

## OCR Engine

Responsibilities:

- Read scanned resumes
- Extract text from images
- Support PDF OCR when required

Technology:

- Tesseract OCR
- PyMuPDF
- Pillow

---

## Resume Parser

Responsibilities:

- Parse extracted resume text
- Identify candidate information
- Generate structured JSON

Extracted Information:

- Name
- Email
- Phone
- Education
- Experience
- Publications
- Awards
- Patents
- Certifications
- Skills

Technology:

- spaCy
- Regular Expressions

---

## Questionnaire Engine

Stores responses from the eligibility questionnaire.

Future Version:

- Dynamic questionnaires
- Conditional questions

---

## Knowledge Base

The Knowledge Base contains the EB1A eligibility criteria used during evaluation.

Examples:

- Awards
- Publications
- Memberships
- Original Contributions
- Judging Experience
- Media Coverage
- Leadership Roles

The Knowledge Base should be configurable without requiring code changes.

---

## Claude AI

Claude AI receives:

- Parsed Resume JSON
- Questionnaire Responses
- Knowledge Base

Claude returns:

- Eligibility Recommendation
- Eligibility Score
- Missing Criteria
- Explanation

---

## PostgreSQL Database

Stores:

- Candidate Details
- Resume Information
- Questionnaire Responses
- AI Results
- Status

---

## Admin Dashboard

The Admin Dashboard enables administrators to:

- View candidates
- Review resumes
- View questionnaire responses
- Review AI recommendations
- Update application status
- Search and filter records

Technology:

- Streamlit

---

# 4. Data Flow

```
Candidate

↓

Upload Resume

↓

Resume Stored

↓

OCR

↓

Extracted Text

↓

Resume Parser

↓

Candidate JSON

↓

Questionnaire Responses

↓

Knowledge Base

↓

Claude AI

↓

Eligibility Result

↓

PostgreSQL

↓

Admin Dashboard
```

---

# 5. Folder Structure

```
EB1A_Resume_Screener/

backend/
│
├── api/
├── ai/
├── database/
├── knowledge_base/
├── models/
├── ocr/
├── parser/
├── services/
├── uploads/
├── extracted/
├── utils/
├── logs/
└── main.py

frontend/
│
├── Home.py
├── candidate/
├── admin/
└── components/

docs/

tests/
```

---

# 6. Database Flow

```
Resume

↓

OCR

↓

Resume Parser

↓

Candidate JSON

↓

PostgreSQL
```

Questionnaire

↓

PostgreSQL

↓

Claude AI

↓

Evaluation Results

↓

PostgreSQL

---

# 7. AI Evaluation Flow

```
Resume

↓

OCR

↓

Resume Parser

↓

Structured JSON

↓

Knowledge Base

↓

Claude AI

↓

Eligibility Report

↓

Database
```

---

# 8. Knowledge Base Design

The Knowledge Base contains structured EB1A evaluation criteria.

Example Categories:

- National or International Awards
- Publications
- Research Papers
- Citations
- Patents
- Memberships
- Judging Experience
- Media Recognition
- Leadership Roles
- High Salary
- Original Contributions

Future versions may store this information in a database or configuration file to allow updates without modifying application code.

---

# 9. Security

The MVP will include:

- Input Validation
- File Type Validation
- Environment Variables
- Secure API Keys
- Database Access Control

Future Enhancements:

- JWT Authentication
- HTTPS
- Role-Based Access Control (RBAC)
- Audit Logging

---

# 10. Logging

Application logs will capture:

- Resume Upload
- Questionnaire Submission
- OCR Processing
- Resume Parsing
- AI Evaluation
- Database Operations
- Application Errors

Logs will assist in troubleshooting and monitoring system health.

---

# 11. Scalability

The architecture is designed to support future enhancements such as:

- Multiple reviewers
- Bulk resume processing
- Email notifications
- Cloud storage
- Multi-language resumes
- Analytics dashboard
- Authentication and authorization

---

# 12. Deployment Architecture

```
Candidate

↓

Streamlit

↓

FastAPI

↓

PostgreSQL

↓

Claude API

↓

Admin Dashboard
```

Future production deployment may include managed cloud services, object storage, and containerized hosting based on project requirements.

---

# 13. Future Architecture Enhancements

- Authentication
- Email Notifications
- Background Job Queue
- Redis Caching
- Docker
- Kubernetes
- CI/CD Pipeline
- Cloud Storage
- Monitoring & Alerting
- Analytics Dashboard

---

# 14. Conclusion

The EB1A Resume Screener follows a modular architecture that separates the frontend, backend, OCR, resume parsing, AI evaluation, and database layers.

This design improves maintainability, scalability, and allows new features to be added with minimal impact on existing components.

---

**End of Document**