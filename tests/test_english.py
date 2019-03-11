import pytest
from pySBD.rules import sample_segment


TEST_CASES = [
    ("Hello World. My name is Jonas.", ["Hello World.", "My name is Jonas."]),
    # ("What is your name? My name is Jonas.", ["What is your name?", "My name is Jonas."]),
    # ("There it is! I found it.", ["There it is!", "I found it."])
    ]


@pytest.mark.parametrize('text,expected_sents', TEST_CASES)
def test_en_sbd_prag(text, expected_sents):
    """SBD tests from Pragmatic Segmenter"""
    op_sent = sample_segment(text, expected_sents)
    assert op_sent == expected_sents
