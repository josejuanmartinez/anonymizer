from translate import Translator as Translate


class Translator:
    def __init__(self, from_lang, to_lang):
        self.translator = Translate(from_lang=from_lang, to_lang=to_lang)

    def translate(self, text):
        return self.translator.translate(text)
