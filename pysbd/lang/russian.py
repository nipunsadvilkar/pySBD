# -*- coding: utf-8 -*-
import re

from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class Russian(Common, Standard):

    iso_code = 'ru'

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ["y", "y.e", "а", "авт", "адм.-терр", "акад", "в", "вв", "вкз", "вост.-европ", "г", "гг", "гос", "гр", "д", "деп", "дисс", "дол", "долл", "ежедн", "ж", "жен", "з", "зап", "зап.-европ", "заруб", "и", "ин", "иностр", "инст", "к", "канд", "кв", "кг", "куб", "л", "л.h", "л.н", "м", "мин", "моск", "муж", "н", "нед", "о", "п", "пгт", "пер", "пп", "пр", "просп", "проф", "р", "руб", "с", "сек", "см", "спб", "стр", "т", "тел", "тов", "тт", "тыс", "у", "у.е", "ул", "ф", "ч"]
        PREPOSITIVE_ABBREVIATIONS = []
        NUMBER_ABBREVIATIONS = []

    class AbbreviationReplacer(AbbreviationReplacer):

        SENTENCE_STARTERS = []

        def __init__(self, text, lang):
            super().__init__(text, lang)

        def replace_period_of_abbr(self, txt, abbr):
            txt = re.sub(r'(?<=\s{abbr})\.'.format(abbr=abbr.strip()), '∯', txt)
            txt = re.sub(r'(?<=\A{abbr})\.'.format(abbr=abbr.strip()), '∯', txt)
            txt = re.sub(r'(?<=^{abbr})\.'.format(abbr=abbr.strip()), '∯', txt)
            return txt
