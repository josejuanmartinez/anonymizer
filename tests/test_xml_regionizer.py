import os
import unittest

from constants import SONESPASES
from regionizers.XMLRegionizer import XMLRegionizer


class XMLRegionizerTest(unittest.TestCase):
    def test_creates_two_regions_when_two_regions(self):
        text = "basd as dkaksd TUMOR 1: asdklakldsakl ad  a TUMOR 2: asdadsadad asd a q "
        regexp = r'TUMOR[\s]*\d'
        no_region_type = 'NO_TUMOR'
        regionizer = XMLRegionizer(regexp, no_region_type)
        xml = regionizer.process(text)
        assert len(list(xml.iter('region'))) == 3

    def test_creates_one_region_when_no_regions(self):
        text = "aaaaaaaab bbbbbb ccccc"
        regexp = r'TUMOR[\s]*\d'
        no_region_type = 'NO_TUMOR'
        regionizer = XMLRegionizer(regexp, no_region_type)
        xml = regionizer.process(text)
        assert len(list(xml.iter('region'))) == 1

    def test_creates_several_regions_from_file(self):
        regexp = r'TUMOR[\s]*\d'
        no_region_type = 'NO_TUMOR'
        regionizer = XMLRegionizer(regexp, no_region_type)
        with open(os.path.join(SONESPASES, 'train', 'AP_3.pdf.extracted.anonymized.translated_cat_spa.txt'), 'r',
                  encoding='utf-8') as fr:
            xml = regionizer.process(fr.read())
            assert len(list(xml.iter('region'))) == 3

    def test_regionizes_SonEspases_folder(self):
        regexp = r'TUMOR[\s]*\d'
        no_region_type = 'NO_TUMOR'
        regionizer = XMLRegionizer(regexp, no_region_type)
        for corpus in ('train', 'test'):
            for doc in os.listdir(os.path.join(SONESPASES, corpus)):
                target_doc = os.path.join(SONESPASES, corpus, doc + '.regions.xml')
                with open(os.path.join(SONESPASES, corpus, doc), 'r', encoding='utf-8') as fr:
                    xml = regionizer.process(fr.read(), return_text=True)
                    with open(target_doc, 'w', encoding='utf-8') as fw:
                        fw.write(xml)


if __name__ == '__main__':
    unittest.main()
