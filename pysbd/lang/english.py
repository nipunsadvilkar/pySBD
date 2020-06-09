# -*- coding: utf-8 -*-
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class English(Common, Standard):

    iso_code = 'en'

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = "A Being Did For He How However I In It Millions "\
            "More She That The There They We What When Where Who Why".split(" ")
