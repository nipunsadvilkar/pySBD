# -*- coding: utf-8 -*-
import re
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.between_punctuation import BetweenPunctuation
from pysbd.lang.common import Common, Standard
from pysbd.punctuation_replacer import replace_punctuation
from pysbd.cleaner import Cleaner
from pysbd.utils import Text, Rule

class Japanese(Common, Standard):

    iso_code = 'ja'

    class Cleaner(Cleaner):

        def __init__(self, text, lang, doc_type=None):
            super().__init__(text, lang)

        def clean(self):
            self.remove_newline_in_middle_of_word()
            return self.text

        def remove_newline_in_middle_of_word(self):
            NewLineInMiddleOfWordRule = Rule(r'(?<=の)\n(?=\S)', '')
            self.text = Text(self.text).apply(NewLineInMiddleOfWordRule)

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []

    class BetweenPunctuation(BetweenPunctuation):

        def __init__(self, text):
            super().__init__(text)

        def replace(self):
            self.sub_punctuation_between_quotes_and_parens()
            return self.text

        def sub_punctuation_between_parens_ja(self):
            BETWEEN_PARENS_JA_REGEX = r'（(?=(?P<tmp>[^（）]+|\\{2}|\\.)*)(?P=tmp)）'
            self.text = re.sub(BETWEEN_PARENS_JA_REGEX, replace_punctuation,
                      self.text)

        def sub_punctuation_between_quotes_ja(self):
            BETWEEN_QUOTE_JA_REGEX = r'「(?=(?P<tmp>[^「」]+|\\{2}|\\.)*)(?P=tmp)」'
            self.text = re.sub(BETWEEN_QUOTE_JA_REGEX, replace_punctuation,
                      self.text)

        def sub_punctuation_between_quotes_and_parens(self):
            self.sub_punctuation_between_parens_ja()
            self.sub_punctuation_between_quotes_ja()
