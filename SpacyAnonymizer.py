import spacy

from Anonymizer import Anonymizer


class SpacyAnonymizer(Anonymizer):
    def __init__(self, only_NER=False):
        if only_NER:
            self.nlp = spacy.load("es_core_news_md", disable=["tagger", "parser", "attribute_ruler", "lemmatizer"])
        else:
            self.nlp = spacy.load("es_core_news_md")
        super().__init__()

    def anonymize(self, text):
        doc = self.nlp(text)
        for ent in doc.ents:
            # Do something with the doc here
            print(ent.text, ent.label_)


