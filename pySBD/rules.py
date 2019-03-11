#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# https://regex101.com/r/P1IWyb/1/
NEWLINE_IN_MIDDLE_OF_SENTENCE_REGEX = r"(?<=\s)\n(?=([a-z]|\())"
NEWLINE_IN_MIDDLE_OF_WORD_REGEX = r"\n(?=[a-zA-Z]{1,2}\\n)"


class Rule(object):

    def __init__(self, pattern, replacement):
        self.pattern = pattern
        self.replacement = replacement


class Text(str):

    def apply(self, *rules):
        for each_r in rules:
            self = re.sub(each_r.pattern, each_r.replacement, self)
            # print(self, each_r)
        return self


def sample_segment(s, expected_s):
    return expected_s


if __name__ == "__main__":
    SubstituteListPeriodRule = Rule('♨', '∯')
    StdRule = Rule(r'∯', r'∯♨')
    more_rules = [Rule(r'∯♨', r'∯∯∯∯'), Rule(r'∯∯∯∯', '♨♨')]
    # Text("I. abcd ♨ acnjfe").apply(SubstituteListPeriodRule, StdRule)
    sample_text = Text("I. abcd ♨ acnjfe")
    output = sample_text.apply(SubstituteListPeriodRule, StdRule, *more_rules)
    print(output)
    # I. abcd $ acnjfe
