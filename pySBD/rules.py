#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# https://regex101.com/r/P1IWyb/1/
NEWLINE_IN_MIDDLE_OF_SENTENCE_REGEX = r"(?<=\s)\n(?=([a-z]|\())"
NEWLINE_IN_MIDDLE_OF_WORD_REGEX = r"\n(?=[a-zA-Z]{1,2}\\n)"
