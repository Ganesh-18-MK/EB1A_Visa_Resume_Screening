# API Documentation

# EB1A Resume Screener

Version: 1.0

---

# Overview

The EB1A Resume Screener exposes REST APIs that allow the frontend to communicate with the backend services.

The APIs are responsible for:

- Resume Upload
- Questionnaire Submission
- Candidate Evaluation
- Admin Dashboard
- Candidate Management

Base URL

```
http://localhost:8000/api/v1
```

---

# API Workflow

```
Candidate Portal

↓

FastAPI REST API

↓

Business Logic

↓

OCR

↓

Resume Parser

↓

Knowledge Base

↓

Claude AI

↓

PostgreSQL
```

---

# API Endpoints

## Health Check

### GET

```
/health
```

Description

Checks whether the backend is running.

Response

```json
{
  "status":"running"
}
```

---

## Upload Resume

### POST

```
/resume/upload
```

Description

Uploads a candidate resume.

Request

```
multipart/form-data
```

Parameters

| Name | Type | Required |
|------|------|----------|
| file | PDF | Yes |

Response

```json
{
    "candidate_id":1,
    "message":"Resume uploaded successfully"
}
```

---

## Submit Questionnaire

### POST

```
/questionnaire/submit
```

Description

Stores questionnaire responses.

Request

```json
{
    "candidate_id":1,
    "responses":[]
}
```

Response

```json
{
    "message":"Questionnaire submitted"
}
```

---

## Evaluate Candidate

### POST

```
/evaluate
```

Description

Runs the complete AI evaluation.

Process

- OCR
- Resume Parsing
- Knowledge Base
- Claude AI

Response

```json
{
    "candidate_id":1,
    "eligibility":"Eligible",
    "score":86,
    "recommendation":"Strong Candidate"
}
```

---

## Get All Candidates

### GET

```
/candidates
```

Description

Returns all submitted candidates.

Response

```json
[
   {
      "candidate_id":1,
      "name":"John Doe",
      "status":"Pending"
   }
]
```

---

## Candidate Details

### GET

```
/candidate/{id}
```

Returns

- Resume
- Questionnaire
- AI Evaluation
- Status

---

## Update Candidate Status

### PUT

```
/candidate/{id}/status
```

Request

```json
{
   "status":"Eligible"
}
```

Response

```json
{
   "message":"Status Updated"
}
```

---

## Delete Candidate

### DELETE

```
/candidate/{id}
```

Response

```json
{
    "message":"Candidate Deleted"
}
```

---

# Status Codes

| Code | Meaning |
|------|----------|
|200|Success|
|201|Created|
|400|Bad Request|
|404|Not Found|
|500|Internal Server Error|

---

# Error Response

```json
{
    "error":"Resume not found"
}
```

---

# Future APIs

- Login
- Register
- Email Notification
- Export Report
- Analytics
- Bulk Upload

---

# API Versioning

Current Version

```
v1
```

Future versions

```
v2
v3
```

---

# Security

Future implementation will include

- JWT Authentication
- HTTPS
- Rate Limiting
- API Key Protection

---

# API Flow

```
Frontend

↓

POST Resume

↓

Backend

↓

OCR

↓

Resume Parser

↓

Knowledge Base

↓

Claude AI

↓

Database

↓

Frontend
```

---

# End of Document