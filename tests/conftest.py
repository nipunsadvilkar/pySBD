from pysbd import segmenter
import pytest
import pysbd

@pytest.fixture()
def pysbd_default_en_no_clean_no_span_fixture():
    segmenter = pysbd.Segmenter(language="en", clean=False, char_span=False)
    return segmenter

@pytest.fixture()
def en_with_clean_no_span_fixture():
    segmenter = pysbd.Segmenter(language="en", clean=True, char_span=False)
    return segmenter

@pytest.fixture()
def en_no_clean_with_span_fixture():
    segmenter = pysbd.Segmenter(language="en", clean=False, char_span=True)
    return segmenter

@pytest.fixture()
def hi_default_fixture():
    segmenter = pysbd.Segmenter(language="en", clean=False, char_span=False)
    return segmenter
