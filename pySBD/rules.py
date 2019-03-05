#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# https://regex101.com/r/P1IWyb/1/
NEWLINE_IN_MIDDLE_OF_SENTENCE_REGEX = r"(?<=\s)\n(?=([a-z]|\())"
NEWLINE_IN_MIDDLE_OF_WORD_REGEX = r"\n(?=[a-zA-Z]{1,2}\\n)"


class Rule(object):

    def __init__(self, pattern, replace):
        self.pattern = pattern
        self.replace = replace

    def apply(self, text):
        return re.sub(r'{}'.format(self.pattern), self.replace, text)
