from fastapi import FastAPI

from backend.core.config import settings
from backend.core.logger import app_logger
from backend.api.routes_health import router as health_router
from backend.api.routes_resume import router as resume_router
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes_citation import router as citation_router

# Create FastAPI app FIRST
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="EB1A Resume Screening API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://[::]:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
app.include_router(citation_router,
    prefix="/api/v1",
    tags=["Citation"]
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