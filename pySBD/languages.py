#!/usr/bin/env python
# -*- coding: utf-8 -*-

LANGUAGE_CODES = {'en': "English", 'hi': "Hindi"}


class Language(object):

    def __init__(self, code):
        self.code = LANGUAGE_CODES[code]
