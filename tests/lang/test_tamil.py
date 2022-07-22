import pytest

GOLDEN_TA_RULES_TEST_CASES = []

@pytest.mark.parametrize('text,expected_sents', GOLDEN_TA_RULES_TEST_CASES)
def test_ta_sbd(ta_default_fixture, text, expected_sents):
    """tamil language SBD tests"""
    segments = ta_default_fixture.segment(text)
    assert segments == expected_sents