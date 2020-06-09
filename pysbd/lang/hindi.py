# -*- coding: utf-8 -*-
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class Hindi(Common, Standard):

    iso_code = 'hi'

    SENTENCE_BOUNDARY_REGEX = r'.*?[।\|!\?]|.*?$'
    Punctuations = ['।', '|', '.', '!', '?']

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []
