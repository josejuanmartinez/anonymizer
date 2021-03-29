import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
ONCOLOGY_DATA = os.path.join(DATA_DIR, 'Oncologia')
OTHERS_DATA = os.path.join(DATA_DIR, 'Otros')


entities = {
    'LOC': 'Lugar',
    'PERSON': 'Persona',
    'GPE': 'Lugar',
    'DATE': 'Fecha',
    'TIME': 'Hora'
}