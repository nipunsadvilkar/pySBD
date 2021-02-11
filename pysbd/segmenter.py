# -*- coding: utf-8 -*-
import re

from pysbd.languages import Language
from pysbd.processor import Processor
from pysbd.cleaner import Cleaner
from pysbd.utils import TextSpan

class Segmenter(object):

    def __init__(self, language="en", clean=False, doc_type=None, char_span=False):
        """Segments a text into an list of sentences
        with or withour character offsets from original text

        Parameters
        ----------
        language : str, required
            specify a language use its two character ISO 639-1 code,
            by default "en"
        clean : bool, optional
            cleans original text, by default False
        doc_type : [type], optional
            Normal text or OCRed text, by default None
            set to `pdf` for OCRed text
        char_span : bool, optional
            Get start & end character offsets of each sentences
            within original text, by default False
        """
        self.language = language
        self.language_module = Language.get_language_code(language)
        self.clean = clean
        self.doc_type = doc_type
        self.char_span = char_span
        if self.clean and self.char_span:
            raise ValueError("char_span must be False if clean is True. "
                             "Since `clean=True` will modify original text.")
        # when doctype is pdf then force user to clean the text
        # char_span func wont be provided with pdf doctype also
        elif self.doc_type == 'pdf' and not self.clean:
            raise ValueError("`doc_type='pdf'` should have `clean=True` & "
                            "`char_span` should be False since original"
                            "text will be modified.")

    def cleaner(self, text):
        if hasattr(self.language_module, "Cleaner"):
            return self.language_module.Cleaner(text, self.language_module,
                                                doc_type=self.doc_type)
        else:
            return Cleaner(text, self.language_module, doc_type=self.doc_type)

    def processor(self, text):
        if hasattr(self.language_module, "Processor"):
            return self.language_module.Processor(text, self.language_module,
                                                  char_span=self.char_span)
        else:
            return Processor(text, self.language_module,
                             char_span=self.char_span)

    def sentences_with_char_spans(self, sentences):
        # since SENTENCE_BOUNDARY_REGEX doesnt account
        # for trailing whitespaces \s* & is used as suffix
        # to keep non-destructive text after segments joins
        sent_spans = []
        prior_end_char_idx = 0
        for sent in sentences:
            for match in re.finditer('{0}\s*'.format(re.escape(sent)), self.original_text):
                match_str = match.group()
                match_start_idx, match_end_idx = match.span()
                if match_end_idx > prior_end_char_idx:
                    # making sure if curren sentence and its span
                    # is either first sentence along with its char spans
                    # or current sent spans adjacent to prior sentence spans
                    sent_spans.append(
                        TextSpan(match_str, match_start_idx, match_end_idx))
                    prior_end_char_idx = match_end_idx
                    break
        return sent_spans

    def segment(self, text):
        self.original_text = text
        if not text:
            return []

        if self.clean or self.doc_type == 'pdf':
            text = self.cleaner(text).clean()

        postprocessed_sents = self.processor(text).process()
        sentence_w_char_spans = self.sentences_with_char_spans(postprocessed_sents)
        if self.char_span:
            return sentence_w_char_spans
        elif self.clean:
            # clean and destructed sentences
            return postprocessed_sents
        else:
            # nondestructive with whitespaces
            return [textspan.sent for textspan in sentence_w_char_spans]
