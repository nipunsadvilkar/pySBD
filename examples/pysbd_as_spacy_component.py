"""
Example of pySBD as a sentencizer component for spaCy

Installation:
pip install spacy
"""
import pysbd
import spacy

if __name__ == "__main__":
    text = "My name is Jonas E. Smith.          Please turn to p. 55."
    nlp = spacy.blank('en')
    
    @nlp.component("sbd")
    def pysbd_sentence_boundaries(doc):
        seg = pysbd.Segmenter(language="en", clean=False, char_span=True)
        sents_char_spans = seg.segment(doc.text)
        char_spans = [doc.char_span(sent_span.start, sent_span.end, alignment_mode="contract") for sent_span in sents_char_spans]
        start_token_ids = [span[0].idx for span in char_spans if span is not None]
        for token in doc:
            token.is_sent_start = True if token.idx in start_token_ids else False
        return doc

    # add as a spacy pipeline component
    nlp.add_pipe("sbd", first=True)

    doc = nlp(text)
    print('sent_id', 'sentence', sep='\t|\t')
    for sent_id, sent in enumerate(doc.sents, start=1):
        print(sent_id, sent.text, sep='\t|\t')
