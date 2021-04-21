import logging
import unittest

from translators.Translator import Translator

logging.basicConfig(level=logging.INFO)


class TranslatorTest(unittest.TestCase):
    def test_translation_ca_es(self):
        tr = Translator('ca', 'es')
        text = tr.translate("Descripció macroscòpica: Peça de mastectomia que pesa 312g i fa 17x12x2cm. "
                     "Inclou superfície de pel de 3x2.5cm amb mugró."
                     "Es marquen els marges de resecció.")
        logging.info(text)
        assert True


if __name__ == '__main__':
    unittest.main()
