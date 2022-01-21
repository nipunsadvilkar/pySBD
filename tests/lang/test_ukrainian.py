# -*- coding: utf-8 -*-
import re
import pytest

GOLDEN_UK_RULES_TEST_CASES = [
    ("Я народився у м. Харків. Нині я мешкаю на вул. Сводоби 12, кв. 0. ",
     ["Я народився у м. Харків.", "Нині я мешкаю на вул. Сводоби 12, кв. 0."]),
    
    ('"Га?" — відповів хлопець, цілковито здивований. "Що сьогодні, мій веселий компаньйоне?" — гукнув Скрудж.',
     ['"Га?" — відповів хлопець, цілковито здивований.', '"Що сьогодні, мій веселий компаньйоне?" — гукнув Скрудж.']),

    ("Попередньо забронювала велику альтанку, ту, що якраз під лісом на 20.09. Почнемо з'їжджатися десь на 11-ту.",
     ["Попередньо забронювала велику альтанку, ту, що якраз під лісом на 20.09.", "Почнемо з'їжджатися десь на 11-ту."]),

    ("Станом на 2500 р. до н.е.",
     ["Станом на 2500 р. до н.е."]),
]


@pytest.mark.parametrize('text,expected_sents', GOLDEN_UK_RULES_TEST_CASES)
def test_uk_sbd(uk_default_fixture, text, expected_sents):
    """Ukrainian language SBD tests"""
    segments = uk_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents


def test_uk_multiperiod_abbreviation_regex(uk_default_fixture):
    text = "Станом на 2500 р. до н.е."
    match = re.search(uk_default_fixture.language_module.MULTI_PERIOD_ABBREVIATION_REGEX,
                      text)
    assert match.group() == "н.е."
