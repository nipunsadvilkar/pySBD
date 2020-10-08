# -*- coding: utf-8 -*-
import re
from pysbd.utils import Rule

class Common(object):

    # added special case: r"[。．.！!? ]{2,}" to handle intermittent dots, exclamation, etc.
    # r"[。．.！!?] at end to handle single instances of these symbol inputs
    SENTENCE_BOUNDARY_REGEX = r"（(?:[^）])*）(?=\s?[A-Z])|「(?:[^」])*」(?=\s[A-Z])|\((?:[^\)]){2,}\)(?=\s[A-Z])|\'(?:[^\'])*[^,]\'(?=\s[A-Z])|\"(?:[^\"])*[^,]\"(?=\s[A-Z])|\“(?:[^\”])*[^,]\”(?=\s[A-Z])|[。．.！!?？ ]{2,}|\S.*?[。．.！!?？ȸȹ☉☈☇☄]|[。．.！!?？]"

    # # Rubular: http://rubular.com/r/NqCqv372Ix
    QUOTATION_AT_END_OF_SENTENCE_REGEX = r'[!?\.-][\"\'“”]\s{1}[A-Z]'

    # # Rubular: http://rubular.com/r/6flGnUMEVl
    PARENS_BETWEEN_DOUBLE_QUOTES_REGEX = r'["\”]\s\(.*\)\s["\“]'

    # # Rubular: http://rubular.com/r/TYzr4qOW1Q
    # BETWEEN_DOUBLE_QUOTES_REGEX = / "(?:[^"])*[^, ]"|“(?: [ ^”])*[^, ]”/

    # # Rubular: http://rubular.com/r/JMjlZHAT4g
    SPLIT_SPACE_QUOTATION_AT_END_OF_SENTENCE_REGEX = r'(?<=[!?\.-][\"\'“”])\s{1}(?=[A-Z])'

    # # Rubular: http://rubular.com/r/mQ8Es9bxtk
    CONTINUOUS_PUNCTUATION_REGEX = r'(?<=\S)(!|\?){3,}(?=(\s|\Z|$))'

    # https://rubular.com/r/UkumQaILKbkeyc
    # https://github.com/diasks2/pragmatic_segmenter/commit/d9ec1a352aff92b91e2e572c30bb9561eb42c703
    NUMBERED_REFERENCE_REGEX = r'(?<=[^\d\s])(\.|∯)((\[(\d{1,3},?\s?-?\s?)*\b\d{1,3}\])+|((\d{1,3}\s?)?\d{1,3}))(\s)(?=[A-Z])'

    # # Rubular: http://rubular.com/r/yqa4Rit8EY
    PossessiveAbbreviationRule = Rule(r"\.(?='s\s)|\.(?='s$)|\.(?='s\Z)", '∯')

    # # Rubular: http://rubular.com/r/NEv265G2X2
    KommanditgesellschaftRule = Rule(r'(?<=Co)\.(?=\sKG)', '∯')

    # # Rubular: http://rubular.com/r/xDkpFZ0EgH
    MULTI_PERIOD_ABBREVIATION_REGEX = r"\b[a-z](?:\.[a-z])+[.]"

    class SingleLetterAbbreviationRules(object):
        """Searches for periods within an abbreviation and
        replaces the periods.
        """
        # Rubular: http://rubular.com/r/e3H6kwnr6H
        SingleUpperCaseLetterAtStartOfLineRule = Rule(r"(?<=^[A-Z])\.(?=\s)", '∯')

        # Rubular: http://rubular.com/r/gitvf0YWH4
        SingleUpperCaseLetterRule = Rule(r"(?<=\s[A-Z])\.(?=,?\s)", '∯')

        All = [
            SingleUpperCaseLetterAtStartOfLineRule, SingleUpperCaseLetterRule
        ]

    class AmPmRules(object):

        # Rubular: http://rubular.com/r/Vnx3m4Spc8
        UpperCasePmRule = Rule(r'(?<= P∯M)∯(?=\s[A-Z])', '.')

        # Rubular: http://rubular.com/r/AJMCotJVbW
        UpperCaseAmRule = Rule(r'(?<=A∯M)∯(?=\s[A-Z])', '.')

        # Rubular: http://rubular.com/r/13q7SnOhgA
        LowerCasePmRule = Rule(r'(?<=p∯m)∯(?=\s[A-Z])', '.')

        # Rubular: http://rubular.com/r/DgUDq4mLz5
        LowerCaseAmRule = Rule(r'(?<=a∯m)∯(?=\s[A-Z])', '.')

        All = [UpperCasePmRule, UpperCaseAmRule, LowerCasePmRule, LowerCaseAmRule]

    class Numbers(object):
        # Rubular: http://rubular.com/r/oNyxBOqbyy
        PeriodBeforeNumberRule = Rule(r'\.(?=\d)', '∯')

        # Rubular: http://rubular.com/r/EMk5MpiUzt
        NumberAfterPeriodBeforeLetterRule = Rule(r'(?<=\d)\.(?=\S)', '∯')

        # Rubular: http://rubular.com/r/rf4l1HjtjG
        NewLineNumberPeriodSpaceLetterRule = Rule(r'(?<=\r\d)\.(?=(\s\S)|\))', '∯')

        # Rubular: http://rubular.com/r/HPa4sdc6b9
        StartLineNumberPeriodRule = Rule(r'(?<=^\d)\.(?=(\s\S)|\))', '∯')

        # Rubular: http://rubular.com/r/NuvWnKleFl
        StartLineTwoDigitNumberPeriodRule = Rule(r'(?<=^\d\d)\.(?=(\s\S)|\))', '∯')

        All = [
            PeriodBeforeNumberRule,
            NumberAfterPeriodBeforeLetterRule,
            NewLineNumberPeriodSpaceLetterRule,
            StartLineNumberPeriodRule,
            StartLineTwoDigitNumberPeriodRule
            ]
