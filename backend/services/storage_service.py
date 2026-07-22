from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import UploadFile

UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class StorageService:

    @staticmethod
    async def save_resume(file: UploadFile):

        extension = Path(file.filename).suffix

        candidate_id = f"EB1A-{uuid4().hex[:8]}"

        filename = f"{candidate_id}{extension}"

        file_path = UPLOAD_DIR / filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return candidate_id, filename, str(file_path)