import spacy

from Anonymizer import Anonymizer
from Entities import Entities


class SpacyAnonymizer(Anonymizer):
    def __init__(self):
        # I'm using an English NER with DATES
        self.entities = [Entities.DATE.name, Entities.TIME.name, Entities.GPE.name]
        self.nlp = spacy.load("en_core_web_trf")
        super().__init__()

    def anonymize(self, text):
        doc = self.nlp(text)
        # print('The following NER tags are found:')
        ents = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in self.entities]
        for ent in ents:
            text = text.replace(ent[0], ent[1])
        print(text)


