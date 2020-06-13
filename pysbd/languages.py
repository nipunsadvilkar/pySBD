# -*- coding: utf-8 -*-
from pysbd.lang.english import English
from pysbd.lang.hindi import Hindi
from pysbd.lang.marathi import Marathi
from pysbd.lang.chinese import Chinese
from pysbd.lang.spanish import Spanish
from pysbd.lang.amharic import Amharic
from pysbd.lang.arabic import Arabic
from pysbd.lang.armenian import Armenian
from pysbd.lang.bulgarian import Bulgarian

LANGUAGE_CODES = {
    'en': English,
    'hi': Hindi,
    'mr': Marathi,
    'zh': Chinese,
    'es': Spanish,
    'am': Amharic,
    'ar': Arabic,
    'hy': Armenian,
    'bg': Bulgarian
}


class Language(object):

    def __init__(self, code):
        self.code = code

    @classmethod
    def get_language_code(cls, code):
        try:
            return LANGUAGE_CODES[code]
        except KeyError:
            raise ValueError("Provide valid language ID i.e. ISO code. "
                "Available codes are : {}".format(set(LANGUAGE_CODES.keys())))
