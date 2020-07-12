import blingfire
from blingfire import text_to_sentences

from .english_golden_rules import GOLDEN_EN_RULES

def blingfire_english_benchmark(golden_rules):
    global percent_score
    total_rules = len(golden_rules)
    score = 0
    for rule in golden_rules:
        text, expected = rule
        segments = text_to_sentences(text).split('\n')
        if segments == expected:
            score += 1
    percent_score = (score / total_rules) * 100.0

if __name__ == "__main__":
    import timeit
    import pkg_resources
    version = pkg_resources.get_distribution("blingfire").version
    time_taken = timeit.timeit("blingfire_english_benchmark(GOLDEN_EN_RULES)",
                  setup="from __main__ import blingfire_english_benchmark, GOLDEN_EN_RULES",
                  number=100)
    print(f'{blingfire.__name__} - v{version}')
    print(f'GRS score: {percent_score:0.2f}%')
    print(f'Speed: {time_taken*1000:>10.2f} ms')
    # blingfire - v0.1.2
    # GRS score: 75.00%
    # Speed:      49.91 ms
