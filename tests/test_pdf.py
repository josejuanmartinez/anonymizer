import logging
import os
import unittest

from constants import INPUT_DIR, OUTPUT_DIR
from processors.PDFProcessor import PDFProcessor

logging.basicConfig(level=logging.INFO)


class TestPDF(unittest.TestCase):

    def test_pdf_extraction(self):
        for filename in os.listdir(INPUT_DIR):
            ext = os.path.splitext(filename)[-1].lower()
            if ext.lower() != '.pdf':
                continue
            with open(os.path.join(OUTPUT_DIR, filename + '.extracted.txt'), encoding='utf-8', mode='w') as f:
                logging.info(f"================={filename}================")
                # text = PDFProcessor.get_text(os.path.join(INPUT_DIR, filename))
                text = PDFProcessor.get_text_from_filename(os.path.join(INPUT_DIR, filename))
                f.write(text)


if __name__ == '__main__':
    unittest.main()
