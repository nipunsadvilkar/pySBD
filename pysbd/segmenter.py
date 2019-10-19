# -*- coding: utf-8 -*-
from pysbd.languages import Language
from pysbd.processor import Processor
from pysbd.cleaner import Cleaner


class Segmenter(object):

    def __init__(self, language="en", clean=False, doc_type=None, char_span=False):
        self.language = language
        self.language_module = Language.get_language_code(language)
        self.clean = clean
        self.doc_type = doc_type
        self.char_span = char_span

    def segment(self, text):
        if not text:
            return []
        if self.clean:
            text = Cleaner(text, doc_type=self.doc_type).clean()
        processor = Processor(text)
        segments = processor.process(char_span=self.char_span)
        return segments


if __name__ == "__main__":
    text = "My name is Jonas E. Smith. Please turn to p. 55."
    print("Input String:\n{}".format(text))
    seg = Segmenter(language="en", clean=True, char_span=True)
    # seg = Segmenter(language="en", clean=True, char_span=False)
    segments = seg.segment(text)
    print("\n################## Processing #######################\n")
    print("Number of sentences: {}\n".format(len(segments)))
    print("Sentences found:\n{}\n".format(segments))
    print("\n################## Output #######################\n")
    for ind, sent in enumerate(segments, start=1):
        print("{} -> {}".format(ind, sent))
