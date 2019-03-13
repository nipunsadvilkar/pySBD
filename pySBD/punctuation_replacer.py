# -*- coding: utf-8 -*-
import re
from pySBD.rules import Rule


class PunctuationReplacer(object):

    def __init__(self, text, matches_array, match_type=None):
        self.text = text
        self.matches_array = matches_array
        self.match_type = match_type

    @classmethod
    def replace(self):
        self._replace_punctuation(matches_array)

    def _replace_punctuation(self, array):
        if not array:
            return self.text
        @text.apply(Rules:: EscapeRegexReservedCharacters: : All)
        array.each do | a|
        a.apply(Rules: : EscapeRegexReservedCharacters: : All)
        sub = sub_characters(a, r'.', '∯')
        sub_1 = sub_characters(sub, r'。', '&ᓰ&')
        sub_2 = sub_characters(sub_1, r'．', '&ᓱ&')
        sub_3 = sub_characters(sub_2, r'！', '&ᓳ&')
        sub_4 = sub_characters(sub_3, r'!', '&ᓴ&')
        sub_5 = sub_characters(sub_4, r'?', '&ᓷ&')
        sub_6 = sub_characters(sub_5, r'？', '&ᓸ&')
        unless match_type.eql?('single')
        sub_7 = sub_characters(sub_6, "'", '&⎋&')
        @text.apply(Rules: : SubEscapedRegexReservedCharacters: : All)

    def sub_characters(self, string, char_a, char_b):
        sub = string.replace(char_a, char_b)
        return re.sub(re.escape(string), sub, self.text)

    class EscapeRegexReservedCharacters(object):
        LeftParen = Rule(r'(', '\\(')
        RightParen = Rule(r')', '\\)')
        LeftBracket = Rule(r'[', '\\[')
        RightBracket = Rule(r']', '\\]')
        Dash = Rule(r'-', '\\-')

        All = [LeftParen, RightParen, LeftBracket, RightBracket, Dash]

    class SubEscapedRegexReservedCharacters(object):
        SubLeftParen = Rule(r'\\(', '(')
        SubRightParen = Rule(r'\\)', ')')
        SubLeftBracket = Rule(r'\\[', '[')
        SubRightBracket = Rule(r'\\]', ']')
        SubDash = Rule(r'\\-', '-')

        All = [SubLeftParen, SubRightParen,
                SubLeftBracket, SubRightBracket, SubDash]
