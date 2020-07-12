# -*- coding: utf-8 -*-
import pytest

GOLDEN_EL_RULES_TEST_CASES = [
("Με συγχωρείτε· πού είναι οι τουαλέτες; Τις Κυριακές δε δούλευε κανένας. το κόστος του σπιτιού ήταν £260.950,00.",
 ["Με συγχωρείτε· πού είναι οι τουαλέτες;", "Τις Κυριακές δε δούλευε κανένας.", "το κόστος του σπιτιού ήταν £260.950,00."]),
]

@pytest.mark.parametrize('text,expected_sents', GOLDEN_EL_RULES_TEST_CASES)
def test_el_sbd(el_default_fixture, text, expected_sents):
    """Greek language SBD tests"""
    segments = el_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
