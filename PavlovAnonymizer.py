from deeppavlov import configs, build_model

from Anonymizer import Anonymizer


class PavlovAnonymizer(Anonymizer):
    def __init__(self):
        self.ner_model = build_model(configs.ner.ner_ontonotes_bert_mult, download=True)
        super().__init__()

    def anonimize(self, text):
        print(self.ner_model(text))