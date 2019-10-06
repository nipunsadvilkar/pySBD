# -*- coding: utf-8 -*-
from pysbd.rules import Rule


class EllipsisRules(object):

    # Rubular: http://rubular.com/r/i60hCK81fz
    ThreeConsecutiveRule = Rule(r'\.\.\.(?=\s+[A-Z])', '☏.')

    # Rubular: http://rubular.com/r/Hdqpd90owl
    FourConsecutiveRule = Rule(r'(?<=\S)\.{3}(?=\.\s[A-Z])', 'ƪ')

    # Rubular: http://rubular.com/r/YBG1dIHTRu
    ThreeSpaceRule = Rule(r'(\s\.){3}\s', '♟')

    # Rubular: http://rubular.com/r/2VvZ8wRbd8
    FourSpaceRule = Rule(r'(?<=[a-z])(\.\s){3}\.($|\\n)', '♝')

    OtherThreePeriodRule = Rule(r'\.\.\.', 'ƪ')

    All = [ThreeSpaceRule, FourSpaceRule, FourConsecutiveRule,
           ThreeConsecutiveRule, OtherThreePeriodRule]
