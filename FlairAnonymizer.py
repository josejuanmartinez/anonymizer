from flair.data import Sentence
from flair.models import SequenceTagger

from Anonymizer import Anonymizer


class FlairAnonymizer(Anonymizer):
    def __init__(self):
        self.tagger = SequenceTagger.load("flair/ner-spanish-large")
        super().__init__()

    def anonymize(self, text):
        sentence = Sentence(text)
        self.tagger.predict(sentence)
        # print predicted NER spans
        print('The following NER tags are found:')
        # iterate over entities and print
        for entity in sentence.get_spans('ner'):
            print(entity)

