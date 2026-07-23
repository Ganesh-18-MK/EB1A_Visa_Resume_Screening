from fastapi import UploadFile

from backend.services.storage_service import StorageService
from backend.services.extraction_service import ExtractionService
from backend.services.profile_extractor import ProfileExtractor

class ResumeService:

    @staticmethod
    async def process_resume(file: UploadFile):

        candidate_id, filename, file_path = await StorageService.save_resume(file)

        extraction = await ExtractionService.extract(file_path)
        profile = ProfileExtractor.extract(extraction["text"]
        )

        # Extract candidate name (first non-empty line)
        lines = extraction["text"].splitlines()

        candidate_name = None

        for line in lines:
            line = line.strip()
            if line:
                candidate_name = line
                break

        return {
            "profile": profile,
            "candidate_id": candidate_id,
            "file_name": filename,
            "status": "uploaded",
            "ocr_engine": extraction["engine"],
            "quality": extraction["quality"],
            "text_length": len(extraction["text"]),
            "preview": extraction["text"][:1000],
            "candidate_name": candidate_name,
            
        }