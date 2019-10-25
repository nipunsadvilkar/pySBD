import pytest
import pysbd
from pysbd.utils import TextSpan

@pytest.mark.parametrize('text,expected',
                         [('My name is Jonas E. Smith. Please turn to p. 55.',
                         [TextSpan(sent='My name is Jonas E. Smith.',
                         start=0, end=26),
                         TextSpan(sent='Please turn to p. 55.',
                         start=27, end=48)])])
def test_sbd_char_span(text, expected):
    """Test sentences with character offsets"""
    seg = pysbd.Segmenter(language="en", clean=False, char_span=True)
    segments = seg.segment(text)
    assert segments == expected

@pytest.mark.xfail(raises=ValueError)
def test_sbd_clean_chart_span():
    """Test to not allow clean=True and char_span=True
    """
    seg = pysbd.Segmenter(language="en", clean=True, char_span=True)
    text = "<h2 class=\"lined\">Hello</h2>\n<p>This is a test. Another test.</p>"
    seg.segment(text)
