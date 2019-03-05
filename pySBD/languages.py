# -*- coding: utf-8 -*-
from pySBD.lang.english import English

LANGUAGE_CODES = {'en': English}


class Language(object):

    def __init__(self, code):
        self.code = LANGUAGE_CODES[code]

    def get_language_code(code):
        return LANGUAGE_CODES[code]
