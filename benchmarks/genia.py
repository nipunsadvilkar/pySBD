import pysbd
from pathlib import Path

segmenter = pysbd.Segmenter(language="en", clean=False, char_span=False)

def run_full_genia_corpus(genia_raw_dir):
    txtfiles = Path(genia_raw_dir).glob("**/*.txt")
    txtfiles = list(txtfiles)
    failed = []
    passed = 0
    for ind, txtfile in enumerate(txtfiles, start=1):
        print(f'Processing {ind}: {txtfile}')
        with open(txtfile) as f:
            geniatext = f.read().strip()
        expected = geniatext.split('\n')
        segments = segmenter.segment(geniatext)
        try:
            assert segments == expected
            passed += 1
        except AssertionError:
            print("Failed")
            failed.append(txtfile)
    print(f'Total Files {len(txtfiles)} | Passed: {passed} | Failed: {len(failed)}')
    return failed

def to_file(failed, outputpath):
    with open(outputpath, 'w') as f:
        for eachpath in failed:
            f.write(f'{eachpath}\n')

def genia_failed_cases_inspector(filepath):
    # /Users/nipunsadvilkar/projects/Personal/genia-dependency-trees/raw/future_use/7665588.txt
    with open(filepath) as f:
        geniatext = f.read().strip()

    expected = geniatext.split('\n')
    segments = segmenter.segment(geniatext)

    while len(expected) < len(segments):
        expected.append("")
    # print(len(segments), len(expected))

    for seg, exp in zip(segments, expected):
        if seg != exp:
            print(f'{repr(exp)} >>>>>>> {repr(seg)}')


if __name__ == "__main__":
    genia_raw_dir = "/Users/nipunsadvilkar/projects/Personal/genia-dependency-trees/raw/"
    failed_files = run_full_genia_corpus(genia_raw_dir)
    to_file(failed_files, 'benchmarks/pysbd_on_genia_failed.txt')
    # genia_failed_cases_inspector('/Users/nipunsadvilkar/projects/Personal/genia-dependency-trees/raw/train/2205477.txt')
