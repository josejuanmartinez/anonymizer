from cleanser.Cleanser import Cleanser
from constants import NEWPAGE
import pdfplumber


class PDFProcessor:
    def __init__(self):
        pass

    @staticmethod
    def get_text_from_filename(filename):
        all_text = []
        with pdfplumber.open(filename) as pdf:
            for page in range(0, len(pdf.pages)):
                all_text.append(Cleanser.clean(pdf.pages[page].extract_text()))
        return NEWPAGE.join(all_text)
