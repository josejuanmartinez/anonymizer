import os
import unittest

from anonymizers.RegexAnonymizer import RegexAnonymizer
from cleanser.Cleanser import Cleanser
from constants import INPUT_DIR, OUTPUT_DIR
from processors.PDFProcessor import PDFProcessor
from sentencizers.SpacySentencizer import SpacySentencizer
from translators.Translator import Translator


class TestAnonimization(unittest.TestCase):
    def test_regex_anonimization(self):
        # Sentencizer to process sentence by sentence (neural networks have a restriction of 512 tokens)
        sentencizer = SpacySentencizer()

        # Regex anonymizer for easy patterns
        regex_anonymizer = RegexAnonymizer()

        pdf_processor = PDFProcessor()

        from_lang = 'cat'
        to_lang = 'spa'

        translator = Translator(from_lang, to_lang, host='http://162.44.148.238', port='2737')

        for filename in os.listdir(INPUT_DIR):
            ext = os.path.splitext(filename)[-1].lower()
            if ext.lower() != '.pdf':
                continue
            text = pdf_processor.get_text_from_filename(os.path.join(INPUT_DIR, filename))
            sents = []
            for sent in sentencizer.sentencize(text):
                trans_sent = translator.translate(str(sent))
                clean_trans_sent = Cleanser.clean(trans_sent)
                clean_trans_sent_flair_regex = regex_anonymizer.anonymize(clean_trans_sent)
                sents.append(clean_trans_sent_flair_regex)
            with open(os.path.join(OUTPUT_DIR, filename + '.extracted.anonymized.translated_' + from_lang + '_' +
                                               to_lang + '.txt'), encoding='utf-8', mode='w') as f2:
                f2.write("\n".join(sents))


if __name__ == '__main__':
    unittest.main()
