import spacy

from .english_golden_rules import GOLDEN_EN_RULES

nlp = spacy.blank('en')
nlp.add_pipe(nlp.create_pipe("sentencizer"))


def spacy_english_benchmark(golden_rules):
    global percent_score
    total_rules = len(golden_rules)
    score = 0
    for rule in golden_rules:
        text, expected = rule
        doc = nlp(text)
        segments = [sent.text for sent in doc.sents]
        if segments == expected:
            score += 1
    percent_score = (score / total_rules) * 100.0


if __name__ == "__main__":
    import timeit
    time_taken = timeit.timeit("spacy_english_benchmark(GOLDEN_EN_RULES)",
                  setup="from __main__ import spacy_english_benchmark, GOLDEN_EN_RULES",
                  number=100)
    print(f'{spacy.__name__} - v{spacy.__version__}')
    print(f'GRS score: {percent_score:0.2f}%')
    print(f'Speed: {time_taken*1000:>10.2f} ms')
    # spacy - v2.1.8
    # GRS score: 52.08%
    # Speed:     473.96 ms
