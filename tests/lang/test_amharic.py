# -*- coding: utf-8 -*-
import pytest

GOLDEN_AM_RULES_TEST_CASES = [
    ("እንደምን አለህ፧መልካም ቀን ይሁንልህ።እባክሽ ያልሽዉን ድገሚልኝ።",
     ["እንደምን አለህ፧", "መልካም ቀን ይሁንልህ።", "እባክሽ ያልሽዉን ድገሚልኝ።"]),
]

@pytest.mark.parametrize('text,expected_sents', GOLDEN_AM_RULES_TEST_CASES)
def test_am_sbd(am_default_fixture, text, expected_sents):
    """Amharic language SBD tests"""
    segments = am_default_fixture.segment(text)
    assert segments == expected_sents
