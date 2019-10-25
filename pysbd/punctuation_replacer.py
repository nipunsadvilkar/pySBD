# -*- coding: utf-8 -*-
import re
from pysbd.utils import Rule, Text


class EscapeRegexReservedCharacters(object):
    LeftParen = Rule(r'\(', '\\(')
    RightParen = Rule(r'\)', '\\)')
    # LeftParen = Rule(re.escape(r'('), '(')
    # RightParen = Rule(re.escape(r')'), ')')
    LeftBracket = Rule(r'\[', '\\[')
    RightBracket = Rule(r'\]', '\\]')
    Dash = Rule(r'\-', '\\-')

    All = [LeftParen, RightParen, LeftBracket, RightBracket, Dash]


class SubEscapedRegexReservedCharacters(object):
    SubLeftParen = Rule(r'\\\(', '(')
    SubRightParen = Rule(r'\\\)', ')')
    # SubLeftParen = Rule(re.escape(r"\\("), "(")
    # SubRightParen = Rule(re.escape(r'\\)'), ')')
    SubLeftBracket = Rule(r'\\\[', '[')
    SubRightBracket = Rule(r'\\\]', ']')
    SubDash = Rule(r'\\\-', '-')

    All = [
        SubLeftParen, SubRightParen, SubLeftBracket, SubRightBracket, SubDash
    ]


def replace_punctuation(match, match_type=None):
    text = Text(match.group()).apply(*EscapeRegexReservedCharacters.All)
    sub = re.sub(r'\.', '∯', text)
    sub_1 = re.sub(r'\。', '&ᓰ&', sub)
    sub_2 = re.sub(r'\．', '&ᓱ&', sub_1)
    sub_3 = re.sub(r'\！', '&ᓳ&', sub_2)
    sub_4 = re.sub(r'\!', '&ᓴ&', sub_3)
    sub_5 = re.sub(r'\?', '&ᓷ&', sub_4)
    last_sub = re.sub(r'\？', '&ᓸ&', sub_5)
    if match_type != 'single':
        last_sub = re.sub(r"'", '&⎋&', last_sub)
    text = Text(last_sub).apply(*SubEscapedRegexReservedCharacters.All)
    return text
