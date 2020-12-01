# -*- coding: utf-8 -*-
import re
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.between_punctuation import BetweenPunctuation
from pysbd.lang.common import Common, Standard
from pysbd.processor import Processor
from pysbd.utils import Text
from pysbd.punctuation_replacer import replace_punctuation
from pysbd.lists_item_replacer import ListItemReplacer


class Slovak(Common, Standard):

    iso_code = 'sk'

    class ListItemReplacer(ListItemReplacer):

        def add_line_break(self):
            # We've found alphabetical lists are causing a lot of problems with abbreviations
            # with multiple periods and spaces, such as 'Company name s. r. o.'. Disabling
            # alphabetical list parsing seems like a reasonable tradeoff.

            # self.format_alphabetical_lists()
            self.format_roman_numeral_lists()
            self.format_numbered_list_with_periods()
            self.format_numbered_list_with_parens()
            return self.text

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []

        def replace_period_of_abbr(self, txt, abbr):
            # This is a very simple version of the original function, which makes sure
            # all of the periods in the abbreviation get replaced, not only the last one.
            # In Slovak language we use a lot of abbreviations like 'Company Name s. r. o.', so it
            # is important to handle this properly.

            abbr_new = abbr.replace(".", "∯") + "∯"
            txt = txt.replace(abbr + ".", abbr_new)
            return txt

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ['č', 'no', 'nr', 's. r. o', 'ing', 'p', 'a. d', 'o. k', 'pol. pr', 'a. s. a. p', 'p. n. l', 'red', 'o.k', 'a.d', 'm.o', 'pol.pr', 'a.s.a.p', 'p.n.l', 'pp', 'sl', 'corp', 'plgr', 'tz', 'rtg', 'o.c.p', 'o. c. p', 'c.k', 'c. k', 'n.a', 'n. a', 'a.m', 'a. m', 'vz', 'i.b', 'i. b', 'ú.p.v.o', 'ú. p. v. o', 'bros', 'rsdr', 'doc', 'tu', 'ods', 'n.w.a', 'n. w. a', 'nár', 'pedg', 'paeddr', 'rndr', 'naprk', 'a.g.p', 'a. g. p', 'prof', 'pr', 'a.v', 'a. v', 'por', 'mvdr', 'nešp', 'u.s', 'u. s', 'kt', 'vyd', 'e.t', 'e. t', 'al', 'll.m', 'll. m', 'o.f.i', 'o. f. i', 'mr', 'apod', 'súkr', 'stred', 's.e.g', 's. e. g', 'sr', 'tvz', 'ind', 'var', 'etc', 'atd', 'n.o', 'n. o', 's.a', 's. a', 'např', 'a.i.i', 'a. i. i', 'a.k.a', 'a. k. a', 'konkr', 'čsl', 'odd', 'ltd', 't.z', 't. z', 'o.z', 'o. z', 'obv', 'obr', 'pok', 'tel', 'št', 'skr', 'phdr', 'xx', 'š.p', 'š. p', 'ph.d', 'ph. d', 'm.n.m', 'm. n. m', 'zz', 'roz', 'atď.', 'ev', 'v.sp', 'v. sp', 'drsc', 'mudr', 't.č', 't. č', 'el', 'os', 'co', 'r.o', 'r. o', 'str', 'p.a', 'p. a', 'zdravot', 'prek', 'gen', 'viď', 'dr', 'cca', 'p.s', 'p. s', 'zák', 'slov', 'arm', 'inc', 'max', 'd.c', 'k.o', 'a. r. k', 'd. c', 'k. o', 'a. r. k', 'soc', 'bc', 'zs', 'akad', 'sz', 'pozn', 'tr', 'nám', 'kol', 'csc', 'ul', 'sp', 'o.i', 'jr', 'zb', 'sv', 'tj', 'čs', 'tzn', 'príp', 'iv', 'hl', 'st', 'pod', 'vi', 'tis', 'stor', 'rozh', 'mld', 'atď', 'mgr', 'a.s', 'a. s', 'phd', 'z.z', 'z. z', 'judr', 'ing', 'hod', 'vs', 'písm', 's.r.o', 'min', 'ml', 'iii', 't.j', 't. j', 'spol', 'mil', 'ii', 'napr', 'resp', 'tzv']
        PREPOSITIVE_ABBREVIATIONS = ['st', 'p', 'dr', 'mudr', 'judr', 'ing', 'mgr', 'bc', 'drsc', 'doc', 'prof']
        NUMBER_ABBREVIATIONS = ['č', 'no', 'nr']

    class BetweenPunctuation(BetweenPunctuation):
        # Rubular: https://rubular.com/r/rImWbaYFtHHtf4
        BETWEEN_SLOVAK_DOUBLE_QUOTES_REGEX = r'„(?>[^“\\]+|\\{2}|\\.)*“'
        BETWEEN_SLOVAK_DOUBLE_QUOTES_REGEX_2 = r'\„(?=(?P<tmp>[^“\\]+|\\{2}|\\.)*)(?P=tmp)\“'

        def sub_punctuation_between_slovak_double_quotes(self, txt):
            return re.sub(self.BETWEEN_SLOVAK_DOUBLE_QUOTES_REGEX_2, replace_punctuation, txt)

        def sub_punctuation_between_quotes_and_parens(self, txt):
            txt = self.sub_punctuation_between_single_quotes(txt)
            txt = self.sub_punctuation_between_single_quote_slanted(txt)
            txt = self.sub_punctuation_between_double_quotes(txt)
            txt = self.sub_punctuation_between_square_brackets(txt)
            txt = self.sub_punctuation_between_parens(txt)
            txt = self.sub_punctuation_between_quotes_arrow(txt)
            txt = self.sub_punctuation_between_em_dashes(txt)
            txt = self.sub_punctuation_between_quotes_slanted(txt)
            txt = self.sub_punctuation_between_slovak_double_quotes(txt)
            return txt

    class Processor(Processor):

        def __init__(self, text, lang, char_span=False):
            super().__init__(text, lang, char_span)

        def process(self):
            if not self.text:
                return self.text
            self.text = self.text.replace('\n', '\r')

            # Here we use language specific ListItemReplacer:
            li = self.lang.ListItemReplacer(self.text)
            self.text = li.add_line_break()

            self.replace_abbreviations()
            self.replace_numbers()
            self.replace_continuous_punctuation()
            self.replace_periods_before_numeric_references()
            self.text = Text(self.text).apply(
                self.lang.Abbreviation.WithMultiplePeriodsAndEmailRule,
                self.lang.GeoLocationRule, self.lang.FileFormatRule)
            postprocessed_sents = self.split_into_segments()
            return postprocessed_sents

        def replace_numbers(self):
            self.text = Text(self.text).apply(*self.lang.Numbers.All)
            self.replace_period_in_slovak_dates()
            self.replace_period_in_ordinal_numerals()
            self.replace_period_in_roman_numerals()
            return self.text

        def replace_period_in_ordinal_numerals(self):
            # Rubular: https://rubular.com/r/0HkmvzMGTqgWs6
            self.text = re.sub(r'(?<=\d)\.(?=\s*[a-z]+)', '∯', self.text)

        def replace_period_in_roman_numerals(self):
            # Rubular: https://rubular.com/r/XlzTIi7aBRThSl
            self.text = re.sub(r'((\s+[VXI]+)|(^[VXI]+))(\.)(?=\s+)', r'\1∯', self.text, re.IGNORECASE)

        def replace_period_in_slovak_dates(self):
            MONTHS = ['Január', 'Február', 'Marec', 'Apríl', 'Máj', 'Jún', 'Júl', 'August', 'September', 'Október', 'November', 'December',
                      'Januára', 'Februára', 'Marca', 'Apríla', 'Mája', 'Júna', 'Júla', 'Augusta', 'Septembra', 'Októbra', 'Novembra', 'Decembra']
            for month in MONTHS:
                # Rubular: https://rubular.com/r/dGLZqsbjcdJvCd
                self.text = re.sub(r'(?<=\d)\.(?=\s*{month})'.format(month=month), '∯', self.text)
