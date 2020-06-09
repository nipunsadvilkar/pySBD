import pytest
from pysbd.languages import LANGUAGE_CODES, Language


def test_lang_code2instance_mapping():
    for code, language_module in LANGUAGE_CODES.items():
        assert Language.get_language_code(code) == language_module

def test_exception_on_no_lang_code_provided():
    with pytest.raises(ValueError) as e:
        Language.get_language_code('')
    assert "Provide valid language ID i.e. ISO code." in str(e.value)

def test_exception_on_unsupported_lang_code_provided():
    with pytest.raises(ValueError) as e:
        Language.get_language_code('elvish')
    assert "Provide valid language ID i.e. ISO code." in str(e.value)
