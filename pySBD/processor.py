# -*- coding: utf-8 -*-
import re
# from pySBD import punctuation_replacer
# from pySBD import between_punctuation
from pySBD.rules import Text
from pySBD.lists_item_replacer import ListItemReplacer
# from pySBD import abbreviation_replacer
# from pySBD import exclamation_words
from pySBD.languages import Language
from pySBD.lang.standard import Standard
from pySBD.lang.common.numbers import Common
from pySBD.lang.common.ellipsis import EllipsisRules
from pySBD.exclamation_words import ExclamationWords
from pySBD.between_punctuation import BetweenPunctuation


class Processor(object):

    def __init__(self, text, language='common'):
        self.language = language
        self.language_module = Language.get_language_code(language)
        self.text = text

    def process(self):
        # text = ListItemReplacer(self.text)
        # text = add_line_break(text)
        # text = replace_abbreviation(text)
        # text = replace_numbers(text)
        # text = replace_continuous_punctuation(text)
        self.text = self.replace_periods_before_numeric_references(self.text)
        # Abbreviations.WithMultiplePeriodsAndEmailRule
        # GeoLocationRule
        # FileFormatRule
        processed = self.split_into_segments()
        return processed

    def split_into_segments(self):
        text = self.check_for_parens_between_quotes(self.text)
        sents = text.split('\r')
        # remove empty and none values
        # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
        sents = list(filter(None, sents))
        # https://stackoverflow.com/questions/4698493/can-i-add-custom-methods-attributes-to-built-in-python-types
        sents = [
            Text(e).apply(Standard.SingleNewLineRule, *EllipsisRules.All)
            for e in sents
        ]
        # SingleNewLineRule
        # EllipsisRules
        # check_for_punctuation
        # SubSymbolsRules
        # post_process_segments
        # SubSingleQuoteRule
        # raise NotImplementedError
        return sents

    def post_process_segments(self, text):
        # consecutive_underscore
        # ReinsertEllipsisRules
        # ExtraWhiteSpaceRule
        # QUOTATION_AT_END_OF_SENTENCE_REGEX
        # SPLIT_SPACE_QUOTATION_AT_END_OF_SENTENCE_REGEX
        raise NotImplementedError

    def check_for_parens_between_quotes(self, txt):
        def paren_replace(match):
            match = match.group()
            sub1 = re.sub(r'\s(?=\()', r'\\r', match)
            sub2 = re.sub(r'(?<=\))\s', r'\\r', sub1)
            return sub2
        # TODO: return Text class inherited from str
        # should have .apply method
        return re.sub(Common.PARENS_BETWEEN_DOUBLE_QUOTES_REGEX,
                      paren_replace, txt)

    def replace_continuous_punctuation(self, txt):
        # CONTINUOUS_PUNCTUATION_REGEX
        raise NotImplementedError

    def replace_periods_before_numeric_references(self, txt):
        # https://github.com/diasks2/pragmatic_segmenter/commit/d9ec1a352aff92b91e2e572c30bb9561eb42c703
        return re.sub(Common.NUMBERED_REFERENCE_REGEX,
                      r"∯\\2\\r\\7", txt)

    def consecutive_underscore(self, txt):
        # Rubular: http://rubular.com/r/fTF2Ff3WBL
        raise NotImplementedError

    def check_for_punctuation(self, txt):
        # if any(re.search(re.escape(r'{}'.format(p)), txt)
        #        for p in Standard.Punctuations):
        if any(p in txt for p in Standard.Punctuations):
            self.process_text(txt)

    def process_text(self, txt):
        if not any(p in txt[-1] for p in Standard.Punctuations):
            txt += 'ȸ'  # "Hello .World" -> "Hello .Worldȸ"
        # work for Yahoo! company -> work for Yahoo&ᓴ& company
        txt = ExclamationWords.apply_rules(txt)
        txt = BetweenPunctuation(text).replace()
        # ExclamationWords
        # between_punctuation
        # DoublePunctuationRules
        # QuestionMarkInQuotationRule
        # ExclamationPointRules
        # replace_parens
        # sentence_boundary_punctuation
        raise NotImplementedError

    def replace_numbers(self, txt):
        # Numbers
        raise NotImplementedError

    def abbreviations_replacer(self, txt):
        # AbbreviationReplacer
        raise NotImplementedError

    def replace_abbreviations(self, txt):
        # abbreviations_replacer
        raise NotImplementedError

    def between_punctuation_processor(self, txt):
        # BetweenPunctuation
        raise NotImplementedError

    def between_punctuation(self, txt):
        # between_punctuation_processor
        raise NotImplementedError

    def sentence_boundary_punctuation(self, txt):
        # ReplaceColonBetweenNumbersRule
        # ReplaceNonSentenceBoundaryCommaRule
        # SENTENCE_BOUNDARY_REGEX
        raise NotImplementedError


if __name__ == "__main__":
    text = "\"Dinah'll miss me very much to-night, I should think!\" (Dinah was the cat.) \"I hope they'll remember her saucer of milk at tea-time. Dinah, my dear, I wish you were down here with me!\""
    print("Input String:\n{}".format(text))
    p = Processor(text)
    print("\nOutput String:\n")
    print(p.check_for_parens_between_quotes(text))
