import re

from anonymizers.BaseAnonymizer import BaseAnonymizer
from esentities import ESEntities
import logging

logging.basicConfig(level=logging.INFO)


class RegexAnonymizer(BaseAnonymizer):
    def __init__(self):
        self.entities = [ESEntities.PHONES, ESEntities.PHONE, ESEntities.EMAIL, ESEntities.DOCUMENT, ESEntities.NIE,
                         ESEntities.NIF, ESEntities.PASSPORT, ESEntities.SOCIAL, ESEntities.HISTORY]
        super().__init__()

    def anonymize(self, text):
        for ent in self.entities:
            if re.search(ESEntities.get_regex(ent), text):
                logging.info(f"Found: {text} replaced with {ent.name}")
                text = re.sub(ESEntities.get_regex(ent), ent.name, text)
        return text
