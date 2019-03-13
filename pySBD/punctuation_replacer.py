# -*- coding: utf-8 -*-
import re
from pySBD.rules import Rule, Text


class EscapeRegexReservedCharacters(object):
    LeftParen = Rule(re.escape(r'('), '\\(')
    RightParen = Rule(re.escape(r')'), '\\)')
    LeftBracket = Rule(re.escape(r'\['), '\\[')
    RightBracket = Rule(re.escape(r'\]'), '\\]')
    Dash = Rule(re.escape(r'\-'), '\\-')

    All = [LeftParen, RightParen, LeftBracket, RightBracket, Dash]


class SubEscapedRegexReservedCharacters(object):
    SubLeftParen = Rule(re.escape(r"\\("), "(")
    SubRightParen = Rule(re.escape(r'\\)'), ')')
    SubLeftBracket = Rule(re.escape(r'\\['), '[')
    SubRightBracket = Rule(re.escape(r'\\]'), ']')
    SubDash = Rule(re.escape(r'\\-'), '-')

    All = [
        SubLeftParen, SubRightParen, SubLeftBracket, SubRightBracket, SubDash
    ]


def replace_punctuation(match):
    text = Text(match.group()).apply(*EscapeRegexReservedCharacters.All)
    sub = re.sub(r'\.', '∯', text)
    sub_1 = re.sub(r'\。', '&ᓰ&', sub)
    sub_2 = re.sub(r'\．', '&ᓱ&', sub_1)
    sub_3 = re.sub(r'\！', '&ᓳ&', sub_2)
    sub_4 = re.sub(r'\!', '&ᓴ&', sub_3)
    sub_5 = re.sub(r'\?', '&ᓷ&', sub_4)
    sub_6 = re.sub(r'\？', '&ᓸ&', sub_5)
    text = Text(sub_6).apply(*SubEscapedRegexReservedCharacters.All)
    return text
