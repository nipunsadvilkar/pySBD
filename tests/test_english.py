# -*- coding: utf-8 -*-
import pytest
import pySBD
# from pySBD.segmenter import Segmenter


TEST_CASES = [
    ("Hello World. My name is Jonas.", ["Hello World.", "My name is Jonas."]),
    ("What is your name? My name is Jonas.", ["What is your name?", "My name is Jonas."]),
    ("There it is! I found it.", ["There it is!", "I found it."]),
    ("My name is Jonas E. Smith.", ["My name is Jonas E. Smith."]),
    ("Please turn to p. 55.", ["Please turn to p. 55."]),
    ("Were Jane and co. at the party?", ["Were Jane and co. at the party?"]),
    ("They closed the deal with Pitt, Briggs & Co. at noon.",
        ["They closed the deal with Pitt, Briggs & Co. at noon."]),
    (
        "Let's ask Jane and co. They should know.",
        ["Let's ask Jane and co.", "They should know."]),
    (
        "They closed the deal with Pitt, Briggs & Co. It closed yesterday.", [
            "They closed the deal with Pitt, Briggs & Co.",
            "It closed yesterday."
        ],
    ),
    ("I can see Mt. Fuji from here.", ["I can see Mt. Fuji from here."]),
    (
        "St. Michael's Church is on 5th st. near the light.",
        ["St. Michael's Church is on 5th st. near the light."],
    ),
    ("That is JFK Jr.'s book.", ["That is JFK Jr.'s book."]),
    ("I visited the U.S.A. last year.", ["I visited the U.S.A. last year."]),
    (
        "I live in the E.U. How about you?",
        ["I live in the E.U.", "How about you?"],
    ),
    (
        "I live in the U.S. How about you?",
        ["I live in the U.S.", "How about you?"],
    ),
    ("I work for the U.S. Government in Virginia.",
        ["I work for the U.S. Government in Virginia."]),
    ("I have lived in the U.S. for 20 years.",
        ["I have lived in the U.S. for 20 years."]),
    # Most difficult sentence to crack
    pytest.param(
         "At 5 a.m. Mr. Smith went to the bank. He left the bank at 6 P.M. Mr. Smith then went to the store.",
         [
             "At 5 a.m. Mr. Smith went to the bank.",
             "He left the bank at 6 P.M.", "Mr. Smith then went to the store."
         ],
    marks=pytest.mark.xfail),
    ("She has $100.00 in her bag.", ["She has $100.00 in her bag."]),
    ("She has $100.00. It is in her bag.", ["She has $100.00.", "It is in her bag."]),
    ("He teaches science (He previously worked for 5 years as an engineer.) at the local University.",
        ["He teaches science (He previously worked for 5 years as an engineer.) at the local University."]),
    ("Her email is Jane.Doe@example.com. I sent her an email.",
        ["Her email is Jane.Doe@example.com.", "I sent her an email."]),
    ("The site is: https://www.example.50.com/new-site/awesome_content.html. Please check it out.",
        ["The site is: https://www.example.50.com/new-site/awesome_content.html.",
            "Please check it out."]),
    (
        "She turned to him, 'This is great.' she said.",
        ["She turned to him, 'This is great.' she said."],
    ),
    (
        'She turned to him, "This is great." she said.',
        ['She turned to him, "This is great." she said.'],
    ),
    (
        'She turned to him, "This is great." She held the book out to show him.',
        [
            'She turned to him, "This is great."',
            "She held the book out to show him."
        ],
    ),
    ("Hello!! Long time no see.", ["Hello!!", "Long time no see."]),
    ("Hello?? Who is there?", ["Hello??", "Who is there?"]),
    ("Hello!? Is that you?", ["Hello!?", "Is that you?"]),
    ("Hello?! Is that you?", ["Hello?!", "Is that you?"]),
    (
        "1.) The first item 2.) The second item",
        ["1.) The first item", "2.) The second item"],
    ),
    (
        "1.) The first item. 2.) The second item.",
        ["1.) The first item.", "2.) The second item."],
    ),
    (
        "1) The first item 2) The second item",
        ["1) The first item", "2) The second item"],
    ),
    ("1) The first item. 2) The second item.",
        ["1) The first item.", "2) The second item."]),
    (
        "1. The first item 2. The second item",
        ["1. The first item", "2. The second item"],
    ),
    (
        "1. The first item. 2. The second item.",
        ["1. The first item.", "2. The second item."],
    ),
    (
        "• 9. The first item • 10. The second item",
        ["• 9. The first item", "• 10. The second item"],
    ),
    (
        "⁃9. The first item ⁃10. The second item",
        ["⁃9. The first item", "⁃10. The second item"],
    ),
    (
        "a. The first item b. The second item c. The third list item",
        ["a. The first item", "b. The second item", "c. The third list item"],
    ),
    (
        "You can find it at N°. 1026.253.553. That is where the treasure is.",
        [
            "You can find it at N°. 1026.253.553.",
            "That is where the treasure is."
        ],
    ),
    (
        "She works at Yahoo! in the accounting department.",
        ["She works at Yahoo! in the accounting department."],
    ),
    (
        "We make a good team, you and I. Did you see Albert I. Jones yesterday?",
        [
            "We make a good team, you and I.",
            "Did you see Albert I. Jones yesterday?"
        ],
    ),
    (
        "Thoreau argues that by simplifying one’s life, “the laws of the universe will appear less complex. . . .”",
        [
            "Thoreau argues that by simplifying one’s life, “the laws of the universe will appear less complex. . . .”"
        ],
    ),
    (
        """"Bohr [...] used the analogy of parallel stairways [...]" (Smith 55).""",
        [
            '"Bohr [...] used the analogy of parallel stairways [...]" (Smith 55).'
        ],
    ),
    ("If words are left off at the end of a sentence, and that is all that is omitted, indicate the omission with ellipsis marks (preceded and followed by a space) and then indicate the end of the sentence with a period . . . . Next sentence.",
        [
            "If words are left off at the end of a sentence, and that is all that is omitted, indicate the omission with ellipsis marks (preceded and followed by a space) and then indicate the end of the sentence with a period . . . .",
            "Next sentence."
        ]),
    (
        "I never meant that.... She left the store.",
        ["I never meant that....", "She left the store."],
    ),
    (
        "I wasn’t really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn’t mean it.",
        [
            "I wasn’t really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn’t mean it."
        ],
    ),
    (
        "One further habit which was somewhat weakened . . . was that of combining words into self-interpreting compounds. . . . The practice was not abandoned. . . .",
        [
            "One further habit which was somewhat weakened . . . was that of combining words into self-interpreting compounds.",
            ". . . The practice was not abandoned. . . ."
        ],
    )
]

