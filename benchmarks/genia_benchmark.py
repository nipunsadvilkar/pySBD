import blingfire
import nltk
import pysbd
import spacy
import stanza

import syntok
from syntok.tokenizer import Tokenizer
import syntok.segmenter as syntok_segmenter

from pathlib import Path

pysbd_segmenter = pysbd.Segmenter(language="en", clean=False, char_span=False)

nlp = spacy.blank('en')
nlp.add_pipe(nlp.create_pipe("sentencizer"))
nlp_dep = spacy.load('en_core_web_sm', disable=["ner"])
#stanza.download('en')
stanza_nlp = stanza.Pipeline(lang='en', processors='tokenize')

syntok_tokenizer = Tokenizer()

def blingfire_tokenize(text):
    return blingfire.text_to_sentences(text).split('\n')

def nltk_tokenize(text):
    return nltk.sent_tokenize(text)

def pysbd_tokenize(text):
    return pysbd_segmenter.segment(text)

def spacy_tokenize(text):
    return [sent.text.strip("\n") for sent in nlp(text).sents]

def spacy_dep_tokenize(text):
    return [sent.text.strip("\n") for sent in nlp_dep(text).sents]

def stanza_tokenize(text):
    return [e.text for e in stanza_nlp(text).sentences]

def make_sentences(segmented_tokens):
    for sentence in segmented_tokens:
        yield "".join(str(token) for token in sentence).strip()

def syntok_tokenize(text):
    tokens = syntok_tokenizer.split(text)
    result = syntok_segmenter.split(iter(tokens))
    segments = [sent for sent in make_sentences(result)]
    return segments

def load_genia_corpus(genia_raw_dir):
    txtfiles = Path(genia_raw_dir).glob("**/*.txt")
    txtfiles = list(txtfiles)
    all_docs = []
    for ind, txtfile in enumerate(txtfiles, start=1):
        with open(txtfile) as f:
            geniatext = f.read().strip()
        expected = geniatext.split('\n')
        all_docs.append((geniatext, expected))

    return all_docs

def benchmark(docs, tokenize_func):

    correct = 0
    for (text, expected) in docs:
        segments = tokenize_func(text)
        if segments == expected:
            correct +=1
    return correct


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--genia',
            help="Path to the directory containing genia data."
    )

    args = parser.parse_args()

    libraries = (
        blingfire_tokenize,
        nltk_tokenize,
        pysbd_tokenize,
        spacy_tokenize,
        spacy_dep_tokenize,
        stanza_tokenize,
        syntok_tokenize
        )

    docs = load_genia_corpus(args.genia)
    total = len(docs)
    for tokenize_func in libraries:
        correct = benchmark(docs, tokenize_func)
        percent_score = correct/total * 100
        print()
        print(tokenize_func.__name__)
        print(f'GENIA abstract acc: {percent_score:0.2f}%')
