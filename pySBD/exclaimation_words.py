# -*- coding: utf-8 -*-
import re
from pySBD.punctuation_replacer import PunctuationReplacer


class ExclamationWords(object):
    """
    Searches for exclamation points that are part of words
    and not ending punctuation and replaces them.
    """
    EXCLAMATION_WORDS = "!Xũ !Kung ǃʼOǃKung !Xuun !Kung-Ekoka ǃHu ǃKhung ǃKu ǃung ǃXo ǃXû ǃXung ǃXũ !Xun Yahoo! Y!J Yum!".split()
    EXCLAMATION_REGEX = r"|".join(re.escape(w) for w in EXCLAMATION_WORDS)

    def __init__(self, text):
        self.text = text

    @classmethod
    def apply_rules(self):
        matches = re.findall(ExclamationWords.EXCLAMATION_REGEX, self.text)
        PunctuationReplacer(self.text, matches).replace()
