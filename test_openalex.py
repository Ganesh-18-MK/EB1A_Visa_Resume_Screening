from backend.services.citation_service import CitationService

author = CitationService.search_author(
    "Andrew Ng"
)

print(author)