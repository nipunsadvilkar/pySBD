# -*- coding: utf-8 -*-
import re
from pysbd.punctuation_replacer import replace_punctuation


class ExclaimationWords(object):
    """
    Searches for exclaimation points that are part of words
    and not ending punctuation and replaces them.
    """
    EXCLAIMATION_WORDS = "!Xũ !Kung ǃʼOǃKung !Xuun !Kung-Ekoka ǃHu ǃKhung ǃKu ǃung ǃXo ǃXû ǃXung ǃXũ !Xun Yahoo! Y!J Yum!".split()
    EXCLAIMATION_REGEX = r"|".join(re.escape(w) for w in EXCLAIMATION_WORDS)

    @classmethod
    def apply_rules(cls, text):
        return re.sub(ExclaimationWords.EXCLAIMATION_REGEX, replace_punctuation,
                      text)
