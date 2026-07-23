from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.citation_service import CitationService

router = APIRouter()


class CitationLookupRequest(BaseModel):
    orcid: str | None = None
    profile_url: str | None = None
    candidate_name: str | None = None


@router.post("/citations/lookup")
async def lookup_citations(request: CitationLookupRequest):

    # 1. ORCID (highest priority)
    if request.orcid:
        result = CitationService.search_by_orcid(request.orcid)
        if result:
            return result

    # 2. Profile URL (future implementation)
    if request.profile_url:
        result = CitationService.search_by_profile(request.profile_url)
        if result:
            return result

    # 3. Candidate name (fallback)
    if request.candidate_name:
        result = CitationService.search_author(request.candidate_name)
        if result:
            return result

    return {"message": "No citation record found."}