import requests
from loguru import logger


class CitationService:

    OPENALEX_URL = "https://api.openalex.org/authors"

    # ---------------------------------------------------
    # Search using candidate name
    # ---------------------------------------------------
    @staticmethod
    def search_author(author_name: str):

        params = {
            "search": author_name,
            "per-page": 10
        }

        logger.info(f"Searching OpenAlex for: {author_name}")

        response = requests.get(
            CitationService.OPENALEX_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        if not data["results"]:
            logger.warning("No authors found.")
            return None

        resume_name = author_name.strip().lower()

        for author in data["results"]:

            openalex_name = author.get("display_name", "").strip().lower()

            logger.info(f"Checking: {openalex_name}")

            if openalex_name == resume_name:

                logger.success("Exact author match found.")

                return {
                    "name": author.get("display_name"),
                    "orcid": author.get("orcid"),
                    "citations": author.get("cited_by_count", 0),
                    "works": author.get("works_count", 0),
                    "h_index": author.get("summary_stats", {}).get("h_index")
                }

        logger.warning("No exact author match found.")
        return None


    # ---------------------------------------------------
    # Search using ORCID
    # ---------------------------------------------------
    @staticmethod
    def search_by_orcid(orcid: str):

        if not orcid:
            return None

        # Remove URL if user pasted full ORCID link
        orcid = orcid.replace("https://orcid.org/", "").strip()

        logger.info(f"Searching OpenAlex using ORCID: {orcid}")

        url = f"https://api.openalex.org/authors?filter=orcid:{orcid}"

        response = requests.get(url, timeout=20)

        response.raise_for_status()

        data = response.json()

        if not data["results"]:
            logger.warning("No author found for ORCID.")
            return None

        author = data["results"][0]

        logger.success("Author found using ORCID.")

        return {
            "name": author.get("display_name"),
            "orcid": author.get("orcid"),
            "citations": author.get("cited_by_count", 0),
            "works": author.get("works_count", 0),
            "h_index": author.get("summary_stats", {}).get("h_index")
        }


    # ---------------------------------------------------
    # Search using Profile URL
    # (Google Scholar / ResearchGate / Impactio)
    # ---------------------------------------------------
    @staticmethod
    def search_by_profile(profile_url: str):

        if not profile_url:
            return None

        logger.info(f"Profile URL received: {profile_url}")

        # To be implemented later
        return None