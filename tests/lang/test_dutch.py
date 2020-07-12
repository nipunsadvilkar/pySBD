# -*- coding: utf-8 -*-
import pytest

GOLDEN_NL_RULES_TEST_CASES = [
    ("Hij schoot op de JP8-brandstof toen de Surface-to-Air (sam)-missiles op hem af kwamen. 81 procent van de schoten was raak.",
     ["Hij schoot op de JP8-brandstof toen de Surface-to-Air (sam)-missiles op hem af kwamen.", "81 procent van de schoten was raak."]),
    ("81 procent van de schoten was raak. ...en toen barste de hel los.",
     ["81 procent van de schoten was raak.", "...en toen barste de hel los."]),
    ("Afkorting aanw. vnw.", ["Afkorting aanw. vnw."])
]

@pytest.mark.parametrize('text,expected_sents', GOLDEN_NL_RULES_TEST_CASES)
def test_nl_sbd(nl_default_fixture, text, expected_sents):
    """Dutch language SBD tests"""
    segments = nl_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
