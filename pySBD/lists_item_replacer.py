# -*- coding: utf-8 -*-
import string
import re
from pySBD.rules import Text


class ListItemReplacer(object):

    ROMAN_NUMERALS = "i ii iii iv v vi vii viii ix x xi xii xiii xiv x xi xii xiii xv xvi xvii xviii xix xx".split(' ')
    LATIN_NUMERALS = list(string.ascii_lowercase)

    # Rubular: http://rubular.com/r/XcpaJKH0sz
    ALPHABETICAL_LIST_WITH_PERIODS = r'(?<= ^)[a-z](?=\.) | (?<=\A)[a-z](?=\.) | (?<=\s)[a-z](?=\.)'

    # Rubular: http://rubular.com/r/Gu5rQapywf
    # TODO: Make sure below regex call is case-insensitive
    ALPHABETICAL_LIST_WITH_PARENS = r'(?<=\()[a-z]+(?=\))|(?<=^)[a-z]+(?=\))|(?<=\A)[a-z]+(?=\))|(?<=\s)[a-z]+(?=\))'

    # (pattern, replacement)
    SubstituteListPeriodRule = ('♨', '∯')
    ListMarkerRule = ('☝', '')

    # Rubular: https://regex101.com/r/62YBlv/1
    SpaceBetweenListItemsFirstRule = (r'(?<=\S\S)\s(?=\S\s*\d+♨)', "\r")

    # Rubular: http://rubular.com/r/AizHXC6HxK
    SpaceBetweenListItemsSecondRule = (r'(?<=\S\S)\s(?=\d{1,2}♨)', "\r")

    # Rubular: http://rubular.com/r/GE5q6yID2j
    SpaceBetweenListItemsThirdRule = (r'(?<=\S\S)\s(?=\d{1,2}☝)', "\r")

    # 1. abcd
    # 2. xyz
    NUMBERED_LIST_REGEX_1 = r'\s\d{1,2}(?=\.\s)|^\d{1,2}(?=\.\s)|\s\d{1,2}(?=\.\))|^\d{1,2}(?=\.\))|(?<=\s\-)\d{1,2}(?=\.\s)|(?<=^\-)\d{1,2}(?=\.\s)|(?<=\s\⁃)\d{1,2}(?=\.\s)|(?<=^\⁃)\d{1,2}(?=\.\s)|(?<=s\-)\d{1,2}(?=\.\))|(?<=^\-)\d{1,2}(?=\.\))|(?<=\s\⁃)\d{1,2}(?=\.\))|(?<=^\⁃)\d{1,2}(?=\.\))'

    NUMBERED_LIST_REGEX_2 = r'(?<=\s)\d{1,2}\.(?=\s)|^\d{1,2}\.(?=\s)|(?<=\s)\d{1,2}\.(?=\))|^\d{1,2}\.(?=\))|(?<=\s\-)\d{1,2}\.(?=\s)|(?<=^\-)\d{1,2}\.(?=\s)|(?<=\s\⁃)\d{1,2}\.(?=\s)|(?<=^\⁃)\d{1,2}\.(?=\s)|(?<=\s\-)\d{1,2}\.(?=\))|(?<=^\-)\d{1,2}\.(?=\))|(?<=\s\⁃)\d{1,2}\.(?=\))|(?<=^\⁃)\d{1,2}\.(?=\))'
    NUMBERED_LIST_PARENS_REGEX = r'\d{1,2}(?=\)\s)'

    # Rubular: http://rubular.com/r/NsNFSqrNvJ
    # TODO: Make sure below regex call is case-insensitive
    EXTRACT_ALPHABETICAL_LIST_LETTERS_REGEX = r'\([a-z]+(?=\))|(?<=^)[a-z]+(?=\))|(?<=\A)[a-z]+(?=\))|(?<=\s)[a-z]+(?=\))'

    # Rubular: http://rubular.com/r/wMpnVedEIb
    # TODO: Make sure below regex call is case-insensitive
    ALPHABETICAL_LIST_LETTERS_AND_PERIODS_REGEX = r'(?<=^)[a-z]\.|(?<=\A)[a-z]\.|(?<=\s)[a-z]\.'

    # Rubular: http://rubular.com/r/GcnmQt4a3I
    ROMAN_NUMERALS_IN_PARENTHESES = r'\(((?=[mdclxvi])m*(c[md]|d?c*)(x[cl]|l?x*)(i[xv]|v?i*))\)(?=\s[A-Z])'

    def __init__(self, text):
        self.text = Text(text)

    @classmethod
    def add_line_break(self, text):
        text = self.format_alphabetical_lists(text)
        text = self.format_roman_numeral_lists(text)
        text = self.format_numbered_list_with_periods(text)
        text = self.format_numbered_list_with_parens(text)
        return text

    # def replace_parens(self):
    #     text = re.sub(self.ROMAN_NUMERALS_IN_PARENTHESES, '&✂&\1&⌬&', self.text)
    #     return text

    # def format_numbered_list_with_parens(self):
    #     # replace_parens_in_numbered_list
    #     # add_line_breaks_for_numbered_list_with_parens
    #     self.text = re.sub(self.ROMAN_NUMERALS_IN_PARENTHESES,
    #                   '&✂&\1&⌬&', self.text)
    #     return self.text

    def format_alphabetical_lists(self):
        self.add_line_breaks_for_alphabetical_list_with_periods(
            roman_numeral=False)
        self.add_line_breaks_for_alphabetical_list_with_parens(
            roman_numeral=False)

    def format_roman_numeral_lists(self):
        self.add_line_breaks_for_alphabetical_list_with_periods(
            roman_numeral=True)
        self.add_line_breaks_for_alphabetical_list_with_parens(
            roman_numeral=True)

    def add_line_breaks_for_alphabetical_list_with_periods(self, roman_numeral=False):
        pass
        # iterate_alphabet_array(ALPHABETICAL_LIST_WITH_PERIODS, roman_numeral: roman_numeral)
    # def replace_periods_in_numbered_list(self):
    #     self.scan_lists(self.NUMBERED_LIST_REGEX_1,
    #                     self.NUMBERED_LIST_REGEX_2, '♨', strip=True)


    # def add_line_breaks_for_numbered_list_with_periods(self):
    #     if @text.include?('♨') & & @text !~ /♨.+\n.+♨|♨.+\r.+♨/ & & @text !~ / for\s\d{1, 2}♨\s[a-z]/
    #     self.text.apply(SpaceBetweenListItemsFirstRule,
    #                     SpaceBetweenListItemsSecondRule)

    # def replace_parens_in_numbered_list
    # scan_lists(
    #     NUMBERED_LIST_PARENS_REGEX, NUMBERED_LIST_PARENS_REGEX, '☝')
    # scan_lists(NUMBERED_LIST_PARENS_REGEX, NUMBERED_LIST_PARENS_REGEX, '☝')
    # end

    # def add_line_breaks_for_numbered_list_with_parens
    # if @text.include?('☝') & & @text !~ /☝.+\n.+☝|☝.+\r.+☝/

    # @text.apply(SpaceBetweenListItemsThirdRule)
