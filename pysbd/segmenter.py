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
        language : str, optional
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
        # for trailing whitespaces \s* is used as suffix
        # to keep non-destructive text after segments joins
        return [TextSpan(m.group(), m.start(), m.end()) for sent in sentences
                for m in re.finditer(f'{re.escape(sent)}\s*', self.original_text)]

    def segment(self, text):
        self.original_text = text
        if not text:
            return []
        if self.clean and self.char_span:
            raise ValueError("char_span must be False if clean is True. "
                             "Since `clean=True` will modify original text.")
        elif self.clean:
            text = self.cleaner(text).clean()
        postprocessed_sents = self.processor(text).process()
        sentence_w_char_spans = self.sentences_with_char_spans(postprocessed_sents)
        if self.clean:
            # clean and destructed sentences
            return postprocessed_sents
        elif self.char_span:
            return sentence_w_char_spans
        else:
            # nondestructive with whitespaces
            return [textspan.sent for textspan in sentence_w_char_spans]
