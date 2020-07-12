# -*- coding: utf-8 -*-
import pytest

GOLDEN_MR_RULES_TEST_CASES = [
    ("आज दसरा आहे. आज खूप शुभ दिवस आहे.",
     ["आज दसरा आहे.", "आज खूप शुभ दिवस आहे."]),
    ("ढग खूप गर्जत होते; पण पाऊस पडत नव्हता.",
     ["ढग खूप गर्जत होते; पण पाऊस पडत नव्हता."]),
    ("रमाची परीक्षा कधी आहे? अवकाश आहे अजून.",
     ["रमाची परीक्षा कधी आहे?", "अवकाश आहे अजून."]),
    ("शाब्बास, असाच अभ्यास कर! आणि मग तुला नक्की यश मिळणार.",
     ["शाब्बास, असाच अभ्यास कर!", "आणि मग तुला नक्की यश मिळणार."]),
    ("\"आपली आपण करी स्तुती तो एक मूर्ख\" असे समर्थ रामदासस्वामी म्हणतात.",
     ["\"आपली आपण करी स्तुती तो एक मूर्ख\" असे समर्थ रामदासस्वामी म्हणतात."])
]

@pytest.mark.parametrize('text,expected_sents', GOLDEN_MR_RULES_TEST_CASES)
def test_mr_sbd(mr_default_fixture, text, expected_sents):
    """Marathi language SBD tests"""
    segments = mr_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
