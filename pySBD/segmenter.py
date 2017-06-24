#!/usr/bin/env python
# -*- coding: utf-8 -*-

from languages import *
from processor import Processor


class Segmenter(object):

    def __init__(self, text, language="en", doc_type=None, clean=True):
        self.text = text
        self.language = language
        self.doc_type = doc_type
        self.clean = clean
        if clean:
            self.text = cleaner.clean(text, language, doc_type)
        else:
            self.text = text

    def segment(self, text, language):
        ps = Processor()
        segments = ps.process(text, language)
        return segments


if __name__ == "__main__":
    main()

