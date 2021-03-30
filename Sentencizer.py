import spacy


class Sentencizer:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_md")
        self.nlp.disable_pipe("parser")
        self.nlp.enable_pipe("senter")
        pass

    def sentencize(self, text):
        return self.nlp(text).sents