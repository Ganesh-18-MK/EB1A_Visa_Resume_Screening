from pdf2image import convert_from_path
import pytesseract

from backend.utils.image_preprocessor import ImagePreprocessor


class TesseractExtractor:

    @staticmethod
    def extract(file_path: str) -> str:

        images = convert_from_path(file_path)

        extracted_text = []

        for image in images:

            processed = ImagePreprocessor.preprocess(image)

            page_text = pytesseract.image_to_string(
                processed,
                lang="eng",
                config="--oem 3 --psm 6"
            )

            extracted_text.append(page_text)

        return "\n".join(extracted_text).strip()