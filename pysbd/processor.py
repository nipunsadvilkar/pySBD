# -*- coding: utf-8 -*-
import re
import os
from pysbd.rules import Text
from pysbd.lists_item_replacer import ListItemReplacer
from pysbd.languages import Language
from pysbd.lang.standard import (Standard, Abbreviation,
                                 DoublePunctuationRules,
                                 ExclamationPointRules, SubSymbolsRules,
                                 ReinsertEllipsisRules)
from pysbd.lang.common.numbers import Common, Numbers
from pysbd.lang.common.ellipsis import EllipsisRules
from pysbd.exclamation_words import ExclamationWords
from pysbd.between_punctuation import BetweenPunctuation
from pysbd.abbreviation_replacer import AbbreviationReplacer


class TextSpan(object):

    def __init__(self, sent, start, end):
        self.sent = sent
        self.start = start
        self.end = end

    def __repr__(self):
        return "{0}(sent='{1}', start={2}, end={3})".format(
            self.__class__.__name__, self.sent, self.start, self.end)


class Processor(object):

    def __init__(self, text, language='common', char_span=False):
        self.language = language
        self.language_module = Language.get_language_code(language)
        self.text = text
        self.char_span = char_span

    def process(self):
        if not self.text:
            # return empty list?
            return self.text
        li = ListItemReplacer(self.text)
        self.text = li.add_line_break()
        self.text = AbbreviationReplacer(self.text).replace()
        self.replace_numbers()
        self.replace_continuous_punctuation()
        self.replace_periods_before_numeric_references()
        self.text = Text(self.text).apply(
            Abbreviation.WithMultiplePeriodsAndEmailRule,
            Standard.GeoLocationRule, Standard.FileFormatRule)
        processed = self.split_into_segments()
        return processed

    def rm_none_flatten(self, sents):
        """Remove None values and unpack list of list sents

        Parameters
        ----------
        sents : list
            list of sentences

        Returns
        -------
        list
            unpacked and None removed list of sents
        """
        sents = list(filter(None, sents))
        if not any(isinstance(s, list) for s in sents):
            return sents
        new_sents = []
        for sent in sents:
            if isinstance(sent, list):
                for s in sent:
                    new_sents.append(s)
            else:
                new_sents.append(sent)
        return new_sents

    def sentences_with_char_spans(self, sents_w_spans, postp_sents):
        new_sents_spans = []
        tmp_offset = 0
        for sent_w_span, postp_sent in zip(sents_w_spans, postp_sents):
            sent, start, end = sent_w_span
            post_len = len(postp_sent) if postp_sent else len(sent)
            if start == 0:
                new_sents_spans.append((postp_sent, 0, post_len))
            else:
                new_sents_spans.append((postp_sent, tmp_offset, tmp_offset + post_len))
            tmp_offset = tmp_offset + post_len
        return new_sents_spans

    def split_into_segments(self):
        self.check_for_parens_between_quotes()
        sents = self.text.split('\r')
        # remove empty and none values
        sents = self.rm_none_flatten(sents)
        sents = [
            Text(s).apply(Standard.SingleNewLineRule, *EllipsisRules.All)
            for s in sents
        ]
        sents_w_spans = [self.check_for_punctuation(s) for s in sents]
        print(sents_w_spans)
        # flatten list of list of sentences
        sents_w_spans = self.rm_none_flatten(sents_w_spans)
        new_spans = []
        for s in sents_w_spans:
            tmp_char_start = s.start
            s.sent = Text(s.sent).apply(*SubSymbolsRules.All)
            post_process_sent = self.post_process_segments(s.sent)
            if post_process_sent and isinstance(post_process_sent, str):
                s.sent = post_process_sent
                new_spans.append(s)
            elif isinstance(post_process_sent, list):
                for se in post_process_sent:
                    new_spans.append(TextSpan(se, tmp_char_start, tmp_char_start + len(se)))
                    tmp_char_start += len(se)
        post_process_sents = self.rm_none_flatten(new_spans)
        for ps in post_process_sents:
            ps.sent = Text(ps.sent).apply(Standard.SubSingleQuoteRule)
        if self.char_span:
            return post_process_sents
        else:
            return [s.sent for s in post_process_sents]

    def post_process_segments(self, txt):
        if len(txt) > 2 and re.search(r'\A[a-zA-Z]*\Z', txt):
            return txt

        # below condition present in pragmatic segmenter
        # dont know significance of it yet.
        # if self.consecutive_underscore(txt) or len(txt) < 2:
        #     return txt

        if re.match(r'\t', txt):
            pass
        # TODO:
        # Decide on keeping or removing Standard.ExtraWhiteSpaceRule
        # txt = Text(txt).apply(*ReinsertEllipsisRules.All,
        #                       Standard.ExtraWhiteSpaceRule)
        txt = Text(txt).apply(*ReinsertEllipsisRules.All)
        if re.search(Common.QUOTATION_AT_END_OF_SENTENCE_REGEX, txt):
            txt = re.split(
                Common.SPLIT_SPACE_QUOTATION_AT_END_OF_SENTENCE_REGEX, txt)
            return txt
        else:
            txt = txt.replace('\n', '')
            return txt.strip()

    def check_for_parens_between_quotes(self):
        def paren_replace(match):
            match = match.group()
            sub1 = re.sub(r'\s(?=\()', '\r', match)
            sub2 = re.sub(r'(?<=\))\s', '\r', sub1)
            return sub2
        self.text = re.sub(Common.PARENS_BETWEEN_DOUBLE_QUOTES_REGEX,
                      paren_replace, self.text)

    def replace_continuous_punctuation(self):
        def continuous_puncs_replace(match):
            match = match.group()
            sub1 = re.sub(re.escape('!'), '&ᓴ&', match)
            sub2 = re.sub(re.escape('?'), '&ᓷ&', sub1)
            return sub2
        self.text = re.sub(Common.CONTINUOUS_PUNCTUATION_REGEX,
                        continuous_puncs_replace, self.text)

    def replace_periods_before_numeric_references(self):
        # https://github.com/diasks2/pragmatic_segmenter/commit/d9ec1a352aff92b91e2e572c30bb9561eb42c703
        self.text = re.sub(Common.NUMBERED_REFERENCE_REGEX,
                      r"∯\2\r\7", self.text)

    def consecutive_underscore(self, txt):
        # Rubular: http://rubular.com/r/fTF2Ff3WBL
        txt = re.sub(r'_{3,}', '', txt)
        return len(txt) == 0

    def check_for_punctuation(self, txt):
        if any(p in txt for p in Standard.Punctuations):
            sents = self.process_text(txt)
            return sents
        else:
            # NOTE: next steps of check_for_punctuation will unpack this list
            return TextSpan(txt, 0, len(txt))
            # return [txt]

    def process_text(self, txt):
        if txt[-1] not in Standard.Punctuations:
            txt += 'ȸ'
        txt = ExclamationWords.apply_rules(txt)
        txt = BetweenPunctuation(txt).replace()
        txt = Text(txt).apply(*DoublePunctuationRules.All,
                              Standard.QuestionMarkInQuotationRule,
                              *ExclamationPointRules.All)
        txt = ListItemReplacer(txt).replace_parens()
        txt = self.sentence_boundary_punctuation(txt)
        return txt

    def replace_numbers(self):
        self.text = Text(self.text).apply(*Numbers.All)

    def abbreviations_replacer(self, txt):
        # AbbreviationReplacer
        raise NotImplementedError

    def replace_abbreviations(self, txt):
        # abbreviations_replacer
        raise NotImplementedError

    def between_punctuation_processor(self, txt):
        # BetweenPunctuation
        raise NotImplementedError

    def between_punctuation(self, txt):
        # between_punctuation_processor
        raise NotImplementedError

    def sentence_boundary_punctuation(self, txt):
        if hasattr(self.language_module, 'ReplaceColonBetweenNumbersRule'):
            txt = Text(txt).apply(
                self.language_module.ReplaceColonBetweenNumbersRule)
        if hasattr(self.language_module, 'ReplaceNonSentenceBoundaryCommaRule'):
            txt = Text(txt).apply(
                self.language_module.ReplaceNonSentenceBoundaryCommaRule)
        txt = [
            TextSpan(m.group(), m.start(), m.end())
            for m in re.finditer(Common.SENTENCE_BOUNDARY_REGEX, txt)
            ]
        # txt = re.findall(Common.SENTENCE_BOUNDARY_REGEX, txt)
        return txt


if __name__ == "__main__":
    text = "Header 1.2; Attachment Z\n\n\td. Compliance Log – Volume 12 \n\tAttachment A\n\n\te. Additional Logistics Data\n\tSection 10"
    print("Input String:\n{}".format(text))
    p = Processor(text)
    processed_op = p.process()
    print("\nProcessed String:\n")
    print("Number of sentences: {}\n".format(len(processed_op)))
    print(processed_op)
    for e in processed_op:
        print(e)
