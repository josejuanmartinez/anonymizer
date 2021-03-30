import os

from FlairAnonymizer import FlairAnonymizer
from SpacyAnonymizer import SpacyAnonymizer
from constants import ONCOLOGY_DATA, OTHERS_DATA

if __name__ == '__main__':
    txt = []
    PERLOC_anonymizer = FlairAnonymizer()
    DATETIMEGPE_anonymizer = SpacyAnonymizer()

    for folder in (ONCOLOGY_DATA, OTHERS_DATA):
        for filename in os.listdir(folder):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as f:
                text = PERLOC_anonymizer.anonymize(f.read())
                txt.append(DATETIMEGPE_anonymizer.anonymize(text))
