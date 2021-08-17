import os
import unittest

from cleanser.Cleanser import Cleanser
from constants import VALENCIA


class HTMLCleanser(unittest.TestCase):
    def test_html_cleanser_works(self):
        cleanser = Cleanser()
        for fn in os.listdir(VALENCIA):
            ext = os.path.splitext(fn)[-1].lower()
            if ext.lower() == '.csv' and 'clean' not in fn:
                with open(os.path.join(VALENCIA,fn), 'r', encoding='UTF-8') as fr:
                    with open(os.path.join(VALENCIA, fn+'.clean.csv'), 'w', encoding='UTF-8') as fw:
                        for line in fr:
                            fw.write(cleanser.html_to_txt(line))

if __name__ == '__main__':
    unittest.main()
