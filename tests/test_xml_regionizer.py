import unittest

from regionizers.XMLRegionizer import XMLRegionizer


class XMLRegionizerTest(unittest.TestCase):
    def test_creates_two_regions_when_two_regions(self):
        text = "basd as dkaksd TUMOR 1: asdklakldsakl ad  a TUMOR 2: asdadsadad asd a q "
        regexp = r'(TUMOR|Tumor|tumor)[\s]*\d[\s]*:?.*(?=((TUMOR|Tumor|tumor)[\s]*\d))'
        region_type = 'TUMOR'
        regionizer = XMLRegionizer(regexp, region_type)
        xml = regionizer.process(text)
        assert len(list(xml.iter('region'))) == 2

    def test_creates_one_region_when_no_regions(self):
        text = "aaaaaaaab bbbbbb ccccc"
        regexp = r'(TUMOR|Tumor|tumor)[\s]*\d[\s]*:?.*(?=((TUMOR|Tumor|tumor)[\s]*\d))'
        region_type = 'TUMOR'
        regionizer = XMLRegionizer(regexp, region_type)
        xml = regionizer.process(text)
        assert len(list(xml.iter('region'))) == 1


if __name__ == '__main__':
    unittest.main()
