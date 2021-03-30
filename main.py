import os

# from RupertaAnonymizer import RupertaAnonymizer
from FlairAnonymizer import FlairAnonymizer
from SpacyAnonymizer import SpacyAnonymizer
from constants import ONCOLOGY_DATA, OTHERS_DATA

if __name__ == '__main__':
    anonymizer = FlairAnonymizer()
    # anonymizer = SpacyAnonymizer()
    txt = []
    for folder in (ONCOLOGY_DATA, OTHERS_DATA):
        for filename in os.listdir(folder):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as f:
                anonymizer.anonymize(f.read())
