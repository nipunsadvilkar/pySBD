import nltk

from .english_golden_rules import GOLDEN_EN_RULES

def nltk_english_benchmark(golden_rules):
    global percent_score
    total_rules = len(golden_rules)
    score = 0
    for rule in golden_rules:
        text, expected = rule
        segments = nltk.sent_tokenize(text)
        if segments == expected:
            score += 1
    percent_score = (score / total_rules) * 100.0

if __name__ == "__main__":
    import timeit
    time_taken = timeit.timeit("nltk_english_benchmark(GOLDEN_EN_RULES)",
                  setup="from __main__ import nltk_english_benchmark, GOLDEN_EN_RULES",
                  number=100)
    print(f'{nltk.__name__} - v{nltk.__version__}')
    print(f'GRS score: {percent_score:0.2f}%')
    print(f'Speed: {time_taken*1000:>10.2f} ms')
    # nltk - v3.5
    # GRS score: 56.25%
    # Speed:     342.98 ms
