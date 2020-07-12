# -*- coding: utf-8 -*-
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class Amharic(Common, Standard):

    iso_code = 'am'

    SENTENCE_BOUNDARY_REGEX = r'.*?[፧።!\?]|.*?$'
    Punctuations = ['።', '፧', '?', '!']

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []
