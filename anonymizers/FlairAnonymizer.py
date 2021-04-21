import logging

import flair
from flair.data import Sentence
from flair.models import SequenceTagger

from anonymizers.BaseAnonymizer import BaseAnonymizer

from pathlib import Path


from esentities import ESEntities

""" Configure cache dir"""
flair.cache_root = Path("/data/cache/.flair")

logging.basicConfig(level=logging.INFO)


class FlairAnonymizer(BaseAnonymizer):
    def __init__(self):
        self.entities = [ESEntities.PER.name, ESEntities.LOC.name, ESEntities.DATE.name, ESEntities.TIME.name,
                         ESEntities.GPE.name]
        self.taggers = [SequenceTagger.load("flair/ner-spanish-large"),
                        SequenceTagger.load("flair/ner-english-ontonotes-large")]
        super().__init__()

    def anonymize(self, text):
        for tagger in self.taggers:
            sentence = Sentence(text)
            tagger.predict(sentence)
            ents = [(ent.to_original_text(), ent.tag) for ent in sentence.get_spans('ner')]
            for ent in ents:
                if ent[1] in self.entities:
                    logging.info(f"Found: {ent[0]} replaced with {ent[1]}")
                    text = text.replace(ent[0], ent[1])
                else:
                    logging.info(f"Found: {ent[0]} but not replaced (skipped)")
        return text
