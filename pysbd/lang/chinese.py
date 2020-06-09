# -*- coding: utf-8 -*-
import re
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.between_punctuation import BetweenPunctuation
from pysbd.lang.common import Common, Standard
from pysbd.punctuation_replacer import replace_punctuation

class Chinese(Common, Standard):

    iso_code = 'zh'

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []

    class BetweenPunctuation(BetweenPunctuation):

        def __init__(self, text):
            super().__init__(text)

        def replace(self):
            self.sub_punctuation_between_quotes_and_parens()
            return self.text

        def sub_punctuation_between_double_angled_quotation_marks(self):
            BETWEEN_DOUBLE_ANGLE_QUOTATION_MARK_REGEX = r"《(?=(?P<tmp>[^》\\]+|\\{2}|\\.)*)(?P=tmp)》"
            self.text = re.sub(BETWEEN_DOUBLE_ANGLE_QUOTATION_MARK_REGEX, replace_punctuation,
                      self.text)

        def sub_punctuation_between_l_bracket(self):
            BETWEEN_L_BRACKET_REGEX = r"「(?=(?P<tmp>[^」\\]+|\\{2}|\\.)*)(?P=tmp)」"
            self.text = re.sub(BETWEEN_L_BRACKET_REGEX, replace_punctuation,
                      self.text)

        def sub_punctuation_between_quotes_and_parens(self):
            self.sub_punctuation_between_double_angled_quotation_marks()
            self.sub_punctuation_between_l_bracket()
