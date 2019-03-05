#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pySBD import punctuation_replacer
from pySBD import between_punctuation
from pySBD import lists
from pySBD import abbreviation_replacer
from pySBD import exclamation_words


class Processor(object):

    def __init__(self, language, text):
        self.language = language
        self.text = text

    def process(self, text):
        text = add_line_break(text)
        text = replace_abbreviation(text)
        text = replace_numbers(text)
        text = replace_continuous_punctuation(text)
        text = replace_periods_before_numeric_references(text)
        # Abbreviations.WithMultiplePeriodsAndEmailRule
        # GeoLocationRule
        # FileFormatRule
        # split_into_segments
        return text

    def split_into_segments(self, text):
        # check_for_parens_between_quotes
        # SingleNewLineRule
        # EllipsisRules
        # check_for_punctuation
        # SubSymbolsRules
        # post_process_segments
        # SubSingleQuoteRule
        raise NotImplementedError

    def post_process_segments(self, text):
        # consecutive_underscore
        # ReinsertEllipsisRules
        # ExtraWhiteSpaceRule
        # QUOTATION_AT_END_OF_SENTENCE_REGEX
        # SPLIT_SPACE_QUOTATION_AT_END_OF_SENTENCE_REGEX
        raise NotImplementedError

    def check_for_parens_between_quotes(self, txt):
        # PARENS_BETWEEN_DOUBLE_QUOTES_REGEX
        # PARENS_BETWEEN_DOUBLE_QUOTES_REGEX
        raise NotImplementedError

    def replace_continuous_punctuation(self, txt):
        # CONTINUOUS_PUNCTUATION_REGEX
        raise NotImplementedError

    def replace_periods_before_numeric_references(self, txt):
        # NUMBERED_REFERENCE_REGEX
        raise NotImplementedError

    def consecutive_underscore(self, txt):
        # Rubular: http://rubular.com/r/fTF2Ff3WBL
        raise NotImplementedError

    def check_for_punctuation(self, txt):
        # Punctuations
        # process_text
        raise NotImplementedError

    def process_text(self, txt):
        # Punctuations
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
