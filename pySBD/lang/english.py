# -*- coding: utf-8 -*-
from pysbd.lang.common.numbers import Common
from pysbd.cleaner import Cleaner
# from pysbd.abbreviation_replacer import AbbreviationReplacer


class English(Common):

    def __init__(self):
        pass

    def clear_quotations(self, text):
        raise NotImplementedError

    def abbreviations(self, text):
        raise NotImplementedError


# class EnAbbreviationReplacer(AbbreviationReplacer):
#     raise NotImplementedError


if __name__ == "__main__":
    ec = English()
    print(hasattr(ec, 'PARENS_BETWEEN_DOUBLE_QUOTES_REGEX'))
