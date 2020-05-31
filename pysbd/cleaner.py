# -*- coding: utf-8 -*-
import re
from pysbd.utils import Text
from pysbd.clean.rules import PDF, HTML, CleanRules as cr


class Cleaner(object):

    def __init__(self, text, lang, doc_type=None):
        self.text = text
        self.lang = lang
        self.doc_type = doc_type

    def clean(self):
        if not self.text:
            return self.text
        self.remove_all_newlines()
        self.replace_double_newlines()
        self.replace_newlines()
        self.replace_escaped_newlines()
        self.text = Text(self.text).apply(*HTML.All)
        self.replace_punctuation_in_brackets()
        self.text = Text(self.text).apply(cr.InlineFormattingRule)
        self.clean_quotations()
        self.clean_table_of_contents()
        self.check_for_no_space_in_between_sentences()
        self.clean_consecutive_characters()
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

    def replace_double_newlines(self):
        self.text = Text(self.text).apply(cr.DoubleNewLineWithSpaceRule,
                                          cr.DoubleNewLineRule)

    def remove_pdf_line_breaks(self):
        self.text = Text(
                self.text).apply(cr.NewLineFollowedByBulletRule,
                                 PDF.NewLineInMiddleOfSentenceRule,
                                 PDF.NewLineInMiddleOfSentenceNoSpacesRule)

    def replace_newlines(self):
        if self.doc_type == 'pdf':
            self.remove_pdf_line_breaks()
        else:
            self.text = Text(
                self.text).apply(cr.NewLineFollowedByPeriodRule,
                                 cr.ReplaceNewlineWithCarriageReturnRule)

    def replace_escaped_newlines(self):
        self.text = Text(
                self.text).apply(cr.EscapedNewLineRule,
                                 cr.EscapedCarriageReturnRule,
                                 cr.TypoEscapedNewLineRule,
                                 cr.TypoEscapedCarriageReturnRule)

    def replace_punctuation_in_brackets(self):
        def replace_punct(match):
            match = match.group()
            if '?' in match:
                sub = re.sub(re.escape('?'), '&ᓷ&', match)
                return sub
            return match
        self.text = re.sub(r'\[(?:[^\]])*\]', replace_punct, self.text)

    def clean_quotations(self):
        # method added explicitly
        # pragmatic-segmenter applies thhis method
        # at different location
        self.text = re.sub('`', "'", self.text)
        self.text = Text(self.text).apply(
                                        cr.QuotationsFirstRule,
                                        cr.QuotationsSecondRule)

    def clean_table_of_contents(self):
        self.text = Text(self.text).apply(
                                        cr.TableOfContentsRule,
                                        cr.ConsecutivePeriodsRule,
                                        cr.ConsecutiveForwardSlashRule)

    def search_for_connected_sentences(self, word, txt, regex, rule):
        if not re.search(regex, word):
            return txt
        if any(k in word for k in cr.URL_EMAIL_KEYWORDS):
            return txt
        if any(a in word for a in self.lang.Abbreviation.ABBREVIATIONS):
            return txt
        new_word = Text(word).apply(rule)
        txt = re.sub(re.escape(word), new_word, txt)
        return txt

    def check_for_no_space_in_between_sentences(self):
        words = self.text.split(' ')
        for word in words:
            self.text = self.search_for_connected_sentences(word, self.text, cr.NO_SPACE_BETWEEN_SENTENCES_REGEX, cr.NoSpaceBetweenSentencesRule)
            self.text = self.search_for_connected_sentences(word, self.text, cr.NO_SPACE_BETWEEN_SENTENCES_DIGIT_REGEX, cr.NoSpaceBetweenSentencesDigitRule)

    def clean_consecutive_characters(self):
        self.text = Text(self.text).apply(
                                        cr.ConsecutivePeriodsRule,
                                        cr.ConsecutiveForwardSlashRule)
