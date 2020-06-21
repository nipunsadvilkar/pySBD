# -*- coding: utf-8 -*-
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard
from pysbd.processor import Processor
from pysbd.utils import Text, Rule


class Kazakh(Common, Standard):

    iso_code = 'kk'

    # Handling Cyrillic characters in re module
    # https://stackoverflow.com/a/10982308/5462100
    MULTI_PERIOD_ABBREVIATION_REGEX = r'\b[\u0400-\u0500]+(?:\.\s?[\u0400-\u0500])+[.]|b[a-z](?:\.[a-z])+[.]'

    class Processor(Processor):

        def __init__(self, text, lang, char_span=False):
            super().__init__(text, lang, char_span)

        def between_punctuation(self, txt):
            txt = self.between_punctuation_processor(txt).replace()
            # Rubular: http://rubular.com/r/WRWy56Z5zp
            QuestionMarkFollowedByDashLowercaseRule = Rule(r'(?<=)\?(?=\s*[-—]\s*)', '&ᓷ&')
            # Rubular: http://rubular.com/r/lixxP7puSa
            ExclamationMarkFollowedByDashLowercaseRule = Rule(r'(?<=)!(?=\s*[-—]\s*)', '&ᓴ&')

            txt = Text(txt).apply(QuestionMarkFollowedByDashLowercaseRule,
                                  ExclamationMarkFollowedByDashLowercaseRule)
            return txt

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ['afp', 'anp', 'atp', 'bae', 'bg', 'bp', 'cam', 'cctv', 'cd', 'cez', 'cgi', 'cnpc', 'farc', 'fbi', 'eiti', 'epo', 'er', 'gp', 'gps', 'has', 'hiv', 'hrh', 'http', 'icu', 'idf', 'imd', 'ime', 'icu', 'idf', 'ip', 'iso', 'kaz', 'kpo', 'kpa', 'kz', 'kz', 'mri', 'nasa', 'nba', 'nbc', 'nds', 'ohl', 'omlt', 'ppm', 'pda', 'pkk', 'psm', 'psp', 'raf', 'rss', 'rtl', 'sas', 'sme', 'sms', 'tnt', 'udf', 'uefa', 'usb', 'utc', 'x', 'zdf', 'әқбк', 'әқбк', 'аақ', 'авг.', 'aбб', 'аек', 'ак', 'ақ', 'акцион.', 'акср', 'ақш', 'англ', 'аөсшк', 'апр', 'м.', 'а.', 'р.', 'ғ.', 'апр.', 'аум.', 'ацат', 'әч', 'т. б.', 'б. з. б.', 'б. з. б.', 'б. з. д.', 'б. з. д.', 'биікт.', 'б. т.', 'биол.', 'биохим', 'бө', 'б. э. д.', 'бта', 'бұұ', 'вич', 'всоонл', 'геогр.', 'геол.', 'гленкор', 'гэс', 'қк', 'км', 'г', 'млн', 'млрд', 'т', 'ғ. с.', 'ғ.', 'қ.', 'ғ.', 'дек.', 'днқ', 'дсұ', 'еақк', 'еқыұ', 'ембімұнайгаз', 'ео', 'еуразэқ', 'еуроодақ', 'еұу', 'ж.', 'ж.', 'жж.', 'жоо', 'жіө', 'жсдп', 'жшс', 'іім', 'инта', 'исаф', 'камаз', 'кгб', 'кеу', 'кг', 'км²', 'км²', 'км³', 'км³', 'кимеп', 'кср', 'ксро', 'кокп', 'кхдр', 'қазатомпром', 'қазкср', 'қазұу', 'қазмұнайгаз', 'қазпошта', 'қазтаг', 'қазұу', 'қкп', 'қмдб', 'қр', 'қхр', 'лат.', 'м²', 'м²', 'м³', 'м³', 'магатэ', 'май.', 'максам', 'мб', 'мвт', 'мемл', 'м', 'мсоп', 'мтк', 'мыс.', 'наса', 'нато', 'нквд', 'нояб.', 'обл.', 'огпу', 'окт.', 'оңт.', 'опек', 'оеб', 'өзенмұнайгаз', 'өф', 'пәк', 'пед.', 'ркфср', 'рнқ', 'рсфср', 'рф', 'свс', 'сву', 'сду', 'сес', 'сент.', 'см', 'снпс', 'солт.', 'солт.', 'сооно', 'ссро', 'сср', 'ссср', 'ссс', 'сэс', 'дк', 'т. б.', 'т', 'тв', 'тереңд.', 'тех.', 'тжқ', 'тмд', 'төм.', 'трлн', 'тр', 'т.', 'и.', 'м.', 'с.', 'ш.', 'т.', 'т. с. с.', 'тэц', 'уаз', 'уефа', 'еқыұ', 'ұқк', 'ұқшұ', 'февр.', 'фққ', 'фсб', 'хим.', 'хқко', 'шұар', 'шыұ', 'экон.', 'экспо', 'цтп', 'цас', 'янв.', 'dvd', 'жкт', 'ққс', 'км', 'ацат', 'юнеско', 'ббс', 'mgm', 'жск', 'зоо', 'бсн', 'өұқ', 'оар', 'боак', 'эөкк', 'хтқо', 'әөк', 'жэк', 'хдо', 'спбму', 'аф', 'сбд', 'амт', 'гсдп', 'гсбп', 'эыдұ', 'нұсжп', 'шыұ', 'жтсх', 'хдп', 'эқк', 'фкққ', 'пиқ', 'өгк', 'мбф', 'маж', 'кота', 'тж', 'ук', 'обб', 'сбл', 'жхл', 'кмс', 'бмтрк', 'жққ', 'бхооо', 'мқо', 'ржмб', 'гулаг', 'жко', 'еэы', 'еаэы', 'кхдр', 'рфкп', 'рлдп', 'хвқ', 'мр', 'мт', 'кту', 'ртж', 'тим', 'мемдум', 'ксро', 'т.с.с', 'с.ш.', 'ш.б.', 'б.б.', 'руб', 'мин', 'акад.', 'ғ.', 'мм', 'мм.']
        PREPOSITIVE_ABBREVIATIONS = []
        NUMBER_ABBREVIATIONS = []

    class AbbreviationReplacer(AbbreviationReplacer):

        SENTENCE_STARTERS = []

        def __init__(self, text, lang):
            super().__init__(text, lang)

        def replace(self):
            SingleUpperCaseCyrillicLetterAtStartOfLineRule = Rule(r'(?<=^[А-ЯЁ])\.(?=\s)', '∯')
            SingleUpperCaseCyrillicLetterRule = Rule(r'(?<=\s[А-ЯЁ])\.(?=\s)', '∯')
            self.text = Text(self.text).apply(SingleUpperCaseCyrillicLetterAtStartOfLineRule,
                                              SingleUpperCaseCyrillicLetterRule)
            self.replace_multi_period_abbreviations()
            return self.text
