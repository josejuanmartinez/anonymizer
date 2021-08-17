import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(ROOT_DIR, 'input')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output')
SONESPASES = os.path.join(INPUT_DIR, 'SonEspases')
VALENCIA = os.path.join(INPUT_DIR, 'Valencia')

entities = {
    'LOC': '<LOC>', # Flair ES
    'PER': '<PER>', # FLair ES
    'GPE': '<GPE>', # Spacy EN
    'DATE': '<DATE>', # Spacy EN
    'TIME': '<TIME>' # Spacy EN
}

NEWPAGE = '\n<<==NEWPAGE==>>\n'

TRANSLATOR_PORT = '2737'
TRANSLATOR_URL = 'http://localhost'
