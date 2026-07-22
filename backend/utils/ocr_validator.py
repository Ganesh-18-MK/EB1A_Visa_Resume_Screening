import re


class OCRValidator:

    MIN_TEXT_LENGTH = 300
    MIN_WORDS = 50

    @staticmethod
    def is_valid(text: str) -> bool:

        if not text:
            return False

        text = text.strip()

        if len(text) < OCRValidator.MIN_TEXT_LENGTH:
            return False

        words = text.split()

        if len(words) < OCRValidator.MIN_WORDS:
            return False

        readable = len(re.findall(r"[A-Za-z]", text))

        if readable < 100:
            return False

        # Resume should usually contain at least one email
        email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

        # Resume should usually contain a phone number
        phone = re.search(r"\+?\d[\d\s().-]{7,}", text)

        if not email and not phone:
            return False

        return True