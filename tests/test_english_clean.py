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
        ("Hello Wolrd. Here is a secret code AS750-10. Another sentence. Finally, this. 1. The first item 2. The second item 3. The third list item 4. Hello 5. Hello 6. Hello 7. Hello 8. Hello 9. Hello 10. Hello 11. Hello",
            ["Hello Wolrd.", "Here is a secret code AS750-10.", "Another sentence.", "Finally, this.", "1. The first item", "2. The second item", "3. The third list item", "4. Hello", "5. Hello", "6. Hello", "7. Hello", "8. Hello", "9. Hello", "10. Hello", "11. Hello"]),
        ("He works for ABC Ltd. and sometimes for BCD Ltd. She works for ABC Co. and BCD Co. They work for ABC Corp. and BCD Corp.",
            ["He works for ABC Ltd. and sometimes for BCD Ltd.", "She works for ABC Co. and BCD Co.", "They work for ABC Corp. and BCD Corp."]),
        ("<bpt i=\"0\" type=\"bold\">&lt;b&gt;</bpt>J1.txt<ept i=\"1\">&lt;/b&gt;</ept>", ["J1.txt"]),
        ("On Jan. 20, former Sen. Barack Obama became the 44th President of the U.S. Millions attended the Inauguration.",
            ["On Jan. 20, former Sen. Barack Obama became the 44th President of the U.S.", "Millions attended the Inauguration."]),
        ("The U.K. Panel on enivronmental issues said it was true. Finally he left the U.K. He went to a new location.",
            ["The U.K. Panel on enivronmental issues said it was true.", "Finally he left the U.K.", "He went to a new location."]),
        ("He left at 6 P.M. Travelers who didn't get the warning at 5 P.M. left later.",
            ["He left at 6 P.M.", "Travelers who didn't get the warning at 5 P.M. left later."]),
        ("He left at 6 a.m. Travelers who didn't get the warning at 5 a.m. left later.",
            ["He left at 6 a.m.", "Travelers who didn't get the warning at 5 a.m. left later."]),
        ("He left at 6 A.M. Travelers who didn't get the warning at 5 A.M. left later.",
            ["He left at 6 A.M.", "Travelers who didn't get the warning at 5 A.M. left later."]),
        # failing since lots of sentence. # TODO Debug once all tests pass

        # ("Hello World. My name is Jonas. What is your name? My name is Jonas. There it is! I found it. My name is Jonas E. Smith. Please turn to p. 55. Were Jane and co. at the party? They closed the deal with Pitt, Briggs & Co. at noon. Let's ask Jane and co. They should know. They closed the deal with Pitt, Briggs & Co. It closed yesterday. I can see Mt. Fuji from here. St. Michael's Church is on 5th st. near the light. That is JFK Jr.'s book. I visited the U.S.A. last year. I live in the E.U. How about you? I live in the U.S. How about you? I work for the U.S. Government in Virginia. I have lived in the U.S. for 20 years. She has $100.00 in her bag. She has $100.00. It is in her bag. He teaches science (He previously worked for 5 years as an engineer.) at the local University. Her email is Jane.Doe@example.com. I sent her an email. The site is: https://www.example.50.com/new-site/awesome_content.html. Please check it out. She turned to him, 'This is great.' she said. She turned to him, \"This is great.\" she said. She turned to him, \"This is great.\" She held the book out to show him. Hello!! Long time no see. Hello?? Who is there? Hello!? Is that you? Hello?! Is that you? 1.) The first item 2.) The second item 1.) The first item. 2.) The second item. 1) The first item 2) The second item 1) The first item. 2) The second item. 1. The first item 2. The second item 1. The first item. 2. The second item. • 9. The first item • 10. The second item ⁃9. The first item ⁃10. The second item a. The first item b. The second item c. The third list item \rIt was a cold \nnight in the city. features\ncontact manager\nevents, activities\n You can find it at N°. 1026.253.553. That is where the treasure is. She works at Yahoo! in the accounting department. We make a good team, you and I. Did you see Albert I. Jones yesterday? Thoreau argues that by simplifying one’s life, “the laws of the universe will appear less complex. . . .”. \"Bohr [...] used the analogy of parallel stairways [...]\" (Smith 55). If words are left off at the end of a sentence, and that is all that is omitted, indicate the omission with ellipsis marks (preceded and followed by a space) and then indicate the end of the sentence with a period . . . . Next sentence. I never meant that.... She left the store. I wasn’t really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn’t mean it. One further habit which was somewhat weakened . . . was that of combining words into self-interpreting compounds. . . . The practice was not abandoned. . . .",
        #     ["Hello World.", "My name is Jonas.", "What is your name?", "My name is Jonas.", "There it is!", "I found it.", "My name is Jonas E. Smith.", "Please turn to p. 55.", "Were Jane and co. at the party?", "They closed the deal with Pitt, Briggs & Co. at noon.", "Let's ask Jane and co.", "They should know.", "They closed the deal with Pitt, Briggs & Co.", "It closed yesterday.", "I can see Mt. Fuji from here.", "St. Michael's Church is on 5th st. near the light.", "That is JFK Jr.'s book.", "I visited the U.S.A. last year.", "I live in the E.U.", "How about you?", "I live in the U.S.", "How about you?", "I work for the U.S. Government in Virginia.", "I have lived in the U.S. for 20 years.", "She has $100.00 in her bag.", "She has $100.00.", "It is in her bag.", "He teaches science (He previously worked for 5 years as an engineer.) at the local University.", "Her email is Jane.Doe@example.com.", "I sent her an email.", "The site is: https://www.example.50.com/new-site/awesome_content.html.", "Please check it out.", "She turned to him, 'This is great.' she said.", "She turned to him, \"This is great.\" she said.", "She turned to him, \"This is great.\"", "She held the book out to show him.", "Hello!!", "Long time no see.", "Hello??", "Who is there?", "Hello!?", "Is that you?", "Hello?!", "Is that you?", "1.) The first item", "2.) The second item", "1.) The first item.", "2.) The second item.", "1) The first item", "2) The second item", "1) The first item.", "2) The second item.", "1. The first item", "2. The second item", "1. The first item.", "2. The second item.", "• 9. The first item", "• 10. The second item", "⁃9. The first item", "⁃10. The second item", "a. The first item", "b. The second item", "c. The third list item", "It was a cold night in the city.", "features", "contact manager", "events, activities", "You can find it at N°. 1026.253.553.", "That is where the treasure is.", "She works at Yahoo! in the accounting department.", "We make a good team, you and I.", "Did you see Albert I. Jones yesterday?", "Thoreau argues that by simplifying one’s life, “the laws of the universe will appear less complex. . . .”.", "\"Bohr [...] used the analogy of parallel stairways [...]\" (Smith 55).", "If words are left off at the end of a sentence, and that is all that is omitted, indicate the omission with ellipsis marks (preceded and followed by a space) and then indicate the end of the sentence with a period . . . .", "Next sentence.", "I never meant that....", "She left the store.", "I wasn’t really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn’t mean it.", "One further habit which was somewhat weakened . . . was that of combining words into self-interpreting compounds.", ". . . The practice was not abandoned. . . ."]),

        ("His name is Mark E. Smith. a. here it is b. another c. one more\n They went to the store. It was John A. Smith. She was Jane B. Smith.",
            ["His name is Mark E. Smith.", "a. here it is", "b. another", "c. one more", "They went to the store.", "It was John A. Smith.", "She was Jane B. Smith."]),
        ("Hello{b^&gt;1&lt;b^} hello{b^>1<b^}.", ["Hello hello."]),
        ("'Well?' thought Alice to herself, 'after such a fall as this, I shall think nothing of tumbling down stairs? How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)",
            ["'Well?' thought Alice to herself, 'after such a fall as this, I shall think nothing of tumbling down stairs? How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)"]),
        ("Leave me alone! he yelled. I am in the U.S. Army. Charles (Ind.) said he.",
            ["Leave me alone! he yelled.", "I am in the U.S. Army.", "Charles (Ind.) said he."]),
        ("She turned to him, “This is great.” She held the book out to show him.",
            ["She turned to him, “This is great.”", "She held the book out to show him."]),
        ("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////Header starts here\r////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////",
            ["Header starts here"]),
        ('Hello World. \r\n Hello.',
            ["Hello World.", "Hello."]),
        ("a) here it is b) another c) one more\n They went to the store. w) hello x) hello y) hello",
            ["a) here it is", "b) another", "c) one more", "They went to the store.", "w) hello",  "x) hello",  "y) hello"]),

        # ('Hello World. \ r \ nHello.',
        #     ["Hello World.", "Hello."]),
        # ("The nurse gave him the i.v. in his vein. She gave him the i.v. It was a great I.V. that she gave him. She gave him the I.V. It was night.",
        #     ["The nurse gave him the i.v. in his vein.", "She gave him the i.v.", "It was a great I.V. that she gave him.", "She gave him the I.V.", "It was night."])

        # ("(i) Hello world. \n(ii) Hello world.\n(iii) Hello world.\n(iv) Hello world.\n(v) Hello world.\n(vi) Hello world.",
        #     ["(i) Hello world.", "(ii) Hello world.", "(iii) Hello world.", "(iv) Hello world.", "(v) Hello world.", "(vi) Hello world."]),
        ("i) Hello world. \nii) Hello world.\niii) Hello world.\niv) Hello world.\nv) Hello world.\nvi) Hello world.",
            ["i) Hello world.", "ii) Hello world.", "iii) Hello world.", "iv) Hello world.", "v) Hello world.", "vi) Hello world."]),
        # ("(a) Hello world. (b) Hello world. (c) Hello world. (d) Hello world. (e) Hello world.\n(f) Hello world.",
        #     ["(a) Hello world.", "(b) Hello world.", "(c) Hello world.", "(d) Hello world.", "(e) Hello world.", "(f) Hello world."]),
        ("(A) Hello world. \n(B) Hello world.\n(C) Hello world.\n(D) Hello world.\n(E) Hello world.\n(F) Hello world.",
            ["(A) Hello world.", "(B) Hello world.", "(C) Hello world.", "(D) Hello world.", "(E) Hello world.", "(F) Hello world."]),
        ("A) Hello world. \nB) Hello world.\nC) Hello world.\nD) Hello world.\nE) Hello world.\nF) Hello world.",
            ["A) Hello world.", "B) Hello world.", "C) Hello world.", "D) Hello world.", "E) Hello world.", "F) Hello world."]),
        ("The GmbH & Co. KG is a limited partnership with, typically, the sole general partner being a limited liability company.",
            ["The GmbH & Co. KG is a limited partnership with, typically, the sole general partner being a limited liability company."]),
        # ("[?][footnoteRef:6] This is a footnote.",
        #     ["[?][footnoteRef:6] This is a footnote."]),
        # ("[15:  12:32]  [16:  firma? 13:28]",
        #     ["[15:  12:32]  [16:  firma? 13:28]"]),
        ("\"It's a good thing that the water is really calm,\" I answered ironically.",
            ["\"It's a good thing that the water is really calm,\" I answered ironically."]),
        ("December 31, 1988. Hello world. It's great! \nBorn April 05, 1989.",
            ["December 31, 1988.", "Hello world.", "It's great!", "Born April 05, 1989."]),

        ####################
        # add big text test#
        ####################
        ("\"Dear, dear! How queer everything is to-day! And yesterday things went on just as usual. _Was_ I the same when I got up this morning? But if I'm not the same, the next question is, 'Who in the world am I?' Ah, _that's_ the great puzzle!\"",
            ["\"Dear, dear! How queer everything is to-day! And yesterday things went on just as usual. _Was_ I the same when I got up this morning? But if I'm not the same, the next question is, 'Who in the world am I?' Ah, _that's_ the great puzzle!\""]),
        # ("Two began, in a low voice, \"Why, the fact is, you see, Miss, this here ought to have been a _red_ rose-tree, and we put a white one in by mistake; and, if the Queen was to find it out, we should all have our heads cut off, you know. So you see, Miss, we're doing our best, afore she comes, to--\" At this moment, Five, who had been anxiously looking across the garden, called out, \"The Queen! The Queen!\" and the three gardeners instantly threw themselves flat upon their faces.",
        #     ["Two began, in a low voice, \"Why, the fact is, you see, Miss, this here ought to have been a _red_ rose-tree, and we put a white one in by mistake; and, if the Queen was to find it out, we should all have our heads cut off, you know. So you see, Miss, we're doing our best, afore she comes, to--\"", "At this moment, Five, who had been anxiously looking across the garden, called out, \"The Queen! The Queen!\" and the three gardeners instantly threw themselves flat upon their faces."]),
        ("\"Dinah'll miss me very much to-night, I should think!\" (Dinah was the cat.) \"I hope they'll remember her saucer of milk at tea-time. Dinah, my dear, I wish you were down here with me!\"",
            ["\"Dinah'll miss me very much to-night, I should think!\"", "(Dinah was the cat.)", "\"I hope they'll remember her saucer of milk at tea-time. Dinah, my dear, I wish you were down here with me!\""]),
        ("Hello. 'This is a test of single quotes.' A new sentence.",
            ["Hello.", "'This is a test of single quotes.'", "A new sentence."]),
        # ("[A sentence in square brackets.]", ["[A sentence in square brackets.]"]),
        # ("(iii) List item number 3.", ["(iii) List item number 3."])

        # ("(iii) List item number 3.",
        #     ["(iii) List item number 3."])

        # ("Unbelievable??!?!", ["Unbelievable??!?!"]),
        ("This abbreviation f.e. means for example.",
            ["This abbreviation f.e. means for example."]),
        ("The med. staff here is very kind.",
            ["The med. staff here is very kind."]),
        ("What did you order btw., she wondered.",
            ["What did you order btw., she wondered."]),
        ("SEC. 1262 AUTHORIZATION OF APPROPRIATIONS.",
            ["SEC. 1262 AUTHORIZATION OF APPROPRIATIONS."]),
        ("a", ["a"]),
        ("I wrote this in the 'nineties.  It has four sentences.  This is the third, isn't it?  And this is the last",
            ["I wrote this in the 'nineties.", "It has four sentences.", "This is the third, isn't it?", "And this is the last"]),
        ("I wrote this in the ’nineties.  It has four sentences.  This is the third, isn't it?  And this is the last",
            ["I wrote this in the ’nineties.", "It has four sentences.", "This is the third, isn't it?", "And this is the last"]),

        ("Unlike the abbreviations i.e. and e.g., viz. is used to indicate a detailed description of something stated before.",
            ["Unlike the abbreviations i.e. and e.g., viz. is used to indicate a detailed description of something stated before."]),

        ("For example, ‘dragonswort… is said that it should be grown in dragon’s blood. It grows at the tops of mountains where there are groves of trees, chiefly in holy places and in the country that is called Apulia’ (translated by Anne Van Arsdall, in Medieval Herbal Remedies: The Old English Herbarium and Anglo-Saxon Medicine p. 154). The Herbal also includes lore about other plants, such as the mandrake.",
            ["For example, ‘dragonswort… is said that it should be grown in dragon’s blood. It grows at the tops of mountains where there are groves of trees, chiefly in holy places and in the country that is called Apulia’ (translated by Anne Van Arsdall, in Medieval Herbal Remedies: The Old English Herbarium and Anglo-Saxon Medicine p. 154).", "The Herbal also includes lore about other plants, such as the mandrake."]),

        # ("Here’s the - ahem - official citation: Baker, C., Anderson, Kenneth, Martin, James, & Palen, Leysia. Modeling Open Source Software Communities, ProQuest Dissertations and Theses.",
        #     ["Here’s the - ahem - official citation: Baker, C., Anderson, Kenneth, Martin, James, & Palen, Leysia.", "Modeling Open Source Software Communities, ProQuest Dissertations and Theses."])

        ("These include images of various modes of transport and members of the team, all available in .jpeg format. Images can be downloaded from our website. We also offer archives as .zip files.",
            ["These include images of various modes of transport and members of the team, all available in .jpeg format.", "Images can be downloaded from our website.", "We also offer archives as .zip files."]),

        # ("Saint Maximus (died 250) is a Christian saint and martyr.[1] The emperor Decius published a decree ordering the veneration of busts of the deified emperors.",
        #     ["Saint Maximus (died 250) is a Christian saint and martyr.[1]", "The emperor Decius published a decree ordering the veneration of busts of the deified emperors."])

        # ("Differing agendas can potentially create an understanding gap in a consultation.11 12 Take the example of one of the most common presentations in ill health: the common cold.",
        #     ["Differing agendas can potentially create an understanding gap in a consultation.11 12", "Take the example of one of the most common presentations in ill health: the common cold."])

        # ("Daniel Kahneman popularised the concept of fast and slow thinking: the distinction between instinctive (type 1 thinking) and reflective, analytical cognition (type 2).10 This model relates to doctors achieving a balance between efficiency and effectiveness.",
        #     ["Daniel Kahneman popularised the concept of fast and slow thinking: the distinction between instinctive (type 1 thinking) and reflective, analytical cognition (type 2).10", "This model relates to doctors achieving a balance between efficiency and effectiveness."])

        ("Its traditional use[1] is well documented in the ethnobotanical literature [2–11]. Leaves, buds, tar and essential oils are used to treat a wide spectrum of diseases.",
            ["Its traditional use[1] is well documented in the ethnobotanical literature [2–11].", "Leaves, buds, tar and essential oils are used to treat a wide spectrum of diseases."]),
        # ("Thus increasing the desire for political reform both in Lancashire and in the country at large.[7][8] This was a serious misdemeanour,[16] encouraging them to declare the assembly illegal as soon as it was announced on 31 July.[17][18] The radicals sought a second opinion on the meeting's legality.",
        #     ["Thus increasing the desire for political reform both in Lancashire and in the country at large.[7][8]", "This was a serious misdemeanour,[16] encouraging them to declare the assembly illegal as soon as it was announced on 31 July.[17][18]", "The radicals sought a second opinion on the meeting's legality."]),
        # ("The table in (4) is a sample from the Wall Street Journal (1987).1 According to the distribution all the pairs given in (4) count as candidates for abbreviations.",
        #     [ "The table in (4) is a sample from the Wall Street Journal (1987).1", "According to the distribution all the pairs given in (4) count as candidates for abbreviations."])
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

