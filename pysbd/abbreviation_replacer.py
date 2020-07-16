# -*- coding: utf-8 -*-
import re
from pysbd.utils import Text


def replace_pre_number_abbr(txt, abbr):
    # prepend a space to avoid needing another regex for start of string
    txt = " " + txt
    txt = re.sub(r"(?<=\s{abbr})\.(?=(\s\d|\s+\())".format(abbr=abbr.strip()), "∯", txt)
    # remove the prepended space
    txt = txt[1:]
    return txt


def replace_prepositive_abbr(txt, abbr):
    # prepend a space to avoid needing another regex for start of string
    txt = " " + txt
    txt = re.sub(r"(?<=\s{abbr})\.(?=(\s|:\d+))".format(abbr=abbr.strip()), "∯", txt)
    # remove the prepended space
    txt = txt[1:]
    return txt


class AbbreviationReplacer(object):
    def __init__(self, text, lang):
        self.text = text
        self.lang = lang
        abbrs = "|".join([re.escape(abr.strip()) for abr in self.lang.Abbreviation.ABBREVIATIONS])
        self.abbregex = re.compile(r"(?:^|\s|\r|\n)({})\b".format(abbrs), flags=re.IGNORECASE)

    def replace(self):
        self.text = Text(self.text).apply(
            self.lang.PossessiveAbbreviationRule,
            self.lang.KommanditgesellschaftRule,
            *self.lang.SingleLetterAbbreviationRules.All
        )
        abbr_handled_text = ""
        for line in self.text.splitlines(True):
            abbr_handled_text += self.search_for_abbreviations_in_string(line)
        self.text = abbr_handled_text
        self.replace_multi_period_abbreviations()
        self.text = Text(self.text).apply(*self.lang.AmPmRules.All)
        self.text = self.replace_abbreviation_as_sentence_boundary()
        return self.text

    def replace_abbreviation_as_sentence_boundary(self):
        sent_starters = "|".join((r"(?=\s{}\s)".format(word) for word in self.SENTENCE_STARTERS))
        regex = r"(U∯S|U\.S|U∯K|E∯U|E\.U|U∯S∯A|U\.S\.A|I|i.v|I.V)∯({})".format(sent_starters)
        self.text = re.sub(regex, '\\1.', self.text)
        return self.text

    def replace_multi_period_abbreviations(self):
        def mpa_replace(match):
            match = match.group()
            match = re.sub(re.escape(r"."), "∯", match)
            return match

        self.text = re.sub(
            self.lang.MULTI_PERIOD_ABBREVIATION_REGEX,
            mpa_replace,
            self.text,
            flags=re.IGNORECASE
        )

    def replace_period_of_abbr(self, txt, abbr):
        # prepend a space to avoid needing another regex for start of string
        txt = " " + txt
        txt = re.sub(
            r"(?<=\s{abbr})\.(?=((\.|\:|-|\?|,)|(\s([a-z]|I\s|I'm|I'll|\d|\())))".format(
                abbr=abbr.strip()
            ),
            "∯",
            txt,
        )
        # remove the prepended space
        txt = txt[1:]
        return txt

    def search_for_abbreviations_in_string(self, text):
        abbrev_matches = re.findall(self.abbregex, text)
        try:
            # earlier for-loop on each abbreviation logic from
            # pragmatic-segmenter was too timetaking hence we did refactoring
            # of this function to improving performance on bigger text files.
            # Languages - ru, it, bg - were breaking due to the regex approach
            # so added ABBREVIATIONS2 to handle those languages specific
            # abbreviation cases.
            abbrs2 = "|".join([re.escape(abr.strip()) for abr in self.lang.Abbreviation.ABBREVIATIONS2])
            abbregex2 = re.compile(r"(?:^|\s|\r|\n)({})\b".format(abbrs2), flags=re.IGNORECASE)
            abbrev_matches2 = re.findall(abbregex2, text)
            abbrev_matches += abbrev_matches2
        except AttributeError:
            pass
        if not abbrev_matches:
            return text
        else:
            for ind, abbrev_match in enumerate(abbrev_matches):
                next_word_start = r"(?<={" + str(re.escape(abbrev_match)) + "} ).{1}"
                char_array = re.findall(next_word_start, text)
                text = self.scan_for_replacements(text, abbrev_match, ind, char_array)
            return text

    def scan_for_replacements(self, txt, am, ind, char_array):
        try:
            char = char_array[ind]
        except IndexError:
            char = ""
        prepositive = self.lang.Abbreviation.PREPOSITIVE_ABBREVIATIONS
        number_abbr = self.lang.Abbreviation.NUMBER_ABBREVIATIONS
        upper = str(char).isupper()
        if not upper or am.strip().lower() in prepositive:
            if am.strip().lower() in prepositive:
                txt = replace_prepositive_abbr(txt, am)
            elif am.strip().lower() in number_abbr:
                txt = replace_pre_number_abbr(txt, am)
            else:
                txt = self.replace_period_of_abbr(txt, am)
        return txt
