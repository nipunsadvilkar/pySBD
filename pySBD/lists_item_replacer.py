# -*- coding: utf-8 -*-
import string
import re
from pySBD.rules import Rule
from functools import partial


class ListItemReplacer(object):

    ROMAN_NUMERALS = "i ii iii iv v vi vii viii ix x xi xii xiii xiv x xi xii xiii xv xvi xvii xviii xix xx".split(' ')
    LATIN_NUMERALS = list(string.ascii_lowercase)

    # Rubular: http://rubular.com/r/XcpaJKH0sz
    ALPHABETICAL_LIST_WITH_PERIODS = r'(?<=^)[a-z](?=\.)|(?<=\A)[a-z](?=\.)|(?<=\s)[a-z](?=\.)'

    # Rubular: http://rubular.com/r/Gu5rQapywf
    # TODO: Make sure below regex call is case-insensitive
    ALPHABETICAL_LIST_WITH_PARENS = r'(?<=\()[a-z]+(?=\))|(?<=^)[a-z]+(?=\))|(?<=\A)[a-z]+(?=\))|(?<=\s)[a-z]+(?=\))'

    # (pattern, replacement)
    SubstituteListPeriodRule = Rule('♨', '∯')
    ListMarkerRule = Rule('☝', '')

    # Rubular: http://rubular.com/r/Wv4qLdoPx7
    # https://regex101.com/r/62YBlv/1
    SpaceBetweenListItemsFirstRule = Rule(r'(?<=\S\S)\s(?=\S\s*\d+♨)', "\r")

    # Rubular: http://rubular.com/r/AizHXC6HxK
    # https://regex101.com/r/62YBlv/2
    SpaceBetweenListItemsSecondRule = Rule(r'(?<=\S\S)\s(?=\d{1,2}♨)', "\r")

    # Rubular: http://rubular.com/r/GE5q6yID2j
    # https://regex101.com/r/62YBlv/3
    SpaceBetweenListItemsThirdRule = Rule(r'(?<=\S\S)\s(?=\d{1,2}☝)', "\r")


    NUMBERED_LIST_REGEX_1 = r'\s\d{1,2}(?=\.\s)|^\d{1,2}(?=\.\s)|\s\d{1,2}(?=\.\))|^\d{1,2}(?=\.\))|(?<=\s\-)\d{1,2}(?=\.\s)|(?<=^\-)\d{1,2}(?=\.\s)|(?<=\s\⁃)\d{1,2}(?=\.\s)|(?<=^\⁃)\d{1,2}(?=\.\s)|(?<=s\-)\d{1,2}(?=\.\))|(?<=^\-)\d{1,2}(?=\.\))|(?<=\s\⁃)\d{1,2}(?=\.\))|(?<=^\⁃)\d{1,2}(?=\.\))'
    # 1. abcd
    # 2. xyz
    NUMBERED_LIST_REGEX_2 = r'(?<=\s)\d{1,2}\.(?=\s)|^\d{1,2}\.(?=\s)|(?<=\s)\d{1,2}\.(?=\))|^\d{1,2}\.(?=\))|(?<=\s\-)\d{1,2}\.(?=\s)|(?<=^\-)\d{1,2}\.(?=\s)|(?<=\s\⁃)\d{1,2}\.(?=\s)|(?<=^\⁃)\d{1,2}\.(?=\s)|(?<=\s\-)\d{1,2}\.(?=\))|(?<=^\-)\d{1,2}\.(?=\))|(?<=\s\⁃)\d{1,2}\.(?=\))|(?<=^\⁃)\d{1,2}\.(?=\))'
    # 1) abcd
    # 2) xyz
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
        self.text = text

    def add_line_break(self):
        text = self.format_alphabetical_lists(self.text)
        text = self.format_roman_numeral_lists(text)
        text = self.format_numbered_list_with_periods(text)
        text = self.format_numbered_list_with_parens(text)
        return text

    def replace_parens(self):
        text = re.sub(self.ROMAN_NUMERALS_IN_PARENTHESES,
                      r'&✂&\1&⌬&', self.text)
        return text

    # def format_numbered_list_with_parens(self):
    #     # replace_parens_in_numbered_list
    #     # add_line_breaks_for_numbered_list_with_parens
    #     self.text = re.sub(self.ROMAN_NUMERALS_IN_PARENTHESES,
    #                   '&✂&\1&⌬&', self.text)
    #     return self.text

    def format_alphabetical_lists(self):
        self.txt = self.add_line_breaks_for_alphabetical_list_with_periods(
            roman_numeral=False)
        self.txt = self.add_line_breaks_for_alphabetical_list_with_parens(
            roman_numeral=False)
        return self.txt

    def format_roman_numeral_lists(self):
        self.txt = self.add_line_breaks_for_alphabetical_list_with_periods(
            roman_numeral=True)
        self.txt = self.add_line_breaks_for_alphabetical_list_with_parens(
            roman_numeral=True)
        return self.txt

    def add_line_breaks_for_alphabetical_list_with_periods(
            self, roman_numeral=False):
        txt = self.iterate_alphabet_array(
            self.ALPHABETICAL_LIST_WITH_PERIODS,
            roman_numeral=roman_numeral)
        return txt

    def add_line_breaks_for_alphabetical_list_with_parens(self, roman_numeral=False):
        txt = self.iterate_alphabet_array(
            self.ALPHABETICAL_LIST_WITH_PARENS,
            parens=True,
            roman_numeral=roman_numeral)
        return txt

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
    def replace_alphabet_list(self, a):
        """
        Input: 'a. ffegnog b. fgegkl c.'
        Output: \ra∯ ffegnog \rb∯ fgegkl \rc∯
        """

        def replace_letter_period(match, val=None):
            match = match.group()
            match_wo_period = match.strip('.')
            if match_wo_period == val:
                return '\\r{}∯'.format(match_wo_period)
            else:
                return match

        txt = re.sub(self.ALPHABETICAL_LIST_LETTERS_AND_PERIODS_REGEX,
                     partial(replace_letter_period, val=a),
                     self.text, re.IGNORECASE)
        return txt

    def replace_alphabet_list_parens(self, a):
        """
        Input: "a) ffegnog (b) fgegkl c)"
        Output: "\ra) ffegnog \r&✂&b) fgegkl \rc)"
        """

        def replace_alphabet_paren(match, val=None):
            match = match.group()
            print(match, val)
            if '(' in match:
                match_wo_paren = match.strip('(')
                if match_wo_paren == val:
                    return '\\r&✂&{}'.format(match_wo_paren)
                else:
                    return match
            else:
                if match == val:
                    return '\\r{}'.format(match)
                else:
                    return match

        txt = re.sub(self.EXTRACT_ALPHABETICAL_LIST_LETTERS_REGEX,
                     partial(replace_alphabet_paren, val=a),
                     self.text, re.IGNORECASE)
        return txt

    def replace_correct_alphabet_list(self, a, parens):
        if parens:
            a = self.replace_alphabet_list_parens(a)
        else:
            a = self.replace_alphabet_list(a)
        return a

    def last_array_item_replacement(self, a, i, alphabet, list_array, parens):
        if (len(alphabet) == 0) & (len(list_array) == 0) or (
                list_array[i - 1] not in alphabet) or (a not in alphabet):
            return a
        if abs(alphabet.index(list_array[i - 1]) - alphabet.index(a)) != 1:
            return a
        result = self.replace_correct_alphabet_list(a, parens)
        return result

    def other_items_replacement(self, a, i, alphabet, list_array, parens):
        if (len(alphabet) == 0) & (len(list_array) == 0) or (
                list_array[i - 1] not in alphabet) or (a not in alphabet) or (
                    list_array[i + 1] not in alphabet):
            return a
        if alphabet.index(list_array[i + 1]) - alphabet.index(a) != 1 and \
                abs(alphabet.index(list_array[i - 1]) - alphabet.index(a)) != 1:
            return a
        result = self.replace_correct_alphabet_list(a, parens)
        return result

    def iterate_alphabet_array(self, regex, parens=False, roman_numeral=False):
        list_array = re.findall(regex, self.text)
        alphabet = self.ROMAN_NUMERALS if roman_numeral else self.LATIN_NUMERALS
        list_array = [i for i in list_array if i in alphabet]
        # print(list_array)
        for ind, each in enumerate(list_array):
            if ind == len(list_array) - 1:
                self.text = self.last_array_item_replacement(each, ind, alphabet, list_array, parens)
            else:
                self.text = self.other_items_replacement(
                    each, ind, alphabet, list_array, parens)
        return self.text


if __name__ == "__main__":
    text = "a) ffegnog (b) fgegkl c)"
    # "\ra) ffegnog \r&✂&b) fgegkl \rc)"
    # text = 'a. ffegnog b. fgegkl c.'
    # \ra∯ ffegnog \rb∯ fgegkl \rc∯
    li = ListItemReplacer(text)
    print(li.format_alphabetical_lists())
