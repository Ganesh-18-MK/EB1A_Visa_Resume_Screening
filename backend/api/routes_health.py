from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "message": "EB1A Resume Screener API is running."
    }