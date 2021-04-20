import os
import unittest

from anonymizers.FlairAnonymizer import FlairAnonymizer
from anonymizers.RegexAnonymizer import RegexAnonymizer
from constants import OTHERS_DATA, ONCOLOGY_DATA, OUT_DATA, SONESPASES
from processors.PDFProcessor import PDFProcessor
from sentencizers.SpacySentencizer import SpacySentencizer


class TestAnonimization(unittest.TestCase):
    def test_anonimization(self):
        # Sentencizer to process sentence by sentence (neural networks have a restriction of 512 tokens)
        sentencizer = SpacySentencizer()

        # Neural anonymizer (two languages - ES / EN)
        PERLOCDATEGPETIME_anonymizer = FlairAnonymizer()

        # Regex anonymizer for easy patterns
        PHONEEMAIL_anonymizer = RegexAnonymizer()

        for folder in (ONCOLOGY_DATA, OTHERS_DATA):
            for filename in os.listdir(folder):
                with open(os.path.join(folder, filename), 'r', encoding='utf-8') as f:
                    doc_sents = []
                    print(f"Processing {filename}")
                    for sent in sentencizer.sentencize(f.read()):
                        sent_str = sent.text
                        sentxt = PHONEEMAIL_anonymizer.anonynimize(sent_str)
                        sentxt = PERLOCDATEGPETIME_anonymizer.anonymize(sentxt)

                        doc_sents.append(sentxt)
                    with open(os.path.join(folder, OUT_DATA, filename), 'w', encoding='utf-8') as fo:
                        fo.write('\n'.join(doc_sents))

if __name__ == '__main__':
    unittest.main()
