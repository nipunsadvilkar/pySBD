import pytest
from pysbd.cleaner import Cleaner
from pysbd.languages import Language

TEST_TOBE_CLEANED_DATA = [
    ("It was a cold \nnight in the city.", "It was a cold night in the city."),
    ("This is the U.S. Senate my friends. <em>Yes.</em> <em>It is</em>!",
    "This is the U.S. Senate my friends. Yes. It is!")
]

@pytest.mark.parametrize('text,expected_cleaned_sents', TEST_TOBE_CLEANED_DATA)
def test_cleaner(text, expected_cleaned_sents):
    """SBD tests from Pragmatic Segmenter"""
    cleaned_text = Cleaner(text, Language.get_language_code('en')).clean()
    assert cleaned_text == expected_cleaned_sents

def test_cleaner_doesnt_mutate_input(text="It was a cold \nnight in the city."):
    cleaned_text = Cleaner(text, Language.get_language_code('en')).clean()
    assert text == "It was a cold \nnight in the city."

def test_cleaner_none_input(text=None):
    cleaned_text = Cleaner(text, Language.get_language_code('en')).clean()
    assert cleaned_text == text

def test_cleaner_no_input(text=""):
    cleaned_text = Cleaner(text, Language.get_language_code('en')).clean()
    assert cleaned_text == text
