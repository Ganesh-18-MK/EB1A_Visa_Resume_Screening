from pydantic import BaseModel


class ResumeUploadResponse(BaseModel):
    candidate_id: str
    file_name: str
    status: str
    message: str