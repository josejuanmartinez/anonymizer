import os

from FlairAnonymizer import FlairAnonymizer
from SpacyAnonymizer import SpacyAnonymizer
from constants import ONCOLOGY_DATA, OTHERS_DATA, OUT_DATA

if __name__ == '__main__':
    PERLOC_anonymizer = FlairAnonymizer()
    DATETIMEGPE_anonymizer = SpacyAnonymizer()

    for folder in (ONCOLOGY_DATA, OTHERS_DATA):
        for filename in os.listdir(folder):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as f:
                print(f"Processing {filename}")
                text = PERLOC_anonymizer.anonymize(f.read())
                text = DATETIMEGPE_anonymizer.anonymize(text)
                with open(os.path.join(folder, OUT_DATA, filename), 'w') as fo:
                    fo.write(text)


