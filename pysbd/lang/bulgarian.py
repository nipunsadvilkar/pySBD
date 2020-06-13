# -*- coding: utf-8 -*-
import re

from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class Bulgarian(Common, Standard):

    iso_code = 'bg'

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ["p.s", "акад", "ал", "б.р", "б.ред", "бел.а", "бел.пр", "бр", "бул", "в", "вж", "вкл", "вм", "вр", "г", "ген", "гр", "дж", "дм", "доц", "др", "ем", "заб", "зам", "инж", "к.с", "кв", "кв.м", "кг", "км", "кор", "куб", "куб.м", "л", "лв", "м", "м.г", "мин", "млн", "млрд", "мм", "н.с", "напр", "пл", "полк", "проф", "р", "рис", "с", "св", "сек", "см", "сп", "срв", "ст", "стр", "т", "т.г", "т.е", "т.н", "т.нар", "табл", "тел", "у", "ул", "фиг", "ха", "хил", "ч", "чл", "щ.д"]
        NUMBER_ABBREVIATIONS = []
        PREPOSITIVE_ABBREVIATIONS = []

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []

        def __init__(self, text, lang):
            super().__init__(text, lang)

        def replace_period_of_abbr(self, txt, abbr):
            txt = re.sub(r'(?<=\s{abbr})\.|(?<=^{abbr})\.'.format(abbr=abbr.strip()), '∯', txt)
            return txt
