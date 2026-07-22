from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.schemas.resume import ResumeUploadResponse
from backend.services.storage_service import StorageService

router = APIRouter()


@router.post(
    "/resume/upload",
    response_model=ResumeUploadResponse
)
async def upload_resume(
    resume: UploadFile = File(...)
):

    if not resume.filename.lower().endswith((".pdf", ".doc", ".docx")):
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOC and DOCX files are allowed."
        )

    candidate_id, filename, _ = await StorageService.save_resume(resume)

    return ResumeUploadResponse(
        candidate_id=candidate_id,
        file_name=filename,
        status="uploaded",
        message="Resume uploaded successfully."
    )