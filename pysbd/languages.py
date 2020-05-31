# -*- coding: utf-8 -*-
from pysbd.lang.english import English
from pysbd.lang.hindi import Hindi

LANGUAGE_CODES = {'en': English, 'hi': Hindi}


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

if __name__ == "__main__":
    print(Language.get_language_code('standard'))
