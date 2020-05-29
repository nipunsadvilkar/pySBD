import pytest
import pysbd
from pysbd.utils import TextSpan

@pytest.mark.parametrize('text,expected',
                         [('My name is Jonas E. Smith. Please turn to p. 55.',
                            [
                                ('My name is Jonas E. Smith. ', 0, 26),
                                ('Please turn to p. 55.', 27, 48),
                            ])
                         ])
def test_sbd_char_span(text, expected):
    """Test sentences with character offsets"""
    seg = pysbd.Segmenter(language="en", clean=False, char_span=True)
    segments = seg.segment(text)
    expected_text_spans = [TextSpan(sent_w_span[0], sent_w_span[1], sent_w_span[2])
                           for sent_w_span in expected]
    assert segments == expected_text_spans
    # clubbing sentences and matching with original text
    assert text == "".join([seg.sent for seg in segments])

@pytest.mark.xfail(raises=ValueError)
def test_sbd_clean_chart_span():
    """Test to not allow clean=True and char_span=True
    """
    seg = pysbd.Segmenter(language="en", clean=True, char_span=True)
    text = "<h2 class=\"lined\">Hello</h2>\n<p>This is a test. Another test.</p>"
    seg.segment(text)
