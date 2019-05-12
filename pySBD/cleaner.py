# -*- coding: utf-8 -*-
import re
from pySBD.rules import Text
from pySBD.clean.rules import CleanRules as cr


class Cleaner(object):

    def __init__(self, text, language='common', doc_type=None):
        self.text = text
        self.language = language
        # self.language_module = Language.get_language_code(language)
        self.doc_type = doc_type

    def clean(self):
        if not self.text:
            return self.text
        # raise NotImplementedError
        self.remove_all_newlines()
        # self.replace_double_newlines()
        # self.replace_newlines()
        # self.replace_escaped_newlines()
        # # self.remove_or_escape_html_tags(clean_rule_4)
        # self.replace_punctuation_in_brackets()
        # # self.inlineformattingrule(clean_rule_6)
        # self.clean_quotations()
        # self.clean_table_of_contents()
        # self.check_for_no_space_in_between_sentences()
        # self.clean_consecutive_characters()
        return self.text

    def remove_all_newlines(self):
        self.remove_newline_in_middle_of_sentence()
        self.remove_newline_in_middle_of_word()

    def remove_newline_in_middle_of_sentence(self):
        def replace_w_blank(match):
            match = match.group()
            sub = re.sub(cr.NEWLINE_IN_MIDDLE_OF_SENTENCE_REGEX, '', match)
            return sub
        self.text = re.sub(r'(?:[^\.])*', replace_w_blank, self.text)

    def remove_newline_in_middle_of_word(self):
        self.text = Text(self.text).apply(cr.NewLineInMiddleOfWordRule)


if __name__ == "__main__":
    text = "It was a cold \nnight in the city."
    c = Cleaner(text)
    print(c.clean())
