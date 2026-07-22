from backend.extractors.pymupdf_extractor import PyMuPDFExtractor
from backend.extractors.tesseract_extractor import TesseractExtractor
from backend.utils.ocr_validator import OCRValidator
from loguru import logger

class ExtractionService:

    @staticmethod
    async def extract(file_path: str):

        # Step 1 - Try PyMuPDF
        logger.info("Trying PyMuPDF...")

        text = PyMuPDFExtractor.extract(file_path)

        if OCRValidator.is_valid(text):
            logger.info("PyMuPDF succeeded.")

            return {
                "engine": "PyMuPDF",
                "quality": "good",
                "text": text
            }

        logger.info("PyMuPDF extraction poor. Trying Tesseract OCR...")

        # Step 2 - Try Tesseract
        text = TesseractExtractor.extract(file_path)

        if OCRValidator.is_valid(text):
            logger.info("Tesseract succeeded.")

            return {
                "engine": "Tesseract",
                "quality": "good",
                "text": text
            }

        logger.info("Both OCR methods failed.")

        return {
            "engine": "Tesseract",
            "quality": "poor",
            "text": text
        }