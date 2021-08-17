import re
import html


class Cleanser:
    def __init__(self):
        pass

    @staticmethod
    def clean(text):
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'[\n ]+', '\n', text)
        text = re.sub(r'\n', ' ', text)
        text = re.sub(r'\. +', '.\n', text)
        text = re.sub(r'^ +', '', text)
        text = re.sub(r' :', ':', text)
        text = re.sub(r' ,', ',', text)
        text = re.sub(r'\( ', '(', text)
        text = re.sub(r' \)', ')', text)
        text = re.sub(r' \.', '.', text)
        return text

    @staticmethod
    def html_to_txt(text):
        return html.unescape(text)