TESTS_WO_CLEAN = [
        ("He has Ph.D.-level training", ["He has Ph.D.-level training"]),

        # set clean=False
        ("He has Ph.D. level training", ["He has Ph.D. level training"]),

        # set clean=False
        ("I will be paid Rs. 16720/- in total for the time spent and the inconvenience caused to me, only after completion of all aspects of the study.",
            ["I will be paid Rs. 16720/- in total for the time spent and the inconvenience caused to me, only after completion of all aspects of the study."]),

        # set clean=False
        ("If I decide to withdraw from the study for other reasons, I will be paid only up to the extent of my participation amount according to the approved procedure of Apotex BEC. If I complete all aspects in Period 1, I will be paid Rs. 3520 and if I complete all aspects in Period 1 and Period 2, I will be paid Rs. 7790 and if I complete all aspects in Period 1, Period 2 and Period 3, I will be paid Rs. 12060 at the end of the study.",
            ["If I decide to withdraw from the study for other reasons, I will be paid only up to the extent of my participation amount according to the approved procedure of Apotex BEC.", "If I complete all aspects in Period 1, I will be paid Rs. 3520 and if I complete all aspects in Period 1 and Period 2, I will be paid Rs. 7790 and if I complete all aspects in Period 1, Period 2 and Period 3, I will be paid Rs. 12060 at the end of the study."]),

        # set clean=False
        ("After completion of each Period, I will be paid an advance amount of rs. 1000 and this amount will be deducted from my final study compensation.",
            ["After completion of each Period, I will be paid an advance amount of rs. 1000 and this amount will be deducted from my final study compensation."]),

        # set clean=False
        ("Mix it, put it in the oven, and -- voila! -- you have cake.",
            ["Mix it, put it in the oven, and -- voila! -- you have cake."]),

        # set clean=False
        ("Some can be -- if I may say so? -- a bit questionable.",
            ["Some can be -- if I may say so? -- a bit questionable."]),

        # set clean=False
        ("What do you see? - Posted like silent sentinels all around the town, stand thousands upon thousands of mortal men fixed in ocean reveries.",
            ["What do you see?", "- Posted like silent sentinels all around the town, stand thousands upon thousands of mortal men fixed in ocean reveries."]),

        # set clean=False
        ("In placebo-controlled studies of all uses of Tracleer, marked decreases in hemoglobin (>15% decrease from baseline resulting in values <11 g/ dL) were observed in 6% of Tracleer-treated patients and 3% of placebo-treated patients. Bosentan is highly bound (>98%) to plasma proteins, mainly albumin.",
            ["In placebo-controlled studies of all uses of Tracleer, marked decreases in hemoglobin (>15% decrease from baseline resulting in values <11 g/ dL) were observed in 6% of Tracleer-treated patients and 3% of placebo-treated patients.", "Bosentan is highly bound (>98%) to plasma proteins, mainly albumin."]),

        # set clean=False
        ("The parties to this Agreement are PragmaticSegmenterExampleCompanyA Inc. (“Company A”), and PragmaticSegmenterExampleCompanyB Inc. (“Company B”).",
            ["The parties to this Agreement are PragmaticSegmenterExampleCompanyA Inc. (“Company A”), and PragmaticSegmenterExampleCompanyB Inc. (“Company B”)."])
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

@pytest.mark.parametrize('text,expected_sents', TESTS_WO_CLEAN)
def test_en_sbd_wo_clean(text, expected_sents):
    """SBD tests from Pragmatic Segmenter without cleaning"""
    seg = pySBD.Segmenter(text, clean=False)
    segments = seg.segment()
    assert segments == expected_sents
