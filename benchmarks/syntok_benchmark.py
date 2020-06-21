import syntok
import syntok.segmenter as segmenter
from syntok.tokenizer import Tokenizer

from .english_golden_rules import GOLDEN_EN_RULES

TOKENIZER = Tokenizer()

def make_sentences(segmented_tokens):
    for sentence in segmented_tokens:
        yield "".join(str(token) for token in sentence).strip()

def syntok_english_benchmark(golden_rules):
    global percent_score
    total_rules = len(golden_rules)
    score = 0
    for rule in golden_rules:
        text, expected = rule
        tokens = Tokenizer().split(text)
        result = segmenter.split(iter(tokens))
        segments = [sent for sent in make_sentences(result)]
        if segments == expected:
            score += 1
    percent_score = (score / total_rules) * 100.0

if __name__ == "__main__":
    import timeit
    import pkg_resources
    version = pkg_resources.get_distribution("syntok").version
    time_taken = timeit.timeit("syntok_english_benchmark(GOLDEN_EN_RULES)",
                  setup="from __main__ import syntok_english_benchmark, GOLDEN_EN_RULES",
                  number=100)
    print(f'{syntok.__name__} - v{version}')
    print(f'GRS score: {percent_score:0.2f}%')
    print(f'Speed: {time_taken*1000:>10.2f} ms')
    # syntok - v1.3.1
    # GRS score: 68.75%
    # Speed:     783.73 ms
