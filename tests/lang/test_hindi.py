# -*- coding: utf-8 -*-
import pytest

GOLDEN_HI_RULES_TEST_CASES = [
    (u"सच्चाई यह है कि इसे कोई नहीं जानता। हो सकता है यह फ़्रेन्को के खिलाफ़ कोई विद्रोह रहा हो, या फिर बेकाबू हो गया कोई आनंदोत्सव।",
    [u"सच्चाई यह है कि इसे कोई नहीं जानता। ", u"हो सकता है यह फ़्रेन्को के खिलाफ़ कोई विद्रोह रहा हो, या फिर बेकाबू हो गया कोई आनंदोत्सव।"])
]

@pytest.mark.parametrize('text,expected_sents', GOLDEN_HI_RULES_TEST_CASES)
def test_hi_sbd(hi_default_fixture, text, expected_sents):
    """Hindi language SBD tests from Pragmatic Segmenter"""
    segments = hi_default_fixture.segment(text)
    assert segments == expected_sents
