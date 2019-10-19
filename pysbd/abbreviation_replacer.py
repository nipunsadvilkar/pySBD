# -*- coding: utf-8 -*-
import re
from pysbd.rules import Text
# TODO: SENTENCE_STARTERS should be lang specific
from pysbd.lang.standard import Abbreviation, SENTENCE_STARTERS
from pysbd.lang.common.numbers import (Common, SingleLetterAbbreviationRules,
                                       AmPmRules)


def replace_pre_number_abbr(txt, abbr):
    txt = re.sub(r'(?<=\s{abbr})\.(?=\s\d)|(?<=^{abbr})\.(?=\s\d)'.format(abbr=abbr.strip()), "∯", txt)
    txt = re.sub(r'(?<=\s{abbr})\.(?=\s+\()|(?<=^{abbr})\.(?=\s+\()'.format(abbr=abbr.strip()), "∯", txt)
    return txt


def replace_prepositive_abbr(txt, abbr):
    txt = re.sub(r'(?<=\s{abbr})\.(?=\s)|(?<=^{abbr})\.(?=\s)'.format(abbr=abbr.strip()), "∯", txt)
    txt = re.sub(r'(?<=\s{abbr})\.(?=:\d+)|(?<=^{abbr})\.(?=:\d+)'.format(abbr=abbr.strip()), "∯", txt)
    return txt


def replace_period_of_abbr(txt, abbr):
    txt = re.sub(r"(?<=\s{abbr})\.(?=((\.|\:|-|\?)|(\s([a-z]|I\s|I'm|I'll|\d|\())))|(?<=^{abbr})\.(?=((\.|\:|\?)|(\s([a-z]|I\s|I'm|I'll|\d))))".format(abbr=abbr.strip()), '∯', txt)
    txt = re.sub(r"(?<=\s{abbr})\.(?=,)|(?<=^{abbr})\.(?=,)".format(abbr=abbr.strip()), '∯', txt)
    return txt


def replace_abbreviation_as_sentence_boundary(txt):
    for word in SENTENCE_STARTERS:
        escaped = re.escape(word)
        regex = r"(U∯S|U\.S|U∯K|E∯U|E\.U|U∯S∯A|U\.S\.A|I|i.v|I.V)∯(?=\s{}\s)".format(escaped)
        txt = re.sub(regex, '\\1.', txt)
    return txt


class AbbreviationReplacer(object):

    def __init__(self, text, language='en'):
        self.text = text
        self.language = language

    def replace(self):
        self.text = Text(self.text).apply(Common.PossessiveAbbreviationRule,
                                          Common.KommanditgesellschaftRule,
                                          *SingleLetterAbbreviationRules.All)
        self.text = self.search_for_abbreviations_in_string()
        self.replace_multi_period_abbreviations()
        self.text = Text(self.text).apply(*AmPmRules.All)
        self.text = replace_abbreviation_as_sentence_boundary(self.text)
        return self.text

    def replace_multi_period_abbreviations(self):
        def mpa_replace(match):
            match = match.group()
            match = re.sub(re.escape(r'.'), '∯', match)
            return match
        self.text = re.sub(Common.MULTI_PERIOD_ABBREVIATION_REGEX, mpa_replace, self.text, flags=re.IGNORECASE)

    def search_for_abbreviations_in_string(self):
        original = self.text
        lowered = original.lower()
        for abbr in Abbreviation.ABBREVIATIONS:
            stripped = abbr.strip()
            if stripped not in lowered:
                continue
            abbrev_match = re.findall(
                r'(?:^|\s|\r|\n){}'.format(stripped), original,
                flags=re.IGNORECASE)
            if not abbrev_match:
                continue
            next_word_start = r"(?<={" + str(re.escape(stripped)) + "} ).{1}"
            char_array = re.findall(next_word_start, self.text)
            for ind, match in enumerate(abbrev_match):
                self.text = self.scan_for_replacements(self.text, match, ind, char_array)
        return self.text

    def scan_for_replacements(self, txt, am, ind, char_array):
        try:
            char = char_array[ind]
        except IndexError:
            char = ''
        prepositive = Abbreviation.PREPOSITIVE_ABBREVIATIONS
        number_abbr = Abbreviation.NUMBER_ABBREVIATIONS
        upper = str(char).isupper()
        if (not upper or am.strip().lower() in prepositive):
            if am.strip().lower() in prepositive:
                txt = replace_prepositive_abbr(txt, am)
            elif am.strip().lower() in number_abbr:
                txt = replace_pre_number_abbr(txt, am)
            else:
                txt = replace_period_of_abbr(txt, am)
        return txt


if __name__ == "__main__":
    s = "Here’s the - ahem - official citation: Baker, C., Anderson, Kenneth, Martin, James, & Palen, Leysia."
    print(AbbreviationReplacer(s).replace())