TESTS_WITH_CLEAN = [
        ("It was a cold \nnight in the city.",
            ["It was a cold night in the city."]),
        ("features\ncontact manager\nevents, activities\n",
            ["features", "contact manager", "events, activities"]),
        ("Hello world.Today is Tuesday.Mr. Smith went to the store and bought 1,000.That is a lot.",
            ["Hello world.", "Today is Tuesday.",
                "Mr. Smith went to the store and bought 1,000.",
                "That is a lot."])
        ]

PDF_TEST_DATA = [
    ("This is a sentence\ncut off in the middle because pdf.",
        ["This is a sentence cut off in the middle because pdf."]),
    ("Organising your care early \nmeans you'll have months to build a good relationship with your midwife or doctor, ready for \nthe birth.",
        ["Organising your care early means you'll have months to build a good relationship with your midwife or doctor, ready for the birth."]),
    ("10. Get some rest \n \nYou have the best chance of having a problem-free pregnancy and a healthy baby if you follow \na few simple guidelines:",
        ["10. Get some rest", "You have the best chance of having a problem-free pregnancy and a healthy baby if you follow a few simple guidelines:"]),
    ("• 9. Stop smoking \n• 10. Get some rest \n \nYou have the best chance of having a problem-free pregnancy and a healthy baby if you follow \na few simple guidelines:  \n\n1. Organise your pregnancy care early",
        ["• 9. Stop smoking", "• 10. Get some rest", "You have the best chance of having a problem-free pregnancy and a healthy baby if you follow a few simple guidelines:", "1. Organise your pregnancy care early"]),
    ("Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed; it was labelled 'ORANGE MARMALADE', but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody, so managed to put it into one of the cupboards as she fell past it.\n'Well!' thought Alice to herself, 'after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)",
        ["Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next.", "First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs.", "She took down a jar from one of the shelves as she passed; it was labelled 'ORANGE MARMALADE', but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody, so managed to put it into one of the cupboards as she fell past it.", "'Well!' thought Alice to herself, 'after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)"]),
    ("Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed; it was labelled 'ORANGE MARMALADE', but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody, so managed to put it into one of the cupboards as she fell past it.\r'Well!' thought Alice to herself, 'after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)",
        ["Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next.", "First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs.", "She took down a jar from one of the shelves as she passed; it was labelled 'ORANGE MARMALADE', but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody, so managed to put it into one of the cupboards as she fell past it.", "'Well!' thought Alice to herself, 'after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)"])
        ]


@pytest.mark.parametrize('text,expected_sents', TEST_CASES)
def test_en_sbd(text, expected_sents):
    """SBD tests from Pragmatic Segmenter"""
    seg = pySBD.Segmenter(text, clean=False)
    segments = seg.segment()
    assert segments == expected_sents


@pytest.mark.parametrize('text,expected_sents', TESTS_WITH_CLEAN)
def test_en_sbd_clean(text, expected_sents):
    """SBD tests from Pragmatic Segmenter"""
    seg = pySBD.Segmenter(text, clean=True)
    segments = seg.segment()
    assert segments == expected_sents


@pytest.mark.parametrize('text,expected_sents', PDF_TEST_DATA)
def test_en_pdf_type(text, expected_sents):
    seg = pySBD.Segmenter(text, clean=True, doc_type='pdf')
    segments = seg.segment()
    assert segments == expected_sents
