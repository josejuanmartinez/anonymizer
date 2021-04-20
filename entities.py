import re
from enum import Enum


class Entities(Enum):
    PER = 0,
    LOC = 1,
    DATE = 2,
    GPE = 3,
    TIME = 4,
    PHONES = 5,
    EMAIL = 6,
    DOCUMENT = 7,
    NIF = 8,
    NIE = 9,
    PASSPORT = 10,
    PHONE = 11

    @classmethod
    def get_regex(cls, ent):
        if ent == Entities.PHONES:
            return re.compile(r"(?:telefono|Telefono|teléfono|Teléfono|TELÉFONO){1}[\s]*(?:móvil|Móvil|movil|Movil|celular|Celular|Fijo|fijo|Casa|casa)?[\s\n]*:?[\s\n]*[\d.(+)-]+")
        elif ent == Entities.PHONE:
            return re.compile(r"^[+]*[(]?[0-9]{1,4}[)]?[-\s./0-9]*$")
        elif ent == Entities.EMAIL:
            return re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
        elif ent == Entities.DOCUMENT:
            return re.compile(
                r"(?:documento|DOCUMENTO|Documento|NIE|NIF|Pasaporte|PASAPORTE|pasaporte){1}[\s\n]*:?[\s\n]*(?:CC|cc)?[\s\n]*(?:No|no|Nº|Número|número|Numero|numero|NUMERO|NÚMERO|Num.)?[\s\n]*[\s\n]*[\d]+-?[TRWAGMYFPDXBNJZSQVHLCKEtrwagmyfpdxbnjzsqvhlcke]?")
        elif ent == Entities.NIF:
            return re.compile(r"[0-9]{2}[.-]?[0-9]{3}[.-]?[0-9]{3}[-]?[TRWAGMYFPDXBNJZSQVHLCKEtrwagmyfpdxbnjzsqvhlcke]")
        elif ent == Entities.NIE:
            return re.compile(r"[XYZxyz][0-9]{7}[-]?[TRWAGMYFPDXBNJZSQVHLCKEtrwagmyfpdxbnjzsqvhlcke]")
        elif ent == Entities.PASSPORT:
            return re.compile(r"[A-Za-z]{3}[0-9]{6}[A-Za-z]")
