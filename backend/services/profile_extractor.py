import re


class ProfileExtractor:

    @staticmethod
    def extract(text):

        return {
            "orcid": ProfileExtractor.extract_orcid(text),
            "google_scholar": ProfileExtractor.extract_google_scholar(text)
        }

    @staticmethod
    def extract_orcid(text):

        match = re.search(
            r"(?:ORCID[: ]*)?(https?://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X])",
            text,
            re.IGNORECASE
        )

        return match.group(1) if match else None

    @staticmethod
    def extract_google_scholar(text):

        match = re.search(
            r"https?://scholar\.google\.com/citations\?user=[A-Za-z0-9_-]+",
            text
        )

        return match.group(0) if match else None