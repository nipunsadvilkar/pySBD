# -*- coding: utf-8 -*-
from pySBD.languages import Language
from pySBD.processor import Processor
from pySBD.cleaner import Cleaner


class Segmenter(object):

    def __init__(self, text, language="en", doc_type=None, clean=False):
        self.text = text
        self.language = language
        self.language_module = Language.get_language_code(language)
        self.doc_type = doc_type
        self.clean = clean
        if clean:
            self.text = Cleaner(self.text, doc_type=doc_type).clean()
        else:
            self.text = text

    def segment(self):
        if not self.text:
            return []
        processor = Processor(self.text)
        segments = processor.process()
        return segments


if __name__ == "__main__":
    text = "Saint Maximus (died 250) is a Christian saint and martyr.[1] The emperor Decius published a decree ordering the veneration of busts of the deified emperors."
    # ["Saint Maximus (died 250) is a Christian saint and martyr.[1]", "The emperor Decius published a decree ordering the veneration of busts of the deified emperors."
    print("Input String:\n{}".format(text))
    seg = Segmenter(text, clean=True)
    segments = seg.segment()
    print("\n################## Processing #######################\n")
    print("Number of sentences: {}\n".format(len(segments)))
    print("Sentences found:\n{}\n".format(segments))
    print("\n################## Output #######################\n")
    for ind, sent in enumerate(segments, start=1):
        print("{} -> {}".format(ind, sent))
