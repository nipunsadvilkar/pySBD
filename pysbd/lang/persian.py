# -*- coding: utf-8 -*-
import re

from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard
from pysbd.utils import Rule

class Persian(Common, Standard):

    iso_code = 'fa'

    Punctuations = ['?', '!', ':', '.', '؟']
    SENTENCE_BOUNDARY_REGEX = r'.*?[:\.!\?؟]|.*?\Z|.*?$'

    # Rubular: http://rubular.com/r/RX5HpdDIyv
    ReplaceColonBetweenNumbersRule = Rule(r'(?<=\d):(?=\d)', '♭')

    # Rubular: http://rubular.com/r/kPRgApNHUg
    ReplaceNonSentenceBoundaryCommaRule = Rule(r'،(?=\s\S+،)', '♬')

    class AbbreviationReplacer(AbbreviationReplacer):

        SENTENCE_STARTERS = []

        def __init__(self, text, lang):
            super().__init__(text, lang)

        def scan_for_replacements(self, txt, am, index, character_array):
            txt = re.sub('(?<={0})\.'.format(am), '∯', txt)
            return txt
