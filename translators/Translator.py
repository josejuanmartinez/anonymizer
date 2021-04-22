import json
import logging

import requests

from constants import TRANSLATOR_URL

logging.basicConfig(level=logging.INFO)


class Translator:
    def __init__(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, text):
        try:
            params = {'langpair': "|".join([self.from_lang, self.to_lang]),
                      'q': text, 'markUnknown': 'no'}

            # sending get request and saving the response as response object
            r = requests.get(url=TRANSLATOR_URL + "/translate", params=params)

            # extracting data in json format
            return r.json()['responseData']['translatedText']
        except Exception as e:
            logging.error(e)
            return json.dumps({})

