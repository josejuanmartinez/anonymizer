import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(ROOT_DIR, 'input')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output')
DATA_DIR = os.path.join(ROOT_DIR, 'data')
ONCOLOGY_DATA = os.path.join(DATA_DIR, 'Oncologia')
OTHERS_DATA = os.path.join(DATA_DIR, 'Otros')
OUT_DATA = os.path.join(DATA_DIR, 'out')
SONESPASES = os.path.join(DATA_DIR, 'SonEspases')

entities = {
    'LOC': '<LOC>', # Flair ES
    'PER': '<PER>', # FLair ES
    'GPE': '<GPE>', # Spacy EN
    'DATE': '<DATE>', # Spacy EN
    'TIME': '<TIME>' # Spacy EN
}

NEWPAGE = '\n<<==NEWPAGE==>>\n'
