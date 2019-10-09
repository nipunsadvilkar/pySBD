# -*- coding: utf-8 -*-
from pysbd.lang.standard import Standard
from pysbd.lang.english import English

LANGUAGE_CODES = {'en': English}


class Language(object):

    def __init__(self, code):
        self.code = LANGUAGE_CODES[code]

    @classmethod
    def get_language_code(self, code):
        try:
            return LANGUAGE_CODES[code]
        except KeyError:
            return Standard


if __name__ == "__main__":
    print(Language.get_language_code('standard'))
