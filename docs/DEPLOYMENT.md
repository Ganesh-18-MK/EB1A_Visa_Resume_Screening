# 🚀 Deployment Guide

# EB1A Resume Screener

**Version:** 1.0

**Deployment Platform:** Local Development → Google Cloud Run (Production)

---

# 1. Overview

This document describes how to set up, run, and deploy the EB1A Resume Screener application.

The application consists of:

- Streamlit Frontend
- FastAPI Backend
- PostgreSQL Database
- Tesseract OCR
- Claude AI Integration

---

# 2. System Requirements

## Software

- Python 3.11+
- PostgreSQL 15+
- Git
- Tesseract OCR
- Visual Studio Code

---

## Python Libraries

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 3. Project Structure

```
EB1A_Resume_Screener/

backend/
frontend/
docs/
tests/
requirements.txt
.env
README.md
```

---

# 4. Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/eb1a_db

CLAUDE_API_KEY=your_api_key

TESSERACT_PATH=/opt/homebrew/bin/tesseract

UPLOAD_FOLDER=backend/uploads

SECRET_KEY=your_secret_key
```

Never commit the `.env` file to GitHub.

---

# 5. PostgreSQL Setup

Create a new PostgreSQL database.

```sql
CREATE DATABASE eb1a_db;
```

Update the `.env` file with the database credentials.

---

# 6. Install Tesseract OCR

### macOS

```bash
brew install tesseract
```

Verify installation:

```bash
tesseract --version
```

---

# 7. Run FastAPI Backend

Navigate to the backend folder.

```bash
cd backend
```

Start the API server.

```bash
uvicorn main:app --reload
```

Backend URL

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

---

# 8. Run Streamlit Frontend

Navigate to the frontend folder.

```bash
cd frontend
```

Run the application.

```bash
streamlit run Home.py
```

Frontend URL

```
http://localhost:8501
```

---

# 9. Application Startup Sequence

```
Start PostgreSQL

↓

Start FastAPI

↓

Start Streamlit

↓

Upload Resume

↓

Evaluate Candidate
```

---

# 10. Production Deployment

The recommended production environment consists of:

| Component | Platform |
|-----------|----------|
| Frontend | Streamlit |
| Backend | Google Cloud Run |
| Database | Google Cloud SQL (PostgreSQL) |
| Resume Storage | Google Cloud Storage |
| AI | Claude API |

---

# 11. Deployment Workflow

```
GitHub

↓

CI/CD Pipeline

↓

Google Cloud Run

↓

Cloud SQL

↓

Cloud Storage

↓

Production
```

---

# 12. Logging

Application logs should capture:

- Resume Upload
- OCR Processing
- Resume Parsing
- AI Evaluation
- Database Operations
- Errors

Log files are stored in:

```
backend/logs/
```

---

# 13. Backup Strategy

Recommended production backups:

- Daily PostgreSQL backup
- Weekly full backup
- Resume storage backup
- Cloud SQL automated snapshots

---

# 14. Security Checklist

- HTTPS enabled
- Environment variables secured
- Database credentials protected
- API keys stored securely
- File upload validation
- Input validation
- SQL injection prevention

---

# 15. Deployment Checklist

Before production deployment, verify:

- Python dependencies installed
- PostgreSQL running
- Tesseract installed
- Environment variables configured
- Claude API key configured
- Resume upload working
- OCR processing successful
- AI evaluation working
- Admin dashboard accessible

---

# 16. Troubleshooting

## Backend not starting

Check:

- Python version
- Missing packages
- Environment variables

---

## Database connection error

Verify:

- PostgreSQL is running
- Database credentials
- Database exists

---

## OCR not working

Check:

```bash
tesseract --version
```

Verify the Tesseract path in the `.env` file.

---

## Claude AI errors

Verify:

- API key
- Internet connection
- API usage limits

---

# 17. Future Enhancements

Future deployment improvements:

- Docker
- Kubernetes
- GitHub Actions
- Automated CI/CD
- Monitoring
- Load Balancer
- Redis Cache
- Email Service
- Multi-region deployment

---

# 18. Conclusion

The deployment process is designed to support local development and future cloud deployment with minimal changes. The modular architecture enables easy scaling, secure configuration management, and reliable production hosting.

---

**End of Document**