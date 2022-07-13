import pytest

GOLDEN_TE_RULES_TEST_CASES = [                                          # Changes required here
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

@pytest.mark.parametrize('text,expected_sents', GOLDEN_TE_RULES_TEST_CASES)
def test_te_sbd(te_default_fixture, text, expected_sents):
    """Telugu language SBD tests"""
    segments = te_default_fixture.segment(text)
    assert segments == expected_sents