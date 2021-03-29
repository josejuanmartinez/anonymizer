import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer

from Anonymizer import Anonymizer


class RupertaAnonymizer(Anonymizer):
    NER_TAGS = {
        "0": "B-LOC",
        "1": "B-MISC",
        "2": "B-ORG",
        "3": "B-PER",
        "4": "I-LOC",
        "5": "I-MISC",
        "6": "I-ORG",
        "7": "I-PER",
        "8": "O"
    }

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained('mrm8488/bert-spanish-cased-finetuned-ner')
        self.model = AutoModelForTokenClassification.from_pretrained('mrm8488/bert-spanish-cased-finetuned-ner')

        super().__init__()

    def anonymize(self, text):
        # Text to numeric tokens
        tokens_ids = self.tokenizer.encode(text[:512])
        # Creation of tensor with tokens to feed the model
        input_ids = torch.tensor(tokens_ids).unsqueeze(0)

        # Prediction
        outputs = self.model(input_ids)

        # I get last layer states (NER)
        last_hidden_states = outputs[0]

        for m in last_hidden_states:
            for index, n in enumerate(m):
                if 0 < index <= len(text.split(" ")):
                    print(text.split(" ")[index - 1] + ": " + RupertaAnonymizer.NER_TAGS[str(torch.argmax(n).item())])

