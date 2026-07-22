# 🚀 EB1A Resume Screener

> AI-powered Resume Screening & Eligibility Assessment Platform for EB1A (Employment-Based First Preference – Extraordinary Ability) Visa Applicants.

---

## 📖 Overview

The **EB1A Resume Screener** is an AI-powered web application that automates the initial screening process for EB1A visa applicants.

The platform allows candidates to upload their resume and complete an eligibility questionnaire. It then extracts information from the resume using OCR and resume parsing techniques, evaluates the candidate against EB1A eligibility criteria using a Knowledge Base and Claude AI, and presents the results to immigration specialists through an Admin Dashboard.

The goal is to reduce manual effort, improve consistency, and accelerate candidate qualification.

---

# ✨ Features

## Candidate Portal

- Resume Upload
- Eligibility Questionnaire
- Application Submission
- Input Validation

---

## Resume Intelligence

- OCR (Tesseract)
- PDF Text Extraction
- Resume Parsing
- Structured JSON Generation

---

## AI Evaluation

- Knowledge Base Integration
- Claude AI Evaluation
- Eligibility Score
- Recommendation Generation
- Missing Criteria Identification

---

## Admin Dashboard

- Candidate Management
- Resume Viewer
- Questionnaire Viewer
- AI Evaluation Results
- Search & Filters
- Status Management

---

# 🏗️ Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Programming Language | Python 3.x |
| OCR | Tesseract OCR |
| PDF Processing | PyMuPDF |
| Resume Parsing | spaCy |
| Image Processing | OpenCV |
| AI | Claude API |
| Database | PostgreSQL |
| ORM *(Planned)* | SQLAlchemy |
| Deployment | Render |
| Version Control | GitHub |
| Project Tracking | Jira |

---

# 📁 Project Structure

```text
EB1A_Resume_Screener/

│
├── README.md
├── PRD.md
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── DATABASE.md
│   ├── DEPLOYMENT.md
│   └── JIRA_PLAN.md
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── database/
│   ├── ocr/
│   ├── parser/
│   ├── knowledge_base/
│   ├── ai/
│   ├── utils/
│   ├── uploads/
│   ├── extracted/
│   ├── logs/
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── Home.py
│   ├── candidate/
│   ├── admin/
│   └── components/
│
├── tests/
│
└── scripts/
```

---

# 🏛️ High-Level Architecture

```text
                    Candidate

                        │
                        ▼

             Upload Resume & Answer Questionnaire

                        │
                        ▼

                Streamlit Frontend

                        │
                        ▼

                  FastAPI Backend

        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼

     OCR Engine   Resume Parser   Questionnaire

        │              │              │
        └──────────────┼──────────────┘
                       ▼

             Candidate Profile Builder

                       ▼

                Knowledge Base Engine

                       ▼

                 Claude AI Evaluation

                       ▼

                 PostgreSQL Database

                       ▼

                 Admin Dashboard
```

---

# 🔄 Application Workflow

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

Generate Structured JSON

↓

Knowledge Base Matching

↓

Claude AI Evaluation

↓

Eligibility Report

↓

Store Results

↓

Admin Dashboard Review
```

---

# ⚙️ Prerequisites

Before running the project, ensure the following software is installed:

- Python 3.12+
- PostgreSQL
- Tesseract OCR
- Git

Verify installations:

```bash
python --version

tesseract --version

git --version
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-org/EB1A_Resume_Screener.git

cd EB1A_Resume_Screener
```

---

## Create Virtual Environment

Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

# 🔐 Environment Variables

Create a `.env` file inside the `backend` directory.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/eb1a

CLAUDE_API_KEY=your_claude_api_key

UPLOAD_FOLDER=uploads

SECRET_KEY=your_secret_key

LOG_LEVEL=INFO
```

---

# ▶️ Running the Application

## Start Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

---

## Start Frontend

```bash
cd frontend

streamlit run Home.py
```

Frontend URL

```
http://localhost:8501
```

---

# 📂 Supported File Formats

The application currently supports:

- PDF
- DOCX *(Planned)*
- PNG
- JPG
- JPEG

---

# 🗄 Database

The application uses **PostgreSQL** for persistent storage.

Primary tables include:

- Candidates
- Questionnaire Responses
- Parsed Resume Data
- AI Evaluations
- Application Status

See **docs/DATABASE.md** for detailed schema.

---

# 📚 Documentation

| Document | Description |
|----------|-------------|
| PRD.md | Product Requirements Document |
| docs/ARCHITECTURE.md | System Architecture |
| docs/API.md | API Documentation |
| docs/DATABASE.md | Database Schema |
| docs/DEPLOYMENT.md | Deployment Guide |
| docs/JIRA_PLAN.md | Sprint & Jira Planning |

---

# 🚀 Deployment

Recommended deployment stack:

| Component | Platform |
|-----------|----------|
| Frontend | Streamlit Community Cloud / Render |
| Backend | Render |
| Database | PostgreSQL (Neon or Render PostgreSQL) |
| File Storage | Local (Development) / Cloud Storage (Production) |

---

# 🧪 Testing

Run tests using:

```bash
pytest
```

---

# 🤝 Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit changes with meaningful messages.
4. Open a Pull Request.
5. Ensure all tests pass before merging.

---

# 📅 Roadmap

### Phase 1

- Project Setup
- Backend
- Frontend

### Phase 2

- Resume Upload
- OCR
- Resume Parser

### Phase 3

- Questionnaire
- Knowledge Base
- Claude AI Integration

### Phase 4

- Admin Dashboard
- Testing
- Deployment

---

# 🔮 Future Enhancements

- User Authentication
- Email Notifications
- Bulk Resume Upload
- PDF Eligibility Reports
- Analytics Dashboard
- Audit Logs
- Multi-language Resume Support
- Cloud Storage Integration
- AI Chat Assistant

---

# 📄 License

This project is intended for internal development and demonstration purposes.

---

# 👥 Contributors

- **Project Owner:** Steve
- **Development Team:** Ganesh & Mohan

---

# 📞 Support

For project-related questions, enhancements, or issues, please contact the project owner or development team.

---

## ⭐ Project Status

**Current Version:** MVP (In Development)

**Target Completion:** 3 Weeks

**Development Methodology:** Agile (Sprint-Based)
