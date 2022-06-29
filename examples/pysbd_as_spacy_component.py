"""
Example of pySBD as a sentencizer component for spaCy

Installation:
pip install spacy

NOTE: Works with spacy>=3.x.x
"""
import spacy
from spacy.language import Language

from pysbd.utils import PySBDFactory


@Language.factory("pysbd", default_config={"language": 'en'})
def pysbd_component(nlp, name, language: str):
    return PySBDFactory(nlp, language=language)


if __name__ == "__main__":
    text = "My name is Jonas E. Smith.          Please turn to p. 55."
    nlp = spacy.blank('en')

    # add as a spacy pipeline component
    nlp.add_pipe("pysbd", first=True)

    doc = nlp(text)
    print('sent_id', 'sentence', sep='\t|\t')
    for sent_id, sent in enumerate(doc.sents, start=1):
        print(sent_id, repr(sent.text), sep='\t|\t')
