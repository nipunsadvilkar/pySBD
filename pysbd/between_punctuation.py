# -*- coding: utf-8 -*-
import re
from functools import partial
from pysbd.punctuation_replacer import replace_punctuation


class BetweenPunctuation(object):
    # Rubular: http://rubular.com/r/2YFrKWQUYi
    BETWEEN_SINGLE_QUOTES_REGEX = r"(?<=\s)'(?:[^']|'[a-zA-Z])*'"

    BETWEEN_SINGLE_QUOTE_SLANTED_REGEX = r"(?<=\s)‘(?:[^’]|’[a-zA-Z])*’"

    # Rubular: http://rubular.com/r/3Pw1QlXOjd
    BETWEEN_DOUBLE_QUOTES_REGEX = r'"(?>[^"\\]+|\\{2}|\\.)*"'

    # https://regex101.com/r/r6I1bW/1
    # https://stackoverflow.com/questions/13577372/do-python-regular-expressions-have-an-equivalent-to-rubys-atomic-grouping?noredirect=1&lq=1
    BETWEEN_DOUBLE_QUOTES_REGEX_2 = r'"(?=(?P<tmp>[^\"\\]+|\\{2}|\\.)*)(?P=tmp)"'

    # Rubular: http://rubular.com/r/x6s4PZK8jc
    BETWEEN_QUOTE_ARROW_REGEX = r'«(?>[^»\\]+|\\{2}|\\.)*»'

    BETWEEN_QUOTE_ARROW_REGEX_2 = r"\«(?=(?P<tmp>[^»\\]+|\\{2}|\\.)*)(?P=tmp)\»"

    # Rubular: http://rubular.com/r/JbAIpKdlSq
    BETWEEN_QUOTE_SLANTED_REGEX = r"“(?>[^”\\]+|\\{2}|\\.)*”"
    BETWEEN_QUOTE_SLANTED_REGEX_2 = r"\“(?=(?P<tmp>[^”\\]+|\\{2}|\\.)*)(?P=tmp)\”"

    # Rubular: http://rubular.com/r/WX4AvnZvlX
    BETWEEN_SQUARE_BRACKETS_REGEX = r"\[(?>[^\]\\]+|\\{2}|\\.)*\]"

    BETWEEN_SQUARE_BRACKETS_REGEX_2 = r'\[(?=(?P<tmp>[^\]\\]+|\\{2}|\\.)*)(?P=tmp)\]'

    # Rubular: http://rubular.com/r/6tTityPflI
    BETWEEN_PARENS_REGEX = r"\((?>[^\(\)\\]+|\\{2}|\\.)*\)"

    BETWEEN_PARENS_REGEX_2 = r"\((?=(?P<tmp>[^\(\)\\]+|\\{2}|\\.)*)(?P=tmp)\)"

    # Rubular: http://rubular.com/r/mXf8cW025o
    WORD_WITH_LEADING_APOSTROPHE = r"(?<=\s)'(?:[^']|'[a-zA-Z])*'\S"

    # Rubular: http://rubular.com/r/jTtDKfjxzr
    BETWEEN_EM_DASHES_REGEX = r"\-\-(?>[^\-\-])*\-\-"

    BETWEEN_EM_DASHES_REGEX_2 = r"--(?=(?P<tmp>[^--]*))(?P=tmp)--"

    def __init__(self, text):
        self.text = text

    def replace(self):
        return self.sub_punctuation_between_quotes_and_parens(self.text)

    def sub_punctuation_between_quotes_and_parens(self, txt):
        txt = self.sub_punctuation_between_single_quotes(txt)
        txt = self.sub_punctuation_between_single_quote_slanted(txt)
        txt = self.sub_punctuation_between_double_quotes(txt)
        txt = self.sub_punctuation_between_square_brackets(txt)
        txt = self.sub_punctuation_between_parens(txt)
        txt = self.sub_punctuation_between_quotes_arrow(txt)
        txt = self.sub_punctuation_between_em_dashes(txt)
        txt = self.sub_punctuation_between_quotes_slanted(txt)
        return txt

    def sub_punctuation_between_parens(self, txt):
        return re.sub(self.BETWEEN_PARENS_REGEX_2, replace_punctuation, txt)

    def sub_punctuation_between_square_brackets(self, txt):
        return re.sub(self.BETWEEN_SQUARE_BRACKETS_REGEX_2, replace_punctuation,
                      txt)

    def sub_punctuation_between_single_quotes(self, txt):
        if re.search(self.WORD_WITH_LEADING_APOSTROPHE, txt) and \
                (not re.search(r"'\s", txt)):
            return txt
        return re.sub(self.BETWEEN_SINGLE_QUOTES_REGEX,
                      partial(replace_punctuation, match_type='single'), txt)

    def sub_punctuation_between_single_quote_slanted(self, txt):
        return re.sub(self.BETWEEN_SINGLE_QUOTE_SLANTED_REGEX,
                      replace_punctuation, txt)

    def sub_punctuation_between_double_quotes(self, txt):
        return re.sub(self.BETWEEN_DOUBLE_QUOTES_REGEX_2, replace_punctuation,
                      txt)

    def sub_punctuation_between_quotes_arrow(self, txt):
        return re.sub(self.BETWEEN_QUOTE_ARROW_REGEX_2, replace_punctuation, txt)

    def sub_punctuation_between_em_dashes(self, txt):
        return re.sub(self.BETWEEN_EM_DASHES_REGEX_2, replace_punctuation, txt)

    def sub_punctuation_between_quotes_slanted(self, txt):
        return re.sub(self.BETWEEN_QUOTE_SLANTED_REGEX_2, replace_punctuation,
                      txt)
