import os

from RegexAnonymizer import RegexAnonymizer
from Sentencizer import Sentencizer

# from FlairAnonymizer import FlairAnonymizer
# from SpacyAnonymizer import SpacyAnonymizer
from constants import ONCOLOGY_DATA, OTHERS_DATA, OUT_DATA

if __name__ == '__main__':
    sentencizer = Sentencizer()
    PHONEEMAIL_anonymizer = RegexAnonymizer()
    # PERLOC_anonymizer = FlairAnonymizer()
    # DATETIMEGPE_anonymizer = SpacyAnonymizer()

    for folder in (ONCOLOGY_DATA, OTHERS_DATA):
        for filename in os.listdir(folder):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as f:
                doc_sents = []
                print(f"Processing {filename}")
                for sent in sentencizer.sentencize(f.read()):
                    sent_str = sent.text
                    sentxt = PHONEEMAIL_anonymizer.anonynimize(sent_str)
                    # sentxt = PERLOC_anonymizer.anonymize(sentxt)
                    # sentxt = DATETIMEGPE_anonymizer.anonymize(sentxt)

                    doc_sents.append(sentxt)
                with open(os.path.join(folder, OUT_DATA, filename), 'w', encoding='utf-8') as fo:
                    fo.write('\n'.join(doc_sents))


