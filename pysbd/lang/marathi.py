# -*- coding: utf-8 -*-
# Grammer rules from https://gopract.com/Pages/Marathi-Grammar-Viramchinah.aspx
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class Marathi(Common, Standard):

    iso_code = 'mr'

    SENTENCE_BOUNDARY_REGEX = r'.*?[.!?]|.*?$'
    Punctuations = ['.', '!', '?']

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []
