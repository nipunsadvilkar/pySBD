# -*- coding: utf-8 -*-
import re
from pysbd.punctuation_replacer import replace_punctuation


class ExclamationWords(object):
    """
    Searches for exclamation points that are part of words
    and not ending punctuation and replaces them.
    """
    EXCLAMATION_WORDS = "!Xũ !Kung ǃʼOǃKung !Xuun !Kung-Ekoka ǃHu ǃKhung ǃKu ǃung ǃXo ǃXû ǃXung ǃXũ !Xun Yahoo! Y!J Yum!".split()
    EXCLAMATION_REGEX = r"|".join(re.escape(w) for w in EXCLAMATION_WORDS)

    @classmethod
    def apply_rules(cls, text):
        return re.sub(ExclamationWords.EXCLAMATION_REGEX, replace_punctuation,
                      text)
