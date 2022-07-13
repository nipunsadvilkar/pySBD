from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard


class Telugu(Common, Standard):
    SENTENCE_BOUNDARY_REGEX = r'.*?[.!?]|.*?$'  # need to make changes here
    Punctuations = ['.', '!', '?']              # need to make changes here

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []