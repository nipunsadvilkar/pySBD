# -*- coding: utf-8 -*-
import re
import os
# from pySBD import punctuation_replacer
# from pySBD import between_punctuation
from pySBD.rules import Text
from pySBD.lists_item_replacer import ListItemReplacer
# from pySBD import abbreviation_replacer
# from pySBD import exclamation_words
from pySBD.languages import Language
from pySBD.lang.standard import (Standard, DoublePunctuationRules,
                                 ExclamationPointRules, SubSymbolsRules,
                                 ReinsertEllipsisRules)
from pySBD.lang.common.numbers import Common
from pySBD.lang.common.ellipsis import EllipsisRules
from pySBD.exclamation_words import ExclamationWords
from pySBD.between_punctuation import BetweenPunctuation
from pySBD.abbreviation_replacer import AbbreviationReplacer

# os.linesep = '\r'


class Processor(object):

    def __init__(self, text, language='common'):
        self.language = language
        self.language_module = Language.get_language_code(language)
        self.text = text

    def process(self):
        if not self.text:
            return self.text
        li = ListItemReplacer(self.text)
        self.text = li.add_line_break()
        # print(self.text)
        self.text = AbbreviationReplacer(self.text).replace()
        # print(self.text)
        # print(repr(self.text))
        # self.text = self.text.replace('\r', '\r')
        # text = replace_abbreviation(text)
        # text = replace_numbers(text)
        # text = replace_continuous_punctuation(text)
        # Abbreviations.WithMultiplePeriodsAndEmailRule
        # GeoLocationRule
        # FileFormatRule
        self.replace_periods_before_numeric_references()
        processed = self.split_into_segments()
        return processed

    def split_into_segments(self):
        self.check_for_parens_between_quotes(self.text)
        # print(repr(self.text))
        sents = self.text.split('\r')
        # remove empty and none values
        # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
        sents = list(filter(None, sents))
        # print(sents)
        # https://stackoverflow.com/questions/4698493/can-i-add-custom-methods-attributes-to-built-in-python-types
        sents = [
            Text(s).apply(Standard.SingleNewLineRule, *EllipsisRules.All)
            for s in sents
        ]
        new_sents = [self.check_for_punctuation(s) for s in sents]
        # flatten list of list of sentences
        if any(isinstance(s, list) for s in new_sents):
            new_sents = [s for sents in new_sents for s in sents]

        sents = [
            Text(s).apply(*SubSymbolsRules.All)
            for s in new_sents
        ]
        post_process_sents = [self.post_process_segments(s) for s in sents]
        # remove any empty or null values
        sents = [s for s in post_process_sents if s]
        sents = [
            Text(s).apply(Standard.SubSingleQuoteRule)
            for s in sents
        ]
        return sents

    def post_process_segments(self, txt):
        if len(txt) > 2 and re.search(r'\A[a-zA-Z]*\Z', txt):
            return txt
        if self.consecutive_underscore(txt) or len(txt) < 2:
            txt = Text(txt).apply(*ReinsertEllipsisRules.All,
                                  Standard.ExtraWhiteSpaceRule)
            return txt

        if re.search(Common.QUOTATION_AT_END_OF_SENTENCE_REGEX, txt):
            txt = re.split(
                Common.SPLIT_SPACE_QUOTATION_AT_END_OF_SENTENCE_REGEX, txt)
            return txt
        else:
            txt = txt.replace('\n', '')
            return txt.strip()

    def check_for_parens_between_quotes(self, txt):
        def paren_replace(match):
            match = match.group()
            sub1 = re.sub(r'\s(?=\()', r'\r', match)
            sub2 = re.sub(r'(?<=\))\s', r'\r', sub1)
            return sub2
        # TODO: return Text class inherited from str
        # should have .apply method
        return re.sub(Common.PARENS_BETWEEN_DOUBLE_QUOTES_REGEX,
                      paren_replace, txt)

    def replace_continuous_punctuation(self, txt):
        # CONTINUOUS_PUNCTUATION_REGEX
        raise NotImplementedError

    def replace_periods_before_numeric_references(self):
        # https://github.com/diasks2/pragmatic_segmenter/commit/d9ec1a352aff92b91e2e572c30bb9561eb42c703
        return re.sub(Common.NUMBERED_REFERENCE_REGEX,
                      r"∯\\2\r\\7", self.text)

    def consecutive_underscore(self, txt):
        # Rubular: http://rubular.com/r/fTF2Ff3WBL
        txt = re.sub(r'_{3,}', '', txt)
        return len(txt) == 0

    def check_for_punctuation(self, txt):
        # if any(re.search(re.escape(r'{}'.format(p)), txt)
        #        for p in Standard.Punctuations):
        if any(p in txt for p in Standard.Punctuations):
            sents = self.process_text(txt)
            return sents
        else:
            return txt

    def process_text(self, txt):
        # if not any(p in txt[-1] for p in Standard.Punctuations):
        if txt[-1] not in Standard.Punctuations:
            # "Hello .World" -> "Hello .Worldȸ"
            txt += 'ȸ'
        # work for Yahoo! company -> work for Yahoo&ᓴ& company
        txt = ExclamationWords.apply_rules(txt)
        txt = BetweenPunctuation(txt).replace()
        txt = Text(txt).apply(*DoublePunctuationRules.All,
                              Standard.QuestionMarkInQuotationRule,
                              *ExclamationPointRules.All)
        txt = ListItemReplacer(txt).replace_parens()
        txt = self.sentence_boundary_punctuation(txt)
        return txt

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
        if hasattr(self.language_module, 'ReplaceColonBetweenNumbersRule'):
            txt = Text(txt).apply(
                self.language_module.ReplaceColonBetweenNumbersRule)
        if hasattr(self.language_module, 'ReplaceNonSentenceBoundaryCommaRule'):
            txt = Text(txt).apply(
                self.language_module.ReplaceNonSentenceBoundaryCommaRule)
        txt = re.findall(Common.SENTENCE_BOUNDARY_REGEX, txt)
        return txt


if __name__ == "__main__":
    # text = "\"Dinah'll miss me very much to-night, I should think!\" (Dinah was the cat.) \"I hope they'll remember her saucer of milk at tea-time. Dinah, my dear, I wish you were down here with me!\""
    # text = "My name is Jonas E. Smith."
    # text = "1) The first item 2) The second item"
    # text = 'What is your name? My name is Jonas.'
    text = "Please turn to p. 55."
    print("Input String:\n{}".format(text))
    p = Processor(text)
    processed_op = p.process()
    print("\nProcessed String:\n")
    print("Number of sentences: {}\n".format(len(processed_op)))
    print(processed_op)
    for e in processed_op:
        print(e)
# output after check_for_punctuation
# "\"Dinah&⎋&ll miss me very much to-night, I should think&ᓴ&\"ȸ"
# "(Dinah was the cat∯)ȸ"
# "\"I hope they&⎋&ll remember her saucer of milk at tea-time∯ Dinah, my dear, I wish you were down here with me&ᓴ&\"ȸ"

# After SubSymbolsRules.all
# "\"Dinah&⎋&ll miss me very much to-night, I should think!\""
# "(Dinah was the cat.)"
# "\"I hope they&⎋&ll remember her saucer of milk at tea-time. Dinah, my dear, I wish you were down here with me!\""
