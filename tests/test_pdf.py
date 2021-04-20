import os
import unittest

from constants import SONESPASES
from processors.PDFProcessor import PDFProcessor


class TestPDF(unittest.TestCase):
    def test_pdf_extraction(self):
        for filename in os.listdir(SONESPASES):
            print(f"================={filename}================")
            print(PDFProcessor.get_text(os.path.join(SONESPASES, filename)))


if __name__ == '__main__':
    unittest.main()
