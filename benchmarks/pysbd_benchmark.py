import pysbd

from .english_golden_rules import GOLDEN_EN_RULES

en_segmenter = pysbd.Segmenter(language="en", clean=False, char_span=False)

def pysbd_english_benchmark(golden_rules):
    global percent_score
    total_rules = len(golden_rules)
    score = 0
    for rule in golden_rules:
        text, expected = rule
        segments = en_segmenter.segment(text)
        if segments == expected:
            score += 1
    percent_score = (score / total_rules) * 100.0


if __name__ == "__main__":
    import timeit
    time_taken = timeit.timeit("pysbd_english_benchmark(GOLDEN_EN_RULES)",
                  setup="from __main__ import pysbd_english_benchmark, GOLDEN_EN_RULES",
                  number=100)
    print(f'{pysbd.__name__} - v{pysbd.__version__}')
    print(f'GRS score: {percent_score:.2f}%')
    print(f'Speed: {time_taken*1000:>10.2f} ms')
    # pysbd - v0.3.0rc
    # GRS score: 97.92%
    # Speed:    2449.18 ms
