# -*- coding: utf-8 -*-
import pytest
import pysbd
from pysbd.utils import TextSpan

TEST_ISSUE_DATA = [
    ('#27', "This new form of generalized PDF in (9) is generic and suitable for all the fading models presented in Table I withbranches MRC reception. In section III, (9) will be used in the derivations of the unified ABER and ACC expression.",
        ["This new form of generalized PDF in (9) is generic and suitable for all the fading models presented in Table I withbranches MRC reception.",
         "In section III, (9) will be used in the derivations of the unified ABER and ACC expression."]),
    ('#29', "Random walk models (Skellam, 1951;Turchin, 1998) received a lot of attention and were then extended to several more mathematically and statistically sophisticated approaches to interpret movement data such as State-Space Models (SSM) (Jonsen et al., 2003(Jonsen et al., , 2005 and Brownian Bridge Movement Model (BBMM) (Horne et al., 2007). Nevertheless, these models require heavy computational resources (Patterson et al., 2008) and unrealistic structural a priori hypotheses about movement, such as homogeneous movement behavior. A fundamental property of animal movements is behavioral heterogeneity (Gurarie et al., 2009) and these models poorly performed in highlighting behavioral changes in animal movements through space and time (Kranstauber et al., 2012).",
        ["Random walk models (Skellam, 1951;Turchin, 1998) received a lot of attention and were then extended to several more mathematically and statistically sophisticated approaches to interpret movement data such as State-Space Models (SSM) (Jonsen et al., 2003(Jonsen et al., , 2005 and Brownian Bridge Movement Model (BBMM) (Horne et al., 2007).",
         "Nevertheless, these models require heavy computational resources (Patterson et al., 2008) and unrealistic structural a priori hypotheses about movement, such as homogeneous movement behavior.",
         "A fundamental property of animal movements is behavioral heterogeneity (Gurarie et al., 2009) and these models poorly performed in highlighting behavioral changes in animal movements through space and time (Kranstauber et al., 2012)."]),
    ('#30', "Thus, we first compute EMC 3 's response time-i.e., the duration from the initial of a call (from/to a participant in the target region) to the time when the decision of task assignment is made; and then, based on the computed response time, we estimate EMC 3 maximum throughput [28]-i.e., the maximum number of mobile users allowed in the MCS system. EMC 3 algorithm is implemented with the Java SE platform and is running on a Java HotSpot(TM) 64-Bit Server VM; and the implementation details are given in Appendix, available in the online supplemental material.",
        ["Thus, we first compute EMC 3 's response time-i.e., the duration from the initial of a call (from/to a participant in the target region) to the time when the decision of task assignment is made; and then, based on the computed response time, we estimate EMC 3 maximum throughput [28]-i.e., the maximum number of mobile users allowed in the MCS system.",
         "EMC 3 algorithm is implemented with the Java SE platform and is running on a Java HotSpot(TM) 64-Bit Server VM; and the implementation details are given in Appendix, available in the online supplemental material."
        ]),
    ('#31', r"Proof. First let v ∈ V be incident to at least three leaves and suppose there is a minimum power dominating set S of G that does not contain v. If S excludes two or more of the leaves of G incident to v, then those leaves cannot be dominated or forced at any step. Thus, S excludes at most one leaf incident to v, which means S contains at least two leaves ℓ 1 and ℓ 2 incident to v. Then, (S\{ℓ 1 , ℓ 2 }) ∪ {v} is a smaller power dominating set than S, which is a contradiction. Now consider the case in which v ∈ V is incident to exactly two leaves, ℓ 1 and ℓ 2 , and suppose there is a minimum power dominating set S of G such that {v, ℓ 1 , ℓ 2 } ∩ S = ∅. Then neither ℓ 1 nor ℓ 2 can be dominated or forced at any step, contradicting the assumption that S is a power dominating set. If S is a power dominating set that contains ℓ 1 or ℓ 2 , say ℓ 1 , then (S\{ℓ 1 }) ∪ {v} is also a power dominating set and has the same cardinality. Applying this to every vertex incident to exactly two leaves produces the minimum power dominating set required by (3). Definition 3.4. Given a graph G = (V, E) and a set X ⊆ V , define ℓ r (G, X) as the graph obtained by attaching r leaves to each vertex in X. If X = {v 1 , . . . , v k }, we denote the r leaves attached to vertex v i as ℓ",
        ['Proof.', 'First let v ∈ V be incident to at least three leaves and suppose there is a minimum power dominating set S of G that does not contain v. If S excludes two or more of the leaves of G incident to v, then those leaves cannot be dominated or forced at any step.', 'Thus, S excludes at most one leaf incident to v, which means S contains at least two leaves ℓ 1 and ℓ 2 incident to v. Then, (S\\{ℓ 1 , ℓ 2 }) ∪ {v} is a smaller power dominating set than S, which is a contradiction.', 'Now consider the case in which v ∈ V is incident to exactly two leaves, ℓ 1 and ℓ 2 , and suppose there is a minimum power dominating set S of G such that {v, ℓ 1 , ℓ 2 } ∩ S = ∅.', 'Then neither ℓ 1 nor ℓ 2 can be dominated or forced at any step, contradicting the assumption that S is a power dominating set.', 'If S is a power dominating set that contains ℓ 1 or ℓ 2 , say ℓ 1 , then (S\\{ℓ 1 }) ∪ {v} is also a power dominating set and has the same cardinality.', 'Applying this to every vertex incident to exactly two leaves produces the minimum power dominating set required by (3).', 'Definition 3.4.', 'Given a graph G = (V, E) and a set X ⊆ V , define ℓ r (G, X) as the graph obtained by attaching r leaves to each vertex in X. If X = {v 1 , . . . , v k }, we denote the r leaves attached to vertex v i as ℓ']),
    ('#34', '.', ['.']),
    ('#34', '..', ['..']),
    ('#34', '. . .', ['. . .']),
    ('#34', '! ! !', ['! ! !']),
    ('#36', '??', ['??']),
    ('#37', "As an example of a different special-purpose mechanism, we have introduced a methodology for letting donors make their donations to charities conditional on donations by other donors (who, in turn, can make their donations conditional) [70]. We have used this mechanism to collect money for Indian Ocean Tsunami and Hurricane Katrina victims. We have also introduced a more general framework for negotiation when one agent's actions have a direct effect (externality) on the other agents' utilities [69]. Both the charities and externalities methodologies require the solution of NP-hard optimization problems in general, but there are some natural tractable cases as well as effective MIP formulations. Recently, Ghosh and Mahdian [86] at Yahoo! Research extended our charities work, and based on this a web-based system for charitable donations was built at Yahoo!",
     ['As an example of a different special-purpose mechanism, we have introduced a methodology for letting donors make their donations to charities conditional on donations by other donors (who, in turn, can make their donations conditional) [70].', 'We have used this mechanism to collect money for Indian Ocean Tsunami and Hurricane Katrina victims.', "We have also introduced a more general framework for negotiation when one agent's actions have a direct effect (externality) on the other agents' utilities [69].", 'Both the charities and externalities methodologies require the solution of NP-hard optimization problems in general, but there are some natural tractable cases as well as effective MIP formulations.', 'Recently, Ghosh and Mahdian [86] at Yahoo! Research extended our charities work, and based on this a web-based system for charitable donations was built at Yahoo!']),
    ('#39', "T stands for the vector transposition. As shown in Fig. ??",
     ["T stands for the vector transposition.", "As shown in Fig. ??"]),
    ('#39', 'Fig. ??', ['Fig. ??'])
]

