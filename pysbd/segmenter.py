# -*- coding: utf-8 -*-
from pysbd.languages import Language
from pysbd.processor import Processor
from pysbd.cleaner import Cleaner


class Segmenter(object):

    def __init__(self, language="en", clean=False, doc_type=None):
        self.language = language
        self.language_module = Language.get_language_code(language)
        self.clean = clean
        self.doc_type = doc_type

    def segment(self, text):
        if not text:
            return []
        if self.clean:
            text = Cleaner(text, doc_type=self.doc_type).clean()
        processor = Processor(text)
        segments = processor.process()
        return segments


if __name__ == "__main__":
    # text = "Proof. First let v ∈ V be incident to at least three leaves and suppose there is a minimum power dominating set S of G that does not contain v. If S excludes two or more of the leaves of G incident to v, then those leaves cannot be dominated or forced at any step. Thus, S excludes at most one leaf incident to v, which means S contains at least two leaves ℓ 1 and ℓ 2 incident to v. Then, (S\{ℓ 1 , ℓ 2 }) ∪ {v} is a smaller power dominating set than S, which is a contradiction. Now consider the case in which v ∈ V is incident to exactly two leaves, ℓ 1 and ℓ 2 , and suppose there is a minimum power dominating set S of G such that {v, ℓ 1 , ℓ 2 } ∩ S = ∅. Then neither ℓ 1 nor ℓ 2 can be dominated or forced at any step, contradicting the assumption that S is a power dominating set. If S is a power dominating set that contains ℓ 1 or ℓ 2 , say ℓ 1 , then (S\{ℓ 1 }) ∪ {v} is also a power dominating set and has the same cardinality. Applying this to every vertex incident to exactly two leaves produces the minimum power dominating set required by (3). Definition 3.4. Given a graph G = (V, E) and a set X ⊆ V , define ℓ r (G, X) as the graph obtained by attaching r leaves to each vertex in X. If X = {v 1 , . . . , v k }, we denote the r leaves attached to vertex v i as ℓ"
    text = "Random walk models (Skellam, 1951;Turchin, 1998) received a lot of attention and were then extended to several more mathematically and statistically sophisticated approaches to interpret movement data such as State-Space Models (SSM) (Jonsen et al., 2003(Jonsen et al., , 2005 and Brownian Bridge Movement Model (BBMM) (Horne et al., 2007). Nevertheless, these models require heavy computational resources (Patterson et al., 2008) and unrealistic structural a priori hypotheses about movement, such as homogeneous movement behavior. A fundamental property of animal movements is behavioral heterogeneity (Gurarie et al., 2009) and these models poorly performed in highlighting behavioral changes in animal movements through space and time (Kranstauber et al., 2012)."
    print("Input String:\n{}".format(text))
    seg = Segmenter(language="en", clean=False)
    segments = seg.segment(text)
    print("\n################## Processing #######################\n")
    print("Number of sentences: {}\n".format(len(segments)))
    print("Sentences found:\n{}\n".format(segments))
    print("\n################## Output #######################\n")
    for ind, sent in enumerate(segments, start=1):
        print("{} -> {}".format(ind, sent))
