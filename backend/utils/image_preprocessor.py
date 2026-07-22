import cv2
import numpy as np


class ImagePreprocessor:

    @staticmethod
    def preprocess(pil_image):
        """
        Improve image quality before OCR.
        """

        # Convert PIL image to OpenCV format
        image = np.array(pil_image)

        # Convert RGB to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Reduce noise
        gray = cv2.medianBlur(gray, 3)

        # Apply adaptive threshold
        gray = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            2
        )

        return gray