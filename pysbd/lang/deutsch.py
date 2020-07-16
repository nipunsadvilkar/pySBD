# -*- coding: utf-8 -*-
import re
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.between_punctuation import BetweenPunctuation
from pysbd.lang.common import Common, Standard
from pysbd.punctuation_replacer import replace_punctuation
from pysbd.processor import Processor
from pysbd.utils import Text, Rule


class Deutsch(Common, Standard):

    iso_code = 'de'

    class Numbers(Common.Numbers):
        # Rubular: http://rubular.com/r/hZxoyQwKT1
        NumberPeriodSpaceRule = Rule(r'(?<=\s\d)\.(?=\s)|(?<=\s\d\d)\.(?=\s)', '∯')

        # Rubular: http://rubular.com/r/ityNMwdghj
        NegativeNumberPeriodSpaceRule = Rule(r'(?<=-\d)\.(?=\s)|(?<=-\d\d)\.(?=\s)', '∯')

        All = Common.Numbers.All + [NumberPeriodSpaceRule, NegativeNumberPeriodSpaceRule]

    class Processor(Processor):

        def __init__(self, text, lang, char_span=False):
            super().__init__(text, lang, char_span)

        def replace_numbers(self):
            self.text = Text(self.text).apply(*self.lang.Numbers.All)
            self.replace_period_in_deutsch_dates()
            return self.text

        def replace_period_in_deutsch_dates(self):
            MONTHS = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August',
                      'September', 'Oktober', 'November', 'Dezember']
            for month in MONTHS:
                # Rubular: http://rubular.com/r/zlqgj7G5dA
                self.text = re.sub(r'(?<=\d)\.(?=\s*{month})'.format(month=month), '∯', self.text)

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ['Ä', 'ä', 'adj', 'adm', 'adv', 'art', 'asst', 'b.a', 'b.s', 'bart', 'bldg', 'brig', 'bros', 'bse', 'buchst', 'bzgl', 'bzw', 'c.-à-d', 'ca', 'capt', 'chr', 'cmdr', 'co', 'col', 'comdr', 'con', 'corp', 'cpl', 'd.h', 'd.j', 'dergl', 'dgl', 'dkr', 'dr ', 'ens', 'etc', 'ev ', 'evtl', 'ff', 'g.g.a', 'g.u', 'gen', 'ggf', 'gov', 'hon', 'hosp', 'i.f', 'i.h.v', 'ii', 'iii', 'insp', 'iv', 'ix', 'jun', 'k.o', 'kath ', 'lfd', 'lt', 'ltd', 'm.e', 'maj', 'med', 'messrs', 'mio', 'mlle', 'mm', 'mme', 'mr', 'mrd', 'mrs', 'ms', 'msgr', 'mwst', 'no', 'nos', 'nr', 'o.ä', 'op', 'ord', 'pfc', 'ph', 'pp', 'prof', 'pvt', 'rep', 'reps', 'res', 'rev', 'rt', 's.p.a', 'sa', 'sen', 'sens', 'sfc', 'sgt', 'sog', 'sogen', 'spp', 'sr', 'st', 'std', 'str  ', 'supt', 'surg', 'u.a  ', 'u.e', 'u.s.w', 'u.u', 'u.ä', 'usf', 'usw', 'v', 'vgl', 'vi', 'vii', 'viii', 'vs', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xix', 'xv', 'xvi', 'xvii', 'xviii', 'xx', 'z.b', 'z.t', 'z.z', 'z.zt', 'zt', 'zzt', 'univ.-prof', 'o.univ.-prof', 'ao.univ.prof', 'ass.prof', 'hon.prof', 'univ.-doz', 'univ.ass', 'stud.ass', 'projektass', 'ass', 'di', 'dipl.-ing', 'mag']
        PREPOSITIVE_ABBREVIATIONS = []
        NUMBER_ABBREVIATIONS = ['art', 'ca', 'no', 'nos', 'nr', 'pp']

    class AbbreviationReplacer(AbbreviationReplacer):

        SENTENCE_STARTERS = ("Am Auch Auf Bei Da Das Der Die Ein Eine Es Für Heute Ich Im In "
          "Ist Jetzt Mein Mit Nach So Und Warum Was Wenn Wer Wie Wir").split(' ')

        def __init__(self, text, lang):
            super().__init__(text, lang)

        def replace(self):
            # Rubular: http://rubular.com/r/B4X33QKIL8
            SingleLowerCaseLetterRule = Rule(r'(?<=\s[a-z])\.(?=\s)', '∯')

            # Rubular: http://rubular.com/r/iUNSkCuso0
            SingleLowerCaseLetterAtStartOfLineRule = Rule(r'(?<=^[a-z])\.(?=\s)', '∯')
            self.text = Text(self.text).apply(
                    self.lang.PossessiveAbbreviationRule,
                    *self.lang.SingleLetterAbbreviationRules.All,
                    SingleLowerCaseLetterRule,
                    SingleLowerCaseLetterAtStartOfLineRule)

            self.text = self.search_for_abbreviations_in_string(self.text)
            self.replace_multi_period_abbreviations()
            self.text = Text(self.text).apply(*self.lang.AmPmRules.All)
            self.text = self.replace_abbreviation_as_sentence_boundary()
            return self.text

        def scan_for_replacements(self, txt, am, index, character_array):
            txt = re.sub(r'(?<={am})\.(?=\s)'.format(am=am), '∯', txt)
            return txt

    class BetweenPunctuation(BetweenPunctuation):

        def __init__(self, text):
            super().__init__(text)

        def sub_punctuation_between_double_quotes(self, txt):
            # Rubular: http://rubular.com/r/OdcXBsub0w
            BETWEEN_UNCONVENTIONAL_DOUBLE_QUOTE_DE_REGEX = r',,(?=(?P<tmp>[^“\\]+|\\{2}|\\.)*)(?P=tmp)“'

            # Rubular: http://rubular.com/r/2UskIupGgP
            # SPLIT_DOUBLE_QUOTES_DE_REGEX = r'\A„(?=(?P<tmp>[^“\\]+|\\{2}|\\.)*)(?P=tmp)“'

            # Rubular: http://rubular.com/r/TkZomF9tTM
            BETWEEN_DOUBLE_QUOTES_DE_REGEX = r'„(?=(?P<tmp>[^“\\]+|\\{2}|\\.)*)(?P=tmp)“'

            if '„' in txt:
                return re.sub(BETWEEN_DOUBLE_QUOTES_DE_REGEX, replace_punctuation, txt)
            elif ',,' in txt:
                return re.sub(BETWEEN_UNCONVENTIONAL_DOUBLE_QUOTE_DE_REGEX,
                              replace_punctuation, txt)
            else:
                return txt
