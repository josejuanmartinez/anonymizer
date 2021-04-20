import re


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
