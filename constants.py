import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
ONCOLOGY_DATA = os.path.join(DATA_DIR, 'Oncologia')
OTHERS_DATA = os.path.join(DATA_DIR, 'Otros')


entities = {
    'LOC': '<LOC>', # Flair ES
    'PER': '<PER>', # FLair ES
    'GPE': '<GPE>', # Spacy EN
    'DATE': '<DATE>', # Spacy EN
    'TIME': '<TIME>' # Spacy EN
}