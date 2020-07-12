# -*- coding: utf-8 -*-
import pytest

GOLDEN_UR_RULES_TEST_CASES = [
("کیا حال ہے؟ ميرا نام ___ ەے۔ میں حالا تاوان دےدوں؟",
 ["کیا حال ہے؟", "ميرا نام ___ ەے۔", "میں حالا تاوان دےدوں؟"]),
]

@pytest.mark.parametrize('text,expected_sents', GOLDEN_UR_RULES_TEST_CASES)
def test_ur_sbd(ur_default_fixture, text, expected_sents):
    """Urdu language SBD tests"""
    segments = ur_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
