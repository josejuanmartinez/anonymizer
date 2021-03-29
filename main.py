import os

from RupertaAnonymizer import RupertaAnonymizer
from constants import ONCOLOGY_DATA, OTHERS_DATA

if __name__ == '__main__':

    txt = []
    for folder in (ONCOLOGY_DATA, OTHERS_DATA):
        for filename in os.listdir(folder):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as f:
                txt.append(f.read())

    anonymizer = RupertaAnonymizer()
    anonymizer.anonymize(txt[0])
