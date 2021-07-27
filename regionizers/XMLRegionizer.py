import re
from xml.etree import ElementTree as ET

import logging

logging.basicConfig(level=logging.INFO)


class XMLRegionizer:
    def __init__(self, first_region_regex, no_region_type):
        self.regions = []
        self.region_regex = first_region_regex
        self.no_region_type = no_region_type

    def process(self, text, return_text=False):
        xml = ET.Element('document')
        matches = []
        # Finding region matches
        for reg in re.finditer(self.region_regex, text):
            s = reg.start()
            e = reg.end()
            matches.append((text[s:e].upper().strip(), s, e))

        regions = []
        # Aggregating
        for i in range(0, len(matches)):
            # If first region and there is something before, I add it
            if i == 0 and matches[i][1] > 0:
                regions.append((self.no_region_type, text[0:matches[i][1]]))
            # If last region, I add up to the end
            if i == (len(matches) - 1):
                regions.append((matches[i][0], text[matches[i][1]:]))
            elif i < (len(matches) - 1):
                regions.append((matches[i][0], text[matches[i][1]:matches[i+1][1]]))

        if len(matches) == 0:
            regions.append((self.no_region_type, text))

        for i, reg in enumerate(regions):
            et_region = ET.SubElement(xml, 'region')
            et_region_name = ET.SubElement(et_region, 'name')
            et_region_name.text = reg[0]
            et_region_text = ET.SubElement(et_region, 'text')
            et_region_text.text = reg[1]

        logging.info(ET.tostring(xml, encoding='unicode', method='xml'))

        if return_text:
            return ET.tostring(xml, encoding='unicode', method='xml')
        else:
            return xml
