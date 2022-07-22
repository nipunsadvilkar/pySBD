import pytest

GOLDEN_OD_RULES_TEST_CASES = []

@pytest.mark.parametrize('text,expected_sents', GOLDEN_OD_RULES_TEST_CASES)
def test_od_sbd(od_default_fixture, text, expected_sents):
    """odia language SBD tests"""
    segments = od_default_fixture.segment(text)
    assert segments == expected_sents