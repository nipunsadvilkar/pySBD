from pysbd import segmenter
import pytest
import pysbd

@pytest.fixture()
def pysbd_default_en_no_clean_no_span_fixture():
    en_segmenter = pysbd.Segmenter(language="en", clean=False, char_span=False)
    return en_segmenter

@pytest.fixture()
def en_with_clean_no_span_fixture():
    en_segmenter = pysbd.Segmenter(language="en", clean=True, char_span=False)
    return en_segmenter

@pytest.fixture()
def en_no_clean_with_span_fixture():
    en_segmenter = pysbd.Segmenter(language="en", clean=False, char_span=True)
    return en_segmenter

@pytest.fixture()
def hi_default_fixture():
    hi_segmenter = pysbd.Segmenter(language="hi", clean=False, char_span=False)
    return hi_segmenter

@pytest.fixture()
def mr_default_fixture():
    mr_segmenter = pysbd.Segmenter(language="mr", clean=False, char_span=False)
    return mr_segmenter

@pytest.fixture()
def zh_default_fixture():
    zh_segmenter = pysbd.Segmenter(language="zh", clean=False, char_span=False)
    return zh_segmenter

@pytest.fixture()
def es_default_fixture():
    es_segmenter = pysbd.Segmenter(language="es", clean=False, char_span=False)
    return es_segmenter

@pytest.fixture()
def es_with_clean_no_span_fixture():
    es_segmenter_clean = pysbd.Segmenter(language="es", clean=True, char_span=False)
    return es_segmenter_clean

@pytest.fixture()
def am_default_fixture():
    am_segmenter = pysbd.Segmenter(language="am", clean=False, char_span=False)
    return am_segmenter
