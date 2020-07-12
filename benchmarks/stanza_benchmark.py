import stanza
# stanza.download('en')
nlp = stanza.Pipeline(lang='en', processors='tokenize')

from .english_golden_rules import GOLDEN_EN_RULES

def stanza_english_benchmark(golden_rules):
    global percent_score
    total_rules = len(golden_rules)
    score = 0
    for rule in golden_rules:
        text, expected = rule
        doc = nlp(text)
        segments = [e.text for e in doc.sentences]
        if segments == expected:
            score += 1
    percent_score = (score / total_rules) * 100.0

if __name__ == "__main__":
    import timeit
    time_taken = timeit.timeit("stanza_english_benchmark(GOLDEN_EN_RULES)",
                  setup="from __main__ import stanza_english_benchmark, GOLDEN_EN_RULES",
                  number=100)
    print(f'{stanza.__name__} - v{stanza.__version__}')
    print(f'GRS score: {percent_score:0.2f}%')
    print(f'Speed: {time_taken*1000:>10.2f} ms')
    # stanza - v1.0.1
    # GRS score: 72.92%
    # Speed:  120803.37 ms
