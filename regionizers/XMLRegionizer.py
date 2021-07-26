import re
from xml.etree import ElementTree as ET

import logging

logging.basicConfig(level=logging.INFO)


class XMLRegionizer:
    def __init__(self, first_region_regex, region_type):
        self.regions = []
        self.region_regex = first_region_regex
        self.region_type = region_type

    def process(self, text):
        xml = ET.Element('document')
        e = 0
        counter = 1
        for reg in re.finditer(self.region_regex, text):
            region = ET.SubElement(xml, 'region')
            region_name = ET.SubElement(region, 'name')
            region_name.text = self.region_type + '_' + str(counter)
            region_text = ET.SubElement(region, 'text')
            s = reg.start()
            e = reg.end()
            region_text.text = text[s:e]
            counter += 1

        last_or_unique_region = ET.SubElement(xml, 'region')
        last_region_name = ET.SubElement(last_or_unique_region, 'name')
        last_region_name.text = self.region_type + '_' + str(counter)
        last_region_text = ET.SubElement(last_or_unique_region, 'text')
        last_region_text.text = text[e:]
        logging.info(ET.dump(xml))
        return xml
