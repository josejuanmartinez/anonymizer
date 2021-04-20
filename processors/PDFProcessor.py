import PyPDF2

from cleanser.Cleanser import Cleanser
from constants import NEWPAGE


class PDFProcessor:
    def __init__(self):
        pass

    @staticmethod
    def get_text(file):
        all_text = []
        reader = PyPDF2.PdfFileReader(file)
        for i in range(0, reader.getNumPages()):
            all_text.append(Cleanser.clean(reader.getPage(i).extractText()))

        return NEWPAGE.join(all_text)
