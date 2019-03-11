# -*- coding: utf-8 -*-


class PunctuationReplacer(object):

    def __init__(self, text, matches_array, match_type=None):
        self.text = text
        self.matches_array = matches_array
        self.match_type = match_type

    def replace(self):
        self.replace_punctuation(matches_array)

    def replace_punctuation(self, array):
        return if !array | | array.empty?
            @text.apply(Rules: : EscapeRegexReservedCharacters: : All)
            array.each do | a|
            a.apply(Rules: : EscapeRegexReservedCharacters: : All)
            sub = sub_characters(a, '.', '∯')
            sub_1 = sub_characters(sub, '。', '&ᓰ&')
            sub_2 = sub_characters(sub_1, '．', '&ᓱ&')
            sub_3 = sub_characters(sub_2, '！', '&ᓳ&')
            sub_4 = sub_characters(sub_3, '!', '&ᓴ&')
            sub_5 = sub_characters(sub_4, '?', '&ᓷ&')
            sub_6 = sub_characters(sub_5, '？', '&ᓸ&')
            unless match_type.eql?('single')
            sub_7 = sub_characters(sub_6, "'", '&⎋&')
            @text.apply(Rules: : SubEscapedRegexReservedCharacters: : All)

    def sub_characters(self, string, char_a, char_b)
        sub = string.gsub(char_a, char_b)
        @text.gsub!(#{Regexp.escape(string)}, sub)

    class EscapeRegexReservedCharacters(object):
        LeftParen = Rule.new('(', '\\(')
        RightParen = Rule.new(')', '\\)')
        LeftBracket = Rule.new('[', '\\[')
        RightBracket = Rule.new(']', '\\]')
        Dash = Rule.new('-', '\\-')

        All = [LeftParen, RightParen,
                LeftBracket, RightBracket, Dash]

    class SubEscapedRegexReservedCharacters(object):
        SubLeftParen = Rule.new('\\(', '(')
        SubRightParen = Rule.new('\\)', ')')
        SubLeftBracket = Rule.new('\\[', '[')
        SubRightBracket = Rule.new('\\]', ']')
        SubDash = Rule.new('\\-', '-')

        All = [SubLeftParen, SubRightParen,
                SubLeftBracket, SubRightBracket, SubDash]
