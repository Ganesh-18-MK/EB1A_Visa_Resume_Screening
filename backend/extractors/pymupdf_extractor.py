import fitz


class PyMuPDFExtractor:

    @staticmethod
    def extract(file_path: str) -> str:
        text = ""

        document = fitz.open(file_path)

        for page in document:
            text += page.get_text()

        document.close()

        return text.strip()