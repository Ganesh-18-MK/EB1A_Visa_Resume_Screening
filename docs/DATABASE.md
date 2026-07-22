# 🗄️ Database Design Document

# EB1A Resume Screener

**Version:** 1.0

**Database:** PostgreSQL

---

# 1. Overview

The database stores all candidate information, uploaded resumes, questionnaire responses, AI evaluation results, and application statuses.

The design follows a normalized relational model to ensure data integrity, scalability, and maintainability.

---

# 2. Database Architecture

```
                 Candidate
                     │
                     ▼
          Candidate Information
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 Resume        Questionnaire    AI Evaluation
      │              │              │
      └──────────────┼──────────────┘
                     ▼
              Application Status
```

---

# 3. Database Tables

## candidates

Stores basic applicant information.

| Column | Type | Description |
|---------|------|-------------|
| id | SERIAL | Primary Key |
| full_name | VARCHAR(200) | Candidate Name |
| email | VARCHAR(255) | Email Address |
| phone | VARCHAR(30) | Phone Number |
| country | VARCHAR(100) | Country |
| created_at | TIMESTAMP | Submission Time |

---

## resumes

Stores uploaded resume information.

| Column | Type |
|---------|------|
| id | SERIAL |
| candidate_id | INTEGER (FK) |
| file_name | VARCHAR(255) |
| file_path | TEXT |
| extracted_text | TEXT |
| uploaded_at | TIMESTAMP |

Relationship:

```
One Candidate
      │
      ▼
One Resume
```

---

## questionnaire_responses

Stores answers submitted by candidates.

| Column | Type |
|---------|------|
| id | SERIAL |
| candidate_id | INTEGER (FK) |
| question_number | INTEGER |
| answer | TEXT |

Relationship:

```
One Candidate

↓

20 Questionnaire Responses
```

---

## parsed_resume

Stores structured resume information generated after parsing.

| Column | Type |
|---------|------|
| id | SERIAL |
| candidate_id | INTEGER (FK) |
| education | JSONB |
| experience | JSONB |
| publications | JSONB |
| awards | JSONB |
| patents | JSONB |
| certifications | JSONB |
| memberships | JSONB |
| skills | JSONB |

Using JSONB allows flexibility as resume structures vary.

---

## ai_evaluation

Stores AI-generated screening results.

| Column | Type |
|---------|------|
| id | SERIAL |
| candidate_id | INTEGER (FK) |
| eligibility | VARCHAR(50) |
| score | INTEGER |
| recommendation | TEXT |
| missing_criteria | JSONB |
| ai_response | JSONB |
| evaluated_at | TIMESTAMP |

---

## application_status

Tracks the application's review status.

| Column | Type |
|---------|------|
| id | SERIAL |
| candidate_id | INTEGER (FK) |
| status | VARCHAR(50) |
| updated_at | TIMESTAMP |

Example Status Values:

- Submitted
- Processing
- Under Review
- Eligible
- Not Eligible
- Needs More Information

---

# 4. Entity Relationships

```
Candidate
     │
     ├──────── Resume
     │
     ├──────── Questionnaire
     │
     ├──────── Parsed Resume
     │
     ├──────── AI Evaluation
     │
     └──────── Application Status
```

---

# 5. Database Workflow

```
Resume Upload

↓

Resume Table

↓

OCR

↓

Parsed Resume

↓

AI Evaluation

↓

Application Status

↓

Admin Dashboard
```

---

# 6. Data Storage Strategy

| Data | Storage |
|------|---------|
| Resume Files | uploads/ (or Cloud Storage in production) |
| Extracted Text | PostgreSQL |
| Parsed Resume | PostgreSQL (JSONB) |
| Questionnaire | PostgreSQL |
| AI Results | PostgreSQL |

---

# 7. Indexing Strategy

Indexes should be created on:

- candidate_id
- email
- status
- created_at

This improves search and dashboard performance.

---

# 8. Data Validation

The application should validate:

- Email format
- Phone number
- PDF file type
- Required questionnaire answers
- Duplicate submissions

---

# 9. Future Database Enhancements

Future versions may include:

- User Accounts
- Admin Accounts
- Role-Based Access Control
- Audit Logs
- Notification History
- AI Prompt History
- File Versioning
- Activity Logs

---

# 10. Backup & Recovery

Recommended strategy:

- Daily PostgreSQL backups
- Automated database snapshots
- Point-in-time recovery
- Encrypted backups

---

# 11. Security Considerations

- Parameterized SQL queries
- Foreign key constraints
- Secure environment variables
- Encrypted database connections
- Principle of least privilege

---

# 12. Conclusion

The PostgreSQL database is designed to support the complete EB1A Resume Screener workflow, from candidate submission to AI evaluation and administrator review. The schema is modular and extensible, making it suitable for future enhancements without major structural changes.

---

**End of Document**