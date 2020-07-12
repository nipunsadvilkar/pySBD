# -*- coding: utf-8 -*-
import re

from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class Bulgarian(Common, Standard):

    iso_code = 'bg'

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ['бел.пр', 'б.ред', 'бел.а', 'куб.м', 'т.нар', 'акад', 'кв.м', 'млрд', 'напр', 'полк', 'проф', 'табл', 'p.s', 'б.р', 'бул', 'вкл', 'ген', 'доц', 'заб', 'зам', 'инж', 'к.с', 'кор', 'куб', 'м.г', 'мин', 'млн', 'н.с', 'рис', 'сек', 'срв', 'стр', 'т.г', 'т.е', 'т.н', 'тел', 'фиг', 'хил', 'щ.д', 'ал', 'бр', 'вж', 'вм', 'вр', 'гр', 'дж', 'дм', 'др', 'ем', 'кв', 'кг', 'км', 'лв', 'мм', 'пл', 'св', 'см', 'сп', 'ст', 'ул', 'ха', 'чл']
        ABBREVIATIONS2 = ['в', 'г', 'л', 'м', 'р', 'с', 'т', 'у', 'ч']
        NUMBER_ABBREVIATIONS = []
        PREPOSITIVE_ABBREVIATIONS = []

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []

        def __init__(self, text, lang):
            super().__init__(text, lang)

        def replace_period_of_abbr(self, txt, abbr):
            txt = re.sub(r'(?<=\s{abbr})\.|(?<=^{abbr})\.'.format(abbr=abbr.strip()), '∯', txt)
            return txt
