from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class Bangla(Common, Standard):

    iso_code = 'bn'

    SENTENCE_BOUNDARY_REGEX = r'.*?[।\|!\?]|.*?$'
    Punctuations = ['।', '|', '.', '!', '?']

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []