# -*- coding: utf-8 -*-
import re

from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class Russian(Common, Standard):

    iso_code = 'ru'

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ['вост.-европ', 'зап.-европ', 'адм.-терр', 'иностр', 'ежедн', 'заруб', 'просп', 'акад', 'дисс', 'долл', 'инст', 'канд', 'моск', 'проф', 'y.e', 'авт', 'вкз', 'гос', 'деп', 'дол', 'жен', 'зап', 'куб', 'л.h', 'л.н', 'мин', 'муж', 'нед', 'пгт', 'пер', 'руб', 'сек', 'спб', 'стр', 'тел', 'тов', 'тыс', 'у.е', 'вв', 'гг', 'гр', 'ин', 'кв', 'кг', 'пп', 'пр', 'см', 'тт', 'ул']
        ABBREVIATIONS2 = ['y', 'а', 'в', 'г', 'д', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'ч']
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
