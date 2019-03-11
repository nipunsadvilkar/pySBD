# -*- coding: utf-8 -*-
from pySBD.lang.common.numbers import Common
from pySBD.cleaner import Cleaner
# from pySBD.abbreviation_replacer import AbbreviationReplacer


class English(object):

    def __init__(self):
        pass

    def clear_quotations(self, text):
        raise NotImplementedError

    def abbreviations(self, text):
        raise NotImplementedError


# class EnAbbreviationReplacer(AbbreviationReplacer):
#     raise NotImplementedError
