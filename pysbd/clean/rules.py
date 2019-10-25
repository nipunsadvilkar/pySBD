# -*- coding: utf-8 -*-
from pysbd.utils import Rule


class CleanRules(object):

    # NOTE: Caution: Might require \\ for special characters
    # if regex is defined with r'' then dont
    # add extra \\ for special characters
    # Rubular: http://rubular.com/r/V57WnM9Zut
    NewLineInMiddleOfWordRule = Rule(r'\n(?=[a-zA-Z]{1,2}\n)', '')

    # Rubular: http://rubular.com/r/dMxp5MixFS
    DoubleNewLineWithSpaceRule = Rule(r'\n \n', "\r")

    # Rubular: http://rubular.com/r/H6HOJeA8bq
    DoubleNewLineRule = Rule(r'\n\n', "\r")

    # Rubular: http://rubular.com/r/FseyMiiYFT
    NewLineFollowedByPeriodRule = Rule(r'\n(?=\.(\s|\n))', '')

    ReplaceNewlineWithCarriageReturnRule = Rule(r'\n', "\r")

    EscapedNewLineRule = Rule(r'\\n', "\n")

    EscapedCarriageReturnRule = Rule(r'\\r', "\r")

    TypoEscapedNewLineRule = Rule(r'\\\ n', "\n")

    TypoEscapedCarriageReturnRule = Rule(r'\\\ r', "\r")

    # Rubular: http://rubular.com/r/bAJrhyLNeZ
    InlineFormattingRule = Rule(r'{b\^&gt;\d*&lt;b\^}|{b\^>\d*<b\^}', '')

    # Rubular: http://rubular.com/r/8mc1ArOIGy
    TableOfContentsRule = Rule(r'\.{4,}\s*\d+-*\d*', "\r")

    # Rubular: http://rubular.com/r/DwNSuZrNtk
    ConsecutivePeriodsRule = Rule(r'\.{5,}', ' ')

    # Rubular: http://rubular.com/r/IQ4TPfsbd8
    ConsecutiveForwardSlashRule = Rule(r'\/{3}', '')

    # Rubular: http://rubular.com/r/6dt98uI76u
    NO_SPACE_BETWEEN_SENTENCES_REGEX = r'(?<=[a-z])\.(?=[A-Z])'
    # NO_SPACE_BETWEEN_SENTENCES_REGEX = r'[a-z]\.[A-Z]'
    NoSpaceBetweenSentencesRule = Rule(NO_SPACE_BETWEEN_SENTENCES_REGEX, '. ')

    # Rubular: http://rubular.com/r/l6KN6rH5XE
    NO_SPACE_BETWEEN_SENTENCES_DIGIT_REGEX = r'(?<=\d)\.(?=[A-Z])'
    NoSpaceBetweenSentencesDigitRule = Rule(NO_SPACE_BETWEEN_SENTENCES_DIGIT_REGEX, '. ')

    URL_EMAIL_KEYWORDS = ['@', 'http', '.com', 'net', 'www', '//']

    # Rubular: http://rubular.com/r/3GiRiP2IbD
    NEWLINE_IN_MIDDLE_OF_SENTENCE_REGEX = r'(?<=\s)\n(?=([a-z]|\())'

    # Rubular: http://rubular.com/r/Gn18aAnLdZ
    NewLineFollowedByBulletRule = Rule(r"\n(?=•')", "\r")

    QuotationsFirstRule = Rule(r"''", '"')
    QuotationsSecondRule = Rule(r'``', '"')


class HTML(object):
    # Rubular: http://rubular.com/r/9d0OVOEJWj
    HTMLTagRule = Rule(r"<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[\^'\">\s]+))?)+\s*|\s*)\/?>", '')

    # Rubular: http://rubular.com/r/XZVqMPJhea
    EscapedHTMLTagRule = Rule(r'&lt;\/?[^gt;]*gt;', '')

    All = [HTMLTagRule, EscapedHTMLTagRule]


class PDF(object):
    # Rubular: http://rubular.com/r/UZAVcwqck8
    NewLineInMiddleOfSentenceRule = Rule(r'(?<=[^\n]\s)\n(?=\S)', '')

    # Rubular: http://rubular.com/r/eaNwGavmdo
    NewLineInMiddleOfSentenceNoSpacesRule = Rule(r"\n(?=[a-z])", ' ')