TEST_ISSUE_DATA_CHAR_SPANS = [
    ('#49', "1) The first item. 2) The second item.",
        [('1) The first item. ', 0, 18), ('2) The second item.', 19, 38)]
    ),
    ('#49', "a. The first item. b. The second item. c. The third list item",
        [
            ('a. The first item. ', 0, 18), ('b. The second item. ', 19, 38),
            ('c. The third list item', 39, 61)]
    ),
    ('#53', "Trust in journalism is not associated with frequency of media use (except in the case of television as mentioned above), indicating that trust is not an important predictor of media use, though it might have an important impact on information processing. This counterintuitive fi nding can be explained by taking into account the fact that audiences do not watch informative content merely to inform themselves; they have other motivations that might override credibility concerns. For example, they might follow media primarily for entertainment purposes and consequently put less emphasis on the quality of the received information.As <|CITE|> have claimed, audiences tend to approach and process information differently depending on the channel; they approach television primarily for entertainment and newspapers primarily for information. This has implications for trust as well since audiences in an entertainment processing mode will be less attentive to credibility cues, such as news errors, than those in an information processing mode (Ibid.). <|CITE|> research confi rms this claim -he found that audiences tend to approach newspaper reading more actively than television viewing and that credibility assessments differ regarding whether audience members approach news actively or passively. These fi ndings can help explain why we found a weak positive correlation between television news exposure and trust in journalism. It could be that audiences turn to television not because they expect the best quality information but rather the opposite -namely, that they approach television news less critically, focus less attention on credibility concerns and, therefore, develop a higher degree of trust in journalism. The fact that those respondents who follow the commercial television channel POP TV and the tabloid Slovenske Novice exhibit a higher trust in journalistic objectivity compared to those respondents who do not follow these media is also in line with this interpretation. The topic of Janez Janša and exposure to media that are favourable to him and his SDS party is negatively connected to trust in journalism. This phenomenon can be partly explained by the elaboration likelihood model <|CITE|> , according to which highly involved individuals tend to process new information in a way that maintains and confi rms their original opinion by 1) taking information consistent with their views (information that falls within a narrow range of acceptance) as simply veridical and embracing it, and 2) judging counter-attitudinal information to be the product of biased, misguided or ill-informed sources and rejecting it <|CITE|> <|CITE|> . Highly partisan audiences will, therefore, tend to react to dissonant information by lowering the trustworthiness assessment of the source of such information.",
        [('Trust in journalism is not associated with frequency of media use (except in the case of television as mentioned above), indicating that trust is not an important predictor of media use, though it might have an important impact on information processing. ', 0, 254),
        ('This counterintuitive fi nding can be explained by taking into account the fact that audiences do not watch informative content merely to inform themselves; they have other motivations that might override credibility concerns. ', 255, 481),
        ('For example, they might follow media primarily for entertainment purposes and consequently put less emphasis on the quality of the received information.As <|CITE|> have claimed, audiences tend to approach and process information differently depending on the channel; they approach television primarily for entertainment and newspapers primarily for information. ', 482, 843),
        ('This has implications for trust as well since audiences in an entertainment processing mode will be less attentive to credibility cues, such as news errors, than those in an information processing mode (Ibid.). ', 844, 1054),
        ('<|CITE|> research confi rms this claim -he found that audiences tend to approach newspaper reading more actively than television viewing and that credibility assessments differ regarding whether audience members approach news actively or passively. ', 1055, 1303),
        ('These fi ndings can help explain why we found a weak positive correlation between television news exposure and trust in journalism. ', 1304, 1435),
        ('It could be that audiences turn to television not because they expect the best quality information but rather the opposite -namely, that they approach television news less critically, focus less attention on credibility concerns and, therefore, develop a higher degree of trust in journalism. ', 1436, 1728),
        ('The fact that those respondents who follow the commercial television channel POP TV and the tabloid Slovenske Novice exhibit a higher trust in journalistic objectivity compared to those respondents who do not follow these media is also in line with this interpretation. ', 1729, 1998),
        ('The topic of Janez Janša and exposure to media that are favourable to him and his SDS party is negatively connected to trust in journalism. ', 1999, 2138),
        ('This phenomenon can be partly explained by the elaboration likelihood model <|CITE|> , according to which highly involved individuals tend to process new information in a way that maintains and confi rms their original opinion by ', 2139, 2368),
        ('1) taking information consistent with their views (information that falls within a narrow range of acceptance) as simply veridical and embracing it, and ', 2369, 2521),
        ('2) judging counter-attitudinal information to be the product of biased, misguided or ill-informed sources and rejecting it <|CITE|> <|CITE|> . ', 2522, 2664),
        ('Highly partisan audiences will, therefore, tend to react to dissonant information by lowering the trustworthiness assessment of the source of such information.', 2665, 2824)]
    ),
    ('#55', "She turned to him, \"This is great.\" She held the book out to show him.",
        [
            ('She turned to him, "This is great." ', 0, 35), ('She held the book out to show him.', 36, 70)
        ])

]

@pytest.mark.parametrize('issue_no,text,expected_sents', TEST_ISSUE_DATA)
def test_issue(issue_no, text, expected_sents):
    """pySBD issues tests from https://github.com/nipunsadvilkar/pySBD/issues/"""
    seg = pysbd.Segmenter(language="en", clean=False)
    segments = seg.segment(text)
    assert segments == expected_sents
    # clubbing sentences and matching with original text
    assert text == " ".join(segments)

@pytest.mark.parametrize('issue_no,text,expected_sents_w_spans', TEST_ISSUE_DATA_CHAR_SPANS)
def test_issues_with_char_spans(issue_no, text, expected_sents_w_spans):
    """pySBD issues tests from https://github.com/nipunsadvilkar/pySBD/issues/"""
    seg = pysbd.Segmenter(language="en", clean=False, char_span=True)
    segments = seg.segment(text)
    expected_text_spans = [TextSpan(sent_w_span[0], sent_w_span[1], sent_w_span[2])
                           for sent_w_span in expected_sents_w_spans]
    assert segments == expected_text_spans
    # clubbing sentences and matching with original text
    assert text == "".join([seg.sent for seg in segments])
