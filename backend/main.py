from fastapi import FastAPI

from backend.core.config import settings
from backend.core.logger import app_logger
from backend.api.routes_health import router as health_router
from backend.api.routes_resume import router as resume_router

# Create FastAPI app FIRST
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="EB1A Resume Screening API"
)

# Then register routes
app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)
app.include_router(
    resume_router,
    prefix="/api/v1",
    tags=["Resume"]
)

@app.on_event("startup")
async def startup_event():
    app_logger.info("=======================================")
    app_logger.info(f"{settings.APP_NAME} Started")
    app_logger.info("=======================================")


@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running"
    }