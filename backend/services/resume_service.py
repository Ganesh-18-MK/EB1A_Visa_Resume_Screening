from fastapi import UploadFile

from backend.services.storage_service import StorageService
from backend.services.extraction_service import ExtractionService


class ResumeService:

    @staticmethod
    async def process_resume(file: UploadFile):

        candidate_id, filename, file_path = await StorageService.save_resume(file)

        extraction = await ExtractionService.extract(file_path)

        return {
            "candidate_id": candidate_id,
            "file_name": filename,
            "status": "uploaded",
            "ocr_engine": extraction["engine"],
            "quality": extraction["quality"],
            "text_length": len(extraction["text"]),
            "preview": extraction["text"][:1000]
        }