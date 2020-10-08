# pySBD: Python Sentence Boundary Disambiguation (SBD)

![Python package](https://github.com/nipunsadvilkar/pySBD/workflows/Python%20package/badge.svg) [![codecov](https://codecov.io/gh/nipunsadvilkar/pySBD/branch/master/graph/badge.svg)](https://codecov.io/gh/nipunsadvilkar/pySBD) [![License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](https://github.com/nipunsadvilkar/pySBD/blob/master/LICENSE) [![PyPi](https://img.shields.io/pypi/v/pysbd?color=blue&logo=pypi&logoColor=white)](https://pypi.python.org/pypi/pysbd) [![GitHub](https://img.shields.io/github/v/release/nipunsadvilkar/pySBD.svg?include_prereleases&logo=github&style=flat)](https://github.com/nipunsadvilkar/pySBD)

pySBD - python Sentence Boundary Disambiguation (SBD) - is a rule-based sentence boundary detection module that works out-of-the-box.

This project is a direct port of ruby gem - [Pragmatic Segmenter](https://github.com/diasks2/pragmatic_segmenter) which provides rule-based sentence boundary detection.

![pysbd_code](artifacts/pysbd_code.png?raw=true "pysbd_code")

## Install

**Python**

    pip install pysbd

## Usage

-   Currently pySBD supports only English language. Support for more languages will be released soon.

```python
import pysbd
text = "My name is Jonas E. Smith. Please turn to p. 55."
seg = pysbd.Segmenter(language="en", clean=False)
print(seg.segment(text))
# ['My name is Jonas E. Smith.', 'Please turn to p. 55.']
```

-   Use `pysbd` as a [spaCy](https://spacy.io/usage/processing-pipelines) pipeline component. (recommended)</br>Please refer to example [pysbd\_as\_spacy\_component.py](https://github.com/nipunsadvilkar/pySBD/blob/master/examples/pysbd_as_spacy_component.py)
- Use pysbd through [entrypoints](https://spacy.io/usage/saving-loading#entry-points-components)

```python
import spacy
from pysbd.utils import PySBDFactory

nlp = spacy.blank('en')

# explicitly adding component to pipeline
# (recommended - makes it more readable to tell what's going on)
nlp.add_pipe(PySBDFactory(nlp))

# or you can use it implicitly with keyword
# pysbd = nlp.create_pipe('pysbd')
# nlp.add_pipe(pysbd)

doc = nlp('My name is Jonas E. Smith. Please turn to p. 55.')
print(list(doc.sents))
# [My name is Jonas E. Smith., Please turn to p. 55.]

```

## Contributing

If you want to contribute new feature/language support or found a text that is incorrectly segmented using pySBD, then please head to [CONTRIBUTING.md](https://github.com/nipunsadvilkar/pySBD/blob/master/CONTRIBUTING.md) to know more and follow these steps.

1.  Fork it ( https://github.com/nipunsadvilkar/pySBD/fork )
2.  Create your feature branch (`git checkout -b my-new-feature`)
3.  Commit your changes (`git commit -am 'Add some feature'`)
4.  Push to the branch (`git push origin my-new-feature`)
5.  Create a new Pull Request

## Credit

This project wouldn't be possible without the great work done by [Pragmatic Segmenter](https://github.com/diasks2/pragmatic_segmenter) team.
