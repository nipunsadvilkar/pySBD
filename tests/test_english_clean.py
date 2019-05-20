# -*- coding: utf-8 -*-
import pytest
import pySBD


TESTS_WITH_CLEAN = [
        ("It was a cold \nnight in the city.",
            ["It was a cold night in the city."]),
        ("features\ncontact manager\nevents, activities\n",
            ["features", "contact manager", "events, activities"]),
        ("Hello world.Today is Tuesday.Mr. Smith went to the store and bought 1,000.That is a lot.",
            ["Hello world.", "Today is Tuesday.",
                "Mr. Smith went to the store and bought 1,000.",
                "That is a lot."]),
        ('I think Jun. is a great month, said Mr. Suzuki.',
            ["I think Jun. is a great month, said Mr. Suzuki."]),
        ('Jun. is a great month, said Mr. Suzuki.',
            ["Jun. is a great month, said Mr. Suzuki."]),
        ("I have 1.000.00. Yay $.50 and .50! That's 600.",
            ["I have 1.000.00.", "Yay $.50 and .50!", "That's 600."]),
        ('1.) This is a list item with a parens.',
            ["1.) This is a list item with a parens."]),
        ('1. This is a list item.',
            ['1. This is a list item.']),
        ('I live in the U.S.A. I went to J.C. Penney.',
            ["I live in the U.S.A.", "I went to J.C. Penney."]),
        ('His name is Alfred E. Sloan.',
            ['His name is Alfred E. Sloan.']),
        ('Q. What is his name? A. His name is Alfred E. Sloan.',
            ['Q. What is his name?', 'A. His name is Alfred E. Sloan.']),
        ('Today is 11.18.2014.', ['Today is 11.18.2014.']),
        ('I need you to find 3 items, e.g. a hat, a coat, and a bag.',
            ['I need you to find 3 items, e.g. a hat, a coat, and a bag.']),
        ("The game is the Giants vs. the Tigers at 10 p.m. I'm going are you?",
            ["The game is the Giants vs. the Tigers at 10 p.m.", "I'm going are you?"]),
        ('He is no. 5, the shortstop.', ['He is no. 5, the shortstop.']),
        ("Remove long strings of dots........please.", ["Remove long strings of dots please."]),
        ("See our additional services section or contact us for pricing\n.\n\n\nPricing Additionl Info\n",
            ["See our additional services section or contact us for pricing.", "Pricing Additionl Info"]),
        ("As payment for 1. above, pay us a commission fee of 0 yen and for 2. above, no fee will be paid.",
            ["As payment for 1. above, pay us a commission fee of 0 yen and for 2. above, no fee will be paid."]),
        ("Git rid of   unnecessary white space.", ["Git rid of unnecessary white space."]),
        ("See our additional services section or contact us for pricing\n. Pricing Additionl Info",
            ["See our additional services section or contact us for pricing.", "Pricing Additionl Info"]),
        ("I have 600. How many do you have?",
            ["I have 600.", "How many do you have?"]),
        # modified original sents in pragmatic_segmenter are:
        # ["Introduction"]
        ("\n3\n\nIntroduction\n\n", ["3", "Introduction"]),
        ("\nW\nA\nRN\nI\nNG\n", ["WARNING"]),
        # modified original sents in pragmatic_segmenter are:
        # ["WARNING", "AVERTISEMENT"]
        ("\n\n\nW\nA\nRN\nI\nNG\n \n/\n \nA\nV\nE\nR\nT\nI\nS\nE\nM\nE\nNT\n",
            ["WARNING", "/", "AVERTISEMENT"]),
        ('"Help yourself, sweetie," shouted Candy and gave her the cookie.',
            ["\"Help yourself, sweetie,\" shouted Candy and gave her the cookie."]),
        ("Until its release, a generic mechanism was known, where the sear keeps the hammer in back position, and when one pulls the trigger, the sear slips out of hammer’s notches, the hammer falls initiating \na shot.",
            ["Until its release, a generic mechanism was known, where the sear keeps the hammer in back position, and when one pulls the trigger, the sear slips out of hammer’s notches, the hammer falls initiating a shot."]),
        ("This is a test. Until its release, a generic mechanism was known, where the sear keeps the hammer in back position, and when one pulls the trigger, the sear slips out of hammer’s notches, the hammer falls initiating \na shot.",
            ["This is a test.", "Until its release, a generic mechanism was known, where the sear keeps the hammer in back position, and when one pulls the trigger, the sear slips out of hammer’s notches, the hammer falls initiating a shot."]),
        ("This was because it was an offensive weapon, designed to fight at a distance up to 400 yd \n( 365.8 m ).",
            ["This was because it was an offensive weapon, designed to fight at a distance up to 400 yd ( 365.8 m )."]),
        ("“Are demonstrations are evidence of the public anger and frustration at opaque environmental management and decision-making?” Others yet say: \"Should we be scared about these 'protests'?\"",
            ["“Are demonstrations are evidence of the public anger and frustration at opaque environmental management and decision-making?”", "Others yet say: \"Should we be scared about these 'protests'?\""]),
        ("www.testurl.Awesome.com", ["www.testurl.Awesome.com"]),
        ("http://testurl.Awesome.com", ["http://testurl.Awesome.com"]),
        ("St. Michael's Church in is a church.", ["St. Michael's Church in is a church."]),
        ("JFK Jr.'s book is on sale.", ["JFK Jr.'s book is on sale."]),
        ("This is e.g. Mr. Smith, who talks slowly... And this is another sentence.",
            ["This is e.g. Mr. Smith, who talks slowly...", "And this is another sentence."]),
        ("Leave me alone!, he yelled. I am in the U.S. Army. Charles (Ind.) said he.",
            ["Leave me alone!, he yelled.", "I am in the U.S. Army.", "Charles (Ind.) said he."]),
        ("This is the U.S. Senate my friends. <em>Yes.</em> <em>It is</em>!",
            ["This is the U.S. Senate my friends.", "Yes.", "It is!"]),
        ("Send it to P.O. box 6554", ["Send it to P.O. box 6554"]),
        ("There were 500 cases in the U.S. The U.S. Commission asked the U.S. Government to give their opinion on the issue.",
            ["There were 500 cases in the U.S.", "The U.S. Commission asked the U.S. Government to give their opinion on the issue."]),
        ("CELLULAR COMMUNICATIONS INC. sold 1,550,000 common shares at $21.75 each yesterday, according to lead underwriter L.F. Rothschild & Co. (cited from WSJ 05/29/1987)",
            ["CELLULAR COMMUNICATIONS INC. sold 1,550,000 common shares at $21.75 each yesterday, according to lead underwriter L.F. Rothschild & Co. (cited from WSJ 05/29/1987)"]),
        ("Rolls-Royce Motor Cars Inc. said it expects its U.S. sales to remain steady at about 1,200 cars in 1990. `So what if you miss 50 tanks somewhere?' asks Rep. Norman Dicks (D., Wash.), a member of the House group that visited the talks in Vienna. Later, he recalls the words of his Marxist mentor: `The people! Theft! The holy fire!'",
            ["Rolls-Royce Motor Cars Inc. said it expects its U.S. sales to remain steady at about 1,200 cars in 1990.", "'So what if you miss 50 tanks somewhere?' asks Rep. Norman Dicks (D., Wash.), a member of the House group that visited the talks in Vienna.", "Later, he recalls the words of his Marxist mentor: 'The people! Theft! The holy fire!'"]),
        ("He climbed Mt. Fuji.", ["He climbed Mt. Fuji."]),
        ("He speaks !Xũ, !Kung, ǃʼOǃKung, !Xuun, !Kung-Ekoka, ǃHu, ǃKhung, ǃKu, ǃung, ǃXo, ǃXû, ǃXung, ǃXũ, and !Xun.",
            ["He speaks !Xũ, !Kung, ǃʼOǃKung, !Xuun, !Kung-Ekoka, ǃHu, ǃKhung, ǃKu, ǃung, ǃXo, ǃXû, ǃXung, ǃXũ, and !Xun."]),
        ("Test strange period．Does it segment correctly．",
            ["Test strange period．", "Does it segment correctly．"]),
        ("<h2 class=\"lined\">Hello</h2>\n<p>This is a test. Another test.</p>\n<div class=\"center\"><p>\n<img src=\"/images/content/example.jpg\">\n</p></div>",
            ["Hello", "This is a test.", "Another test."]),
        ("This sentence ends with the psuedo-number x10. This one with the psuedo-number %3.00. One last sentence.",
            ["This sentence ends with the psuedo-number x10.", "This one with the psuedo-number %3.00.", "One last sentence."]),
        ("Testing mixed numbers Jahr10. And another 0.3 %11. That's weird.",
            ["Testing mixed numbers Jahr10.", "And another 0.3 %11.", "That's weird."]),
        ("Were Jane and co. at the party?",
            ["Were Jane and co. at the party?"]),
        ("St. Michael's Church is on 5th st. near the light.",
            ["St. Michael's Church is on 5th st. near the light."]),
        ("Let's ask Jane and co. They should know.",
            ["Let's ask Jane and co.", "They should know."]),
        ("He works at Yahoo! and Y!J.",
            ["He works at Yahoo! and Y!J."]),
        ('The Scavenger Hunt ends on Dec. 31st, 2011.',
            ['The Scavenger Hunt ends on Dec. 31st, 2011.']),
        ("Putter King Scavenger Hunt Trophy\n(6 3/4\" Engraved Crystal Trophy - Picture Coming Soon)\nThe Putter King team will judge the scavenger hunt and all decisions will be final.  The scavenger hunt is open to anyone and everyone.  The scavenger hunt ends on Dec. 31st, 2011.",
            ["Putter King Scavenger Hunt Trophy", "(6 3/4\" Engraved Crystal Trophy - Picture Coming Soon)", "The Putter King team will judge the scavenger hunt and all decisions will be final.", "The scavenger hunt is open to anyone and everyone.", "The scavenger hunt ends on Dec. 31st, 2011."]),
        ("Unauthorized modifications, alterations or installations of or to this equipment are prohibited and are in violation of AR 750-10. Any such unauthorized modifications, alterations or installations could result in death, injury or damage to the equipment.",
            ["Unauthorized modifications, alterations or installations of or to this equipment are prohibited and are in violation of AR 750-10.", "Any such unauthorized modifications, alterations or installations could result in death, injury or damage to the equipment."]),
        ("Header 1.2; Attachment Z\n\n\td. Compliance Log – Volume 12 \n\tAttachment A\n\n\te. Additional Logistics Data\n\tSection 10",
            ["Header 1.2; Attachment Z", "d. Compliance Log – Volume 12", "Attachment A", "e. Additional Logistics Data", "Section 10"]),
        ("a.) The first item b.) The second item c.) The third list item",
            ["a.) The first item", "b.) The second item", "c.) The third list item"]),
        ("a) The first item b) The second item c) The third list item",
            ["a) The first item", "b) The second item", "c) The third list item"]),
        # ("Hello Wolrd. Here is a secret code AS750-10. Another sentence. Finally, this. 1. The first item 2. The second item 3. The third list item 4. Hello 5. Hello 6. Hello 7. Hello 8. Hello 9. Hello 10. Hello 11. Hello",
        # ["Hello Wolrd.", "Here is a secret code AS750-10.", "Another sentence.", "Finally, this.", "1. The first item", "2. The second item", "3. The third list item", "4. Hello", "5. Hello", "6. Hello", "7. Hello", "8. Hello", "9. Hello", "10. Hello", "11. Hello"])
        # ,
        # ("He works for ABC Ltd. and sometimes for BCD Ltd. She works for ABC Co. and BCD Co. They work for ABC Corp. and BCD Corp.",
        # ["He works for ABC Ltd. and sometimes for BCD Ltd.", "She works for ABC Co. and BCD Co.", "They work for ABC Corp. and BCD Corp."])
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
