import pysbd
import time
import cProfile
from tqdm import tqdm

segmenter = pysbd.Segmenter(language='en', clean=False)

pr = cProfile.Profile()

def time_profile(text, n_trials):
    pr.enable()
    times = []
    for i in tqdm(range(n_trials)):
        start = time.time()
        segments = segmenter.segment(text)
        end = time.time()
        times.append(end - start)
    pr.disable()
    pr.print_stats(sort='time')
    return times

if __name__ == "__main__":
    text = open('benchmarks/1661-0.txt').read()
    n_trials = 1
    times = time_profile(text, n_trials)
    print("Total seconds {}".format(sum(times)))
    print("Num trials {}".format(n_trials))
    print("Average second {}".format(sum(times)/n_trials))
