# -*- coding: utf-8 -*-
import pytest

GOLDEN_FA_RULES_TEST_CASES = [
    ("خوشبختم، آقای رضا. شما کجایی هستید؟ من از تهران هستم.",
     ["خوشبختم، آقای رضا.", "شما کجایی هستید؟", "من از تهران هستم."])
]


@pytest.mark.parametrize('text,expected_sents', GOLDEN_FA_RULES_TEST_CASES)
def test_fa_sbd(fa_default_fixture, text, expected_sents):
    """Persian language SBD tests"""
    segments = fa_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
