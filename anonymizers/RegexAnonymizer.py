import re

from entities import Entities


class Anonimizer(object):
    pass


class RegexAnonymizer(Anonimizer):
    def __init__(self):
        self.entities = [Entities.PHONES, Entities.PHONE, Entities.EMAIL, Entities.DOCUMENT, Entities.NIE, Entities.NIF,
                         Entities.PASSPORT]

    def anonynimize(self, text):
        for ent in self.entities:
            if re.search(Entities.get_regex(ent), text):
                print(f"Found: {text} replaced with {ent.name}")
                text = re.sub(Entities.get_regex(ent), ent.name, text)
        return text
