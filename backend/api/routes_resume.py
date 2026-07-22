from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.services.resume_service import ResumeService

router = APIRouter()


@router.post("/resume/upload")
async def upload_resume(
    resume: UploadFile = File(...)
):

    if not resume.filename.lower().endswith((".pdf", ".doc", ".docx")):
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOC and DOCX files are allowed."
        )

    return await ResumeService.process_resume(resume)