# -*- coding: utf-8 -*-
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common.numbers import Common
from pysbd.lang.standard import Standard

class English(Common, Standard):

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = "A Being Did For He How However I In It Millions More She That The There They We What When Where Who Why".split(" ")

# class EnAbbreviationReplacer(AbbreviationReplacer):
#     raise NotImplementedError


if __name__ == "__main__":
    en = English()
    print(hasattr(en, 'AbbreviationReplacer'))
