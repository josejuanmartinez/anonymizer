import re
from enum import Enum


class ESEntities(Enum):
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
    PHONE = 11,
    SOCIAL = 12,
    HISTORY = 13

    @classmethod
    def get_regex(cls, ent):
        if ent == ESEntities.PHONES:
            return re.compile(r"(?:telefono|Telefono|teléfono|Teléfono|TELÉFONO){1}[\s]*(?:móvil|Móvil|movil|Movil|celular|Celular|Fijo|fijo|Casa|casa)?[\s\n]*:?[\s\n]*[\d.(+)-]+")
        elif ent == ESEntities.PHONE:
            return re.compile(r"^[+]*[(]?[0-9]{1,4}[)]?[-\s./0-9]*$")
        elif ent == ESEntities.EMAIL:
            return re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
        elif ent == ESEntities.DOCUMENT:
            return re.compile(
                r"(?:documento|DOCUMENTO|Documento|NIE|NIF|Pasaporte|PASAPORTE|pasaporte){1}[\s\n]*:?[\s\n]*(?:CC|cc)?[\s\n]*(?:No|no|Nº|Número|número|Numero|numero|NUMERO|NÚMERO|Num.)?[\s\n]*[\s\n]*[\d]+-?[TRWAGMYFPDXBNJZSQVHLCKEtrwagmyfpdxbnjzsqvhlcke]?")
        elif ent == ESEntities.NIF:
            return re.compile(r"[0-9]{2}[.-]?[0-9]{3}[.-]?[0-9]{3}[-]?[TRWAGMYFPDXBNJZSQVHLCKEtrwagmyfpdxbnjzsqvhlcke]")
        elif ent == ESEntities.NIE:
            return re.compile(r"[XYZxyz][0-9]{7}[-]?[TRWAGMYFPDXBNJZSQVHLCKEtrwagmyfpdxbnjzsqvhlcke]")
        elif ent == ESEntities.PASSPORT:
            return re.compile(r"[A-Za-z]{3}[0-9]{6}[A-Za-z]")
        elif ent == ESEntities.SOCIAL:
            return re.compile(r"([S|s]eguretat [S|s]ocial|[S|s]eguridad Social)[\s]*:?[\s]*[0-9]+")
        elif ent == ESEntities.HISTORY:
            return re.compile(r"[H|h]ist[o|ò]ria [c|C]l[í|i]nica[\s]*:[\s]*[a-zA-Z0-9]*[\s]*([N|n][ú|u]m[\.|ero])[ ]*[a-zA-Z0-9]*")