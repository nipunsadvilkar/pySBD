# -*- coding: utf-8 -*-
import pytest

GOLDEN_PL_RULES_TEST_CASES = [
("To słowo bałt. jestskrótem.",
 ["To słowo bałt. jestskrótem."]),
]

@pytest.mark.parametrize('text,expected_sents', GOLDEN_PL_RULES_TEST_CASES)
def test_pl_sbd(pl_default_fixture, text, expected_sents):
    """Polish language SBD tests"""
    segments = pl_default_fixture.segment(text)
    assert segments == expected_sents
