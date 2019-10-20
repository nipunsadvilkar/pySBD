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

    def __repr__(self):
        return '<{} pattern="{}" and replacement="{}">'.format(
            self.__class__.__name__, self.pattern, self.replacement)


class Text(str):
    """Extending str functionality to apply regex rules

    https://stackoverflow.com/questions/4698493/can-i-add-custom-methods-attributes-to-built-in-python-types

    Parameters
    ----------
    str : str
        string content

    Returns
    -------
    str
        input as it is if rule pattern doesnt match
        else replacing found pattern with replacement chars
    """
    def apply(self, *rules):
        for each_r in rules:
            self = re.sub(each_r.pattern, each_r.replacement, self)
        return self

if __name__ == "__main__":
    SubstituteListPeriodRule = Rule('♨', '∯')
    StdRule = Rule(r'∯', r'∯♨')
    more_rules = [Rule(r'∯♨', r'∯∯∯∯'), Rule(r'∯∯∯∯', '♨♨')]
    sample_text = Text("I. abcd ♨ acnjfe")
    output = sample_text.apply(SubstituteListPeriodRule, StdRule, *more_rules)
    print(output)
