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
        # self.SENTENCE_STARTERS = []
        # self.SENTENCE_STARTERS = "A Being Did For He How However I In It Millions "\
        #     "More She That The There They We What When Where Who Why".split(" ")

    def replace(self):
        self.text = Text(self.text).apply(
            self.lang.PossessiveAbbreviationRule,
            self.lang.KommanditgesellschaftRule,
            *self.lang.SingleLetterAbbreviationRules.All
        )
        self.text = self.search_for_abbreviations_in_string()
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

    # def search_for_abbreviations_in_string(self):
    #     original = self.text
    #     lowered = original.lower()
    #     for abbr in self.lang.Abbreviation.ABBREVIATIONS:
    #         stripped = abbr.strip()
    #         if stripped not in lowered:
    #             continue
    #         abbrev_match = re.findall(
    #             r'(?:^|\s|\r|\n){}'.format(stripped), original,
    #             flags=re.IGNORECASE)
    #         if not abbrev_match:
    #             continue
    #         next_word_start = r"(?<={" + str(re.escape(stripped)) + "} ).{1}"
    #         char_array = re.findall(next_word_start, self.text)
    #         for ind, match in enumerate(abbrev_match):
    #             # import ipdb; ipdb.set_trace()
    #             self.text = self.scan_for_replacements(self.text, match, ind, char_array)
    #     return self.text

    def search_for_abbreviations_in_string(self):
        original = self.text
        abbregex = "|".join([re.escape(abr.strip()) for abr in self.lang.Abbreviation.ABBREVIATIONS])
        abbregex2 = r"(?:^|\s|\r|\n)({})\b".format(abbregex)
        abbrev_matches = re.findall(abbregex2, original, flags=re.IGNORECASE)
        # print(self.text)
        # print(abbrev_matches)
        if not abbrev_matches:
            return self.text
        else:
            for ind, abbrev_match in enumerate(abbrev_matches):
                # import ipdb; ipdb.set_trace()
                next_word_start = r"(?<={" + str(re.escape(abbrev_match)) + "} ).{1}"
                char_array = re.findall(next_word_start, self.text)
                self.text = self.scan_for_replacements(self.text, abbrev_match, ind, char_array)
            return self.text

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


if __name__ == "__main__":
    from pysbd.languages import Language
    # lang = Language.get_language_module('bg')
    # lang = Language.get_language_module('it')
    lang = Language.get_language_module('ru')
    # tests = [('He has Ph.D. level training', [])]
    # tests = [('В първата половина на ноември т.г. ще бъде свикан Консултативният съвет за национална сигурност, обяви държавният глава.', [])]
    # tests = [('Hanno creato un algoritmo allo st. d. arte. Si ringrazia lo psicol. Serenti.', [])]
    # tests = [('Л.Н. Толстой написал "Войну и мир". Кроме Волконских, Л. Н. Толстой состоял в близком родстве с некоторыми другими ар... родами. Дом, где родился Л.Н.Толстой, 1898 г. В 1854 году дом продан по распоряжению писателя на вывоз в село Долгое.', [])]
    tests = [('Постойте, разве можно указывать цены в у.е.!', [])]
    for test in tests:
        text, expected = test
        ab = AbbreviationReplacer(text, lang)
        abtext = ab.replace()
        print(f"{text} => {abtext}")
