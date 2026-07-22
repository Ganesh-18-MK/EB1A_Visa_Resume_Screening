# 📋 Jira Project Plan

# EB1A Resume Screener

**Project Duration:** 3 Weeks

**Methodology:** Agile Scrum

**Sprint Duration:** 1 Week

**Project Owner:** Steve

**Development Team:** Full Stack Developer

---

# Project Goal

Develop an AI-powered EB1A Resume Screener that automates candidate eligibility screening using OCR, Resume Parsing, a Knowledge Base, and Claude AI.

The application will provide:

- Candidate Portal
- Resume Upload
- Eligibility Questionnaire
- AI Evaluation
- Admin Dashboard

---

# Jira Project Structure

Project

```
EB1A Resume Screener
```

Project Type

```
Software Project
```

Methodology

```
Scrum
```

Sprint Duration

```
1 Week
```

---

# EPIC 1 — Project Setup

## Goal

Set up the development environment and project structure.

### User Stories

#### US-101

As a developer,

I want the project structure to be created

So that development can begin efficiently.

Tasks

- Create Git Repository
- Create Folder Structure
- Configure Virtual Environment
- Install Dependencies
- Configure Git Ignore
- Create README

Priority

High

Story Points

3

---

#### US-102

As a developer,

I want PostgreSQL configured

So that application data can be stored.

Tasks

- Install PostgreSQL
- Create Database
- Configure Connection
- Test Connectivity

Priority

High

Story Points

5

---

# EPIC 2 — Candidate Portal

## Goal

Allow candidates to submit applications.

### User Stories

#### US-201

As a candidate,

I want to upload my resume

So that the system can evaluate my profile.

Tasks

- Resume Upload UI
- File Validation
- Upload API
- Store Resume

Priority

High

Story Points

8

---

#### US-202

As a candidate,

I want to answer eligibility questions

So that AI has additional information.

Tasks

- Questionnaire UI
- Save Responses
- Validation

Priority

High

Story Points

8

---

#### US-203

As a candidate,

I want to submit my application

So that it can be processed.

Tasks

- Submit Button
- API Integration
- Confirmation Message

Priority

Medium

Story Points

5

---

# EPIC 3 — Resume Intelligence

## Goal

Extract structured information from resumes.

### User Stories

#### US-301

As the system,

I need OCR

So that scanned resumes can be processed.

Tasks

- OCR Integration
- PDF Processing
- Image Processing

Priority

High

Story Points

8

---

#### US-302

As the system,

I want to parse resumes

So that candidate information becomes structured.

Tasks

- spaCy Integration
- Extract Name
- Extract Skills
- Extract Education
- Extract Experience
- Generate JSON

Priority

High

Story Points

13

---

# EPIC 4 — Knowledge Base & AI

## Goal

Evaluate candidate eligibility.

### User Stories

#### US-401

As the system,

I want a configurable Knowledge Base

So that eligibility criteria can be maintained.

Tasks

- Create JSON Rules
- Rule Engine
- Criteria Matching

Priority

High

Story Points

8

---

#### US-402

As the system,

I want Claude AI to evaluate candidates

So that recommendations are generated automatically.

Tasks

- Claude API Integration
- Prompt Engineering
- Parse Response
- Store Result

Priority

High

Story Points

13

---

# EPIC 5 — Admin Dashboard

## Goal

Allow administrators to review applications.

### User Stories

#### US-501

As an administrator,

I want to view all candidates

So that applications can be managed.

Tasks

- Candidate List
- Pagination
- Search
- Filters

Priority

High

Story Points

8

---

#### US-502

As an administrator,

I want to review AI recommendations

So that I can make final decisions.

Tasks

- Resume Viewer
- Questionnaire Viewer
- AI Recommendation
- Status Update

Priority

High

Story Points

13

---

# Sprint Planning

## Sprint 1 (Week 1)

### Goal

Build the application foundation.

Tasks

- Project Setup
- GitHub Repository
- FastAPI Setup
- Streamlit Setup
- PostgreSQL
- Resume Upload
- Questionnaire
- Database Models

Expected Outcome

Candidate Portal completed.

---

## Sprint 2 (Week 2)

### Goal

Implement AI processing.

Tasks

- OCR
- Resume Parser
- Knowledge Base
- Claude AI
- Candidate Evaluation
- Store Results

Expected Outcome

End-to-end AI evaluation completed.

---

## Sprint 3 (Week 3)

### Goal

Complete administration and deployment.

Tasks

- Admin Dashboard
- Search
- Filters
- Candidate Status
- Testing
- Bug Fixes
- Documentation
- Deployment

Expected Outcome

Production-ready MVP.

---

# Priority Matrix

| Priority | Description |
|-----------|-------------|
| High | Required for MVP |
| Medium | Important but can be delayed |
| Low | Future Enhancement |

---

# Definition of Done

A task is considered complete when:

- Development completed
- Code reviewed
- Tested successfully
- No critical defects
- Documentation updated
- Changes committed to GitHub

---

# Acceptance Criteria

The MVP is complete when:

- Candidates can upload resumes.
- Questionnaire responses are stored.
- OCR extracts resume content.
- Resume parser generates structured JSON.
- Claude AI evaluates eligibility.
- Results are stored in PostgreSQL.
- Admin dashboard displays all applications.
- Administrators can update candidate status.

---

# Risks

| Risk | Mitigation |
|------|------------|
| Poor OCR quality | Improve preprocessing and validation |
| AI API downtime | Retry mechanism and logging |
| Invalid resumes | File validation |
| Timeline constraints | Focus on MVP features only |

---

# Deliverables

- Candidate Portal
- Resume Upload
- Questionnaire
- OCR Engine
- Resume Parser
- Knowledge Base
- Claude AI Integration
- PostgreSQL Database
- Admin Dashboard
- API Documentation
- Deployment Guide
- Complete Project Documentation

---

# Jira Labels

Use the following labels for easy tracking:

- backend
- frontend
- database
- api
- ocr
- ai
- knowledge-base
- admin-dashboard
- candidate-portal
- testing
- deployment
- documentation

---

# Estimated Story Points

| Epic | Story Points |
|------|-------------:|
| Project Setup | 8 |
| Candidate Portal | 21 |
| Resume Intelligence | 21 |
| Knowledge Base & AI | 21 |
| Admin Dashboard | 21 |
| Testing & Deployment | 13 |

**Total Estimated Story Points:** **105**

---

# Recommended Jira Workflow

```
Backlog
    ↓
To Do
    ↓
In Progress
    ↓
Code Review
    ↓
Testing
    ↓
Done
```

---

# Conclusion

This Jira plan provides a structured roadmap for delivering the EB1A Resume Screener MVP within **3 weeks**. The work is organized into clear epics, user stories, and sprints, enabling efficient planning, tracking, and collaboration while maintaining focus on the MVP scope.

---

**End of Document**