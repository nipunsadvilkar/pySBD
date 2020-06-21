# -*- coding: utf-8 -*-
import re

from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard
from pysbd.utils import Rule

class Arabic(Common, Standard):

    iso_code = 'ar'

    Punctuations = ['?', '!', ':', '.', '؟', '،']
    SENTENCE_BOUNDARY_REGEX = r'.*?[:\.!\?؟،]|.*?\Z|.*?$'

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

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ['ا', 'ا. د', 'ا.د', 'ا.ش.ا', 'ا.ش.ا', 'إلخ', 'ت.ب', 'ت.ب', 'ج.ب', 'جم', 'ج.ب', 'ج.م.ع', 'ج.م.ع', 'س.ت', 'س.ت', 'سم', 'ص.ب.', 'ص.ب', 'كج.', 'كلم.', 'م', 'م.ب', 'م.ب', 'ه',]
        PREPOSITIVE_ABBREVIATIONS = []
        NUMBER_ABBREVIATIONS = []
