# -*- coding: utf-8 -*-
from pysbd.utils import Rule


class EllipsisRules(object):

    # below rules aren't similar to original rules of pragmatic segmenter
    # modification: spaces replaced with same number of symbols
    # Rubular: http://rubular.com/r/i60hCK81fz
    ThreeConsecutiveRule = Rule(r'\.\.\.(?=\s+[A-Z])', '☏☏.')

    # Rubular: http://rubular.com/r/Hdqpd90owl
    FourConsecutiveRule = Rule(r'(?<=\S)\.{3}(?=\.\s[A-Z])', 'ƪƪƪ')

    # Rubular: http://rubular.com/r/YBG1dIHTRu
    ThreeSpaceRule = Rule(r'(\s\.){3}\s', '♟♟♟♟♟♟♟')

    # Rubular: http://rubular.com/r/2VvZ8wRbd8
    FourSpaceRule = Rule(r'(?<=[a-z])(\.\s){3}\.($|\\n)', '♝♝♝♝♝♝♝')

    OtherThreePeriodRule = Rule(r'\.\.\.', 'ƪƪƪ')

    All = [ThreeSpaceRule, FourSpaceRule, FourConsecutiveRule,
           ThreeConsecutiveRule, OtherThreePeriodRule]
