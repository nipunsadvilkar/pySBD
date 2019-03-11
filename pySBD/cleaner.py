# -*- coding: utf-8 -*-
# from pySBD.languages import Language
# from pySBD.languages import Language


class Cleaner(object):

    def __init__(self, text, language='common', doc_type=None):
        self.text = text
        self.language = language
        # self.language_module = Language.get_language_code(language)
        self.doc_type = doc_type

    def clean(self):
        raise NotImplementedError
        # clean_rule_1 = remove_all_newlines(self.text)
        # clean_rule_2 = replace_double_newlines(clean_rule_1)
        # clean_rule_3 = replace_newlines(clean_rule_2)
        # clean_rule_4 = replace_escaped_newlines(clean_rule_3)
        # clean_rule_5 = remove_or_escape_html_tags(clean_rule_4)
        # clean_rule_6 = replace_punctuation_in_brackets(clean_rule_5)
        # clean_rule_7 = inlineformattingrule(clean_rule_6)
        # clean_rule_8 = clean_quotations(clean_rule_7)
        # clean_rule_9 = clean_table_of_contents(clean_rule_8)
        # clean_rule_10 = check_for_no_space_in_between_sentences(clean_rule_9)
        # clean_rule_11 = clean_consecutive_characters(clean_rule_10)

    def remove_all_newlines(self):
        raise NotImplementedError
        # rm_all_newline_1 = remove_newline_in_middle_of_sentence(self)
        # rm_newline_in_middle = remove_newline_in_middle_of_word(self)
        # return rm_newline_in_middle

    # def remove_newline_in_middle_of_sentence(self):
