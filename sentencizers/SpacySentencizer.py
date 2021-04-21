import spacy


class SpacySentencizer:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")
        self.nlp.disable_pipe("parser")
        self.nlp.enable_pipe("senter")
        pass

    def sentencize(self, text):
        return self.nlp(text).sents
