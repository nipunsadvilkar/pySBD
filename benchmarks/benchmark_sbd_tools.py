import blingfire
import nltk
import pysbd
import spacy
import stanza

from syntok.tokenizer import Tokenizer
import syntok.segmenter as syntok_segmenter

from english_golden_rules import GOLDEN_EN_RULES

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
    segments = pysbd_segmenter.segment(text)
    return [s.strip() for s in segments]

def spacy_tokenize(text):
    return [sent.text for sent in nlp(text).sents]

def spacy_dep_tokenize(text):
    return [sent.text for sent in nlp_dep(text).sents]

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


total_rules = len(GOLDEN_EN_RULES)

def benchmark(golden_rules, tokenize_func):
    score = 0
    for rule in golden_rules:
        text, expected = rule
        segments = tokenize_func(text)
        if segments == expected:
            score += 1
    percent_score = (score / total_rules) * 100.0

    return percent_score

if __name__ == "__main__":
    import time
    libraries = (
        blingfire_tokenize,
        nltk_tokenize,
        pysbd_tokenize,
        spacy_tokenize,
        spacy_dep_tokenize,
        stanza_tokenize,
        syntok_tokenize)
    for tokenize_func in libraries:
        t = time.time()
        for i in range(100):
            percent_score = benchmark(GOLDEN_EN_RULES, tokenize_func)

        time_taken = time.time() - t
        print()
        print(tokenize_func.__name__)
        print('GRS score: {:0.2f}%'.format(percent_score))
        print('Speed(Avg over 100 runs): {:>10.2f} ms'.format(time_taken*1000/100))
