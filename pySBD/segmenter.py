# -*- coding: utf-8 -*-
from pySBD.languages import Language
# from pySBD.lang.english import English
from pySBD.processor import Processor
from pySBD.cleaner import Cleaner


class Segmenter(object):

    def __init__(self, text, language="en", doc_type=None, clean=False):
        self.text = text
        self.language = language
        self.language_module = Language.get_language_code(language)
        self.doc_type = doc_type
        # self.clean = clean
        if clean:
            self.cleaner = Cleaner(text)
            self.text = self.cleaner.clean()
        else:
            self.text = text

    # TODO: Can be converted to a class method
    def segment(self):
        if not self.text:
            return []
        processor = Processor(self.text, language='en')
        segments = processor.process()
        return segments


if __name__ == "__main__":
    text = "Hello World. My name is Jonas."
    # text = "\"Dinah'll miss me very much to-night, I should think!\" (Dinah was the cat.) \"I hope they'll remember her saucer of milk at tea-time. Dinah, my dear, I wish you were down here with me!\""
    s = Segmenter(text)
    print(s.segment())
    sents = s.segment()
    for s in sents:
        print(s)
