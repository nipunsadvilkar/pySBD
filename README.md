# pySBD: Python Sentence Boundary Disambiguation (SBD)

[![Build Status](https://travis-ci.org/nipunsadvilkar/pySBD.svg?branch=master)](https://travis-ci.org/nipunsadvilkar/pySBD)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](https://github.com/nipunsadvilkar/pySBD/blob/master/LICENSE)

pySBD - python Sentence Boundary Disambiguation (SBD) - is a rule-based sentence boundary detection module that works out-of-the-box across many languages.

This project is a direct port of ruby gem - [Pragmatic Segmenter](https://github.com/diasks2/pragmatic_segmenter) which provides rule-based sentence boundary detection.


## Install

**Python**
```
pip install pysbd
```

## Usage

* Currently pySBD support only English language. Support for more languages will be released soon.

```python
import pySBD
text = "Hello World. My name is Jonas."
seg = pySBD.Segmenter(text, clean=False)
print(seg.segment())
# ['Hello World.', 'My name is Jonas.']
```

## Contributing

If you find a text that is incorrectly segmented using pySBD, please submit an issue.

1. Fork it ( https://github.com/nipunsadvilkar/pySBD/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request


# Credit
This project wouldn't be possible without the great work done by [Pragmatic Segmenter](https://github.com/diasks2/pragmatic_segmenter) team.
