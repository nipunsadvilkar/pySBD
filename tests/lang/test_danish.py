# -*- coding: utf-8 -*-
import pytest
import pysbd

GOLDEN_DA_RULES_TEST_CASES = [
("Hej Verden. Mit navn er Jonas.",
 ["Hej Verden.", "Mit navn er Jonas."]),
("Hvad er dit navn? Mit nav er Jonas.",
 ["Hvad er dit navn?", "Mit nav er Jonas."]),
("There it is! I found it.",
 ["There it is!", "I found it."]),
("My name is Jonas E. Smith.",
 ["My name is Jonas E. Smith."]),
("Please turn to p. 55.",
 ["Please turn to p. 55."]),
("Were Jane and co. at the party?",
 ["Were Jane and co. at the party?"]),
("They closed the deal with Pitt, Briggs & Co. at noon.",
 ["They closed the deal with Pitt, Briggs & Co. at noon."]),
("Lad os spørge Jane og co. De burde vide det.",
 ["Lad os spørge Jane og co.", "De burde vide det."]),
("De lukkede aftalen med Pitt, Briggs & Co. Det lukkede i går.",
 ["De lukkede aftalen med Pitt, Briggs & Co.", "Det lukkede i går."]),
("De holdt Skt. Hans i byen.",
 ["De holdt Skt. Hans i byen."]),
("St. Michael's Kirke er på 5. gade nær ved lyset.",
 ["St. Michael's Kirke er på 5. gade nær ved lyset."]),
("That is JFK Jr.'s book.",
 ["That is JFK Jr.'s book."]),
("I visited the U.S.A. last year.",
 ["I visited the U.S.A. last year."]),
("Jeg bor i E.U. Hvad med dig?",
 ["Jeg bor i E.U.", "Hvad med dig?"]),
("I live in the U.S. Hvad med dig?",
 ["I live in the U.S.", "Hvad med dig?"]),
("I work for the U.S. Government in Virginia.",
 ["I work for the U.S. Government in Virginia."]),
("I have lived in the U.S. for 20 years.",
 ["I have lived in the U.S. for 20 years."]),
("She has $100.00 in her bag.",
 ["She has $100.00 in her bag."]),
("She has $100.00. It is in her bag.",
 ["She has $100.00.", "It is in her bag."]),
("He teaches science (He previously worked for 5 years as an engineer.) at the local University.",
 ["He teaches science (He previously worked for 5 years as an engineer.) at the local University."]),
("Her email is Jane.Doe@example.com. I sent her an email.",
 ["Her email is Jane.Doe@example.com.", "I sent her an email."]),
("The site is: https://www.example.50.com/new-site/awesome_content.html. Please check it out.",
 ["The site is: https://www.example.50.com/new-site/awesome_content.html.", "Please check it out."]),
("She turned to him, 'This is great.' she said.",
 ["She turned to him, 'This is great.' she said."]),
("She turned to him, \"This is great.\" she said.",
 ["She turned to him, \"This is great.\" she said."]),
("She turned to him, \"This is great.\" Hun held the book out to show him.",
 ["She turned to him, \"This is great.\"", "Hun held the book out to show him."]),
("Hello!! Long time no see.",
 ["Hello!!", "Long time no see."]),
("Hello?? Who is there?",
 ["Hello??", "Who is there?"]),
("Hello!? Is that you?",
 ["Hello!?", "Is that you?"]),
("Hello?! Is that you?",
 ["Hello?!", "Is that you?"]),
("1.) The first item 2.) The second item",
 ["1.) The first item", "2.) The second item"]),
("1.) The first item. 2.) The second item.",
 ["1.) The first item.", "2.) The second item."]),
("1) The first item 2) The second item",
 ["1) The first item", "2) The second item"]),
("1) The first item. 2) The second item.",
 ["1) The first item.", "2) The second item."]),
("1. The first item 2. The second item",
 ["1. The first item", "2. The second item"]),
("1. The first item. 2. The second item.",
 ["1. The first item.", "2. The second item."]),
("• 9. The first item • 10. The second item",
 ["• 9. The first item", "• 10. The second item"]),
("⁃9. The first item ⁃10. The second item",
 ["⁃9. The first item", "⁃10. The second item"]),
("a. The first item b. The second item c. The third list item",
 ["a. The first item", "b. The second item", "c. The third list item"]),
("You can find it at N°. 1026.253.553. That is where the treasure is.",
 ["You can find it at N°. 1026.253.553.", "That is where the treasure is."]),
("She works at Yahoo! in the accounting department.",
 ["She works at Yahoo! in the accounting department."]),
("Thoreau argues that by simplifying one’s life, “the laws of the universe will appear less complex. . . .”",
 ["Thoreau argues that by simplifying one’s life, “the laws of the universe will appear less complex. . . .”"]),
("\"Bohr  [...] used the analogy of parallel stairways  [...]\" (Smith 55).",
 ["\"Bohr  [...] used the analogy of parallel stairways  [...]\" (Smith 55)."]),
("If words are left off at the end of a sentence, and that is all that is omitted, indicate the omission with ellipsis marks (preceded and followed by a space) and then indicate the end of the sentence with a period . . . . Next sentence.",
 ["If words are left off at the end of a sentence, and that is all that is omitted, indicate the omission with ellipsis marks (preceded and followed by a space) and then indicate the end of the sentence with a period . . . .", "Next sentence."]),
("I never meant that.... She left the store.",
 ["I never meant that....", "She left the store."]),
("I wasn’t really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn’t mean it.",
 ["I wasn’t really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn’t mean it."]),
("One further habned. . . .",
 ["One further habned. . . ."])
]

@pytest.mark.parametrize('text,expected_sents', GOLDEN_DA_RULES_TEST_CASES)
def test_da_sbd(da_default_fixture, text, expected_sents):
    """Danish language SBD tests"""
    segments = da_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents

DA_RULES_CLEAN_TEST_CASES = [
    ("Hello world.I dag is Tuesday.Hr. Smith went to the store and bought 1,000.That is a lot.",
     ["Hello world.", "I dag is Tuesday.", "Hr. Smith went to the store and bought 1,000.", "That is a lot."]),
    ("It was a cold \nnight in the city.",
     ["It was a cold night in the city."])
]

DA_PDF_TEST_DATA = [("This is a sentence\ncut off in the middle because pdf.",
                    ["This is a sentence cut off in the middle because pdf."])]

@pytest.mark.parametrize('text,expected_sents', DA_RULES_CLEAN_TEST_CASES)
def test_da_sbd_clean(da_with_clean_no_span_fixture, text, expected_sents):
    """Danish language SBD tests with text clean"""
    segments = da_with_clean_no_span_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents

@pytest.mark.parametrize('text,expected_sents', DA_PDF_TEST_DATA)
def test_da_pdf_type(text, expected_sents):
    """SBD tests from Pragmatic Segmenter for doctype:pdf"""
    seg = pysbd.Segmenter(language="da", clean=True, doc_type='pdf')
    segments = seg.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
