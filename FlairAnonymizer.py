import flair
from flair.data import Sentence
from flair.models import SequenceTagger

from Anonymizer import Anonymizer

from pathlib import Path


from Entities import Entities

""" Configure cache dir"""
flair.cache_root = Path("/data/cache/.flair")


class FlairAnonymizer(Anonymizer):
    def __init__(self):
        self.entities = [Entities.PER.name, Entities.LOC.name]
        self.tagger = SequenceTagger.load("flair/ner-spanish-large")
        super().__init__()

    def anonymize(self, text):
        sentence = Sentence(text)
        self.tagger.predict(sentence)
        ents = [(ent.to_original_text(), ent.tag) for ent in sentence.get_spans('ner') if ent.tag in self.entities]
        for ent in ents:
            text = text.replace(ent[0], ent[1])
        return text
