import pytest
import pysbd


SYNTOK_RULES = [('This is abcf. 123 here.', ['This is abcf. 123 here.']),
('This is abcf. (123) in here.', ['This is abcf. (123) in here.']),
('This is no. A13 here.', ['This is no. A13 here.']),
('Brackets before the terminal [2]. You know I told you so.', ['Brackets before the terminal [2].', 'You know I told you so.']),
('This is (Proc. ABC with Abs. Reg. Compliance) not here.', ['This is (Proc. ABC with Abs. Reg. Compliance) not here.']),
('This is (Proc. ABC with Abs. Reg. Compliance) not here.', ['This is (Proc. ABC with Abs. Reg. Compliance) not here.']),
('ET in the 112 ER+ patients (HR=2.79 for high CCNE1, p= .005 and .HR=1.97 for CCNE2, p= .05) is wrong.', ['ET in the 112 ER+ patients (HR=2.79 for high CCNE1, p= .005 and .HR=1.97 for CCNE2, p= .05) is wrong.']),
('This was shown by (A. Author et al.) a few months ago.', ['This was shown by (A. Author et al.) a few months ago.']),
('', []),
('Four patients (67%) with an average response of 3.3 mos. (range 6 wks. to 12 mos.)', ['Four patients (67%) with an average response of 3.3 mos. (range 6 wks. to 12 mos.)']),
('Packed cells (PRBC) for less than 20,000 thousand/micro.L, repsectively.', ['Packed cells (PRBC) for less than 20,000 thousand/micro.L, repsectively.']),
('This is Company Wag.B.H., truly.', ['This is Company Wag.B.H., truly.']),
('Specimens (n = 32) were sent for 16S rRNA PCR.', ['Specimens (n = 32) were sent for 16S rRNA PCR.']),
('I', ['I']),
('Who did this? I. No! Such a shame.', ['Who did this?', 'I. No!', 'Such a shame.']),
('operating at 2.4 GHz. Its power stage', ['operating at 2.4 GHz.', 'Its power stage']),
('got an A. And then he', ['got an A.', 'And then he']),
("Let's meet at 14.10 in N.Y.. This happened in the U.S. last week.", ["Let's meet at 14.10 in N.Y..", 'This happened in the U.S. last week.']),
('Donot splt., please!', ['Donot splt., please!']),
('The U.S. Air Force is here.', ['The U.S. Air Force is here.']),
("The basis for Lester B. Pearson's policy was later.", ["The basis for Lester B. Pearson's policy was later."]),
('got an A. Mathematics was', ['got an A. Mathematics was']),
("This is a sentence. 'This is another sentence.'", ['This is a sentence.', "'This is another sentence.'"]),
('I. This goes first. II. And here thereafter.', ['I. This goes first.', 'II. And here thereafter.']),
('1. This goes first. 2. And here thereafter.', ['1. This goes first.', '2. And here thereafter.']),
('A. This goes first. B. And here thereafter.', ['A. This goes first.', 'B. And here thereafter.']),
('This is Capt. Motto here. And here is Sra. Smithers.', ['This is Capt. Motto here.', 'And here is Sra. Smithers.']),
('This f. e. here. And here is unknwn. help.', ['This f. e. here.', 'And here is unknwn. help.']),
('This is Mr. Motto here. And here is Mrs. Smithers.', ['This is Mr. Motto here.', 'And here is Mrs. Smithers.']),
('This f.e. here. And here is med. help.', ['This f.e. here.', 'And here is med. help.']),
('Thisisasentence.', ['Thisisasentence.']),
('This is one. (Here is another view of the same. And then there is a different case here.)', ['This is one.', '(Here is another view of the same.', 'And then there is a different case here.)']),
('And another sentence on the same line. (How about a sentence in parenthesis?) Or a sentence with "a quote!"', ['And another sentence on the same line.', '(How about a sentence in parenthesis?)', 'Or a sentence with "a quote!"']),
('What the heck? (A) First things here.', ['What the heck?', '(A) First things here.']),
('resp.). Indicate', ['resp.).', 'Indicate']),
('in the E.U.. But they are', ['in the E.U..', 'But they are']),
('This is a sentence! This is another sentence!', ['This is a sentence!', 'This is another sentence!']),
('Is this a sentence? Is this another sentence?', ['Is this a sentence?', 'Is this another sentence?']),
('This is a sentence. This is another sentence.', ['This is a sentence.', 'This is another sentence.']),
('(This is a sentence.) This is another sentence.', ['(This is a sentence.)', 'This is another sentence.']),
('This is a sentence. (This is another sentence.)', ['This is a sentence.', '(This is another sentence.)']),
('{"This is a sentence."} ["This is another sentence."]', ['{"This is a sentence."}', '["This is another sentence."]']),
('"This is a sentence." "This is another sentence."', ['"This is a sentence."', '"This is another sentence."']),
('"This is a sentence." This is another sentence.', ['"This is a sentence."', 'This is another sentence.']),
('This is a sentence. "This is another sentence."', ['This is a sentence.', '"This is another sentence."']),
('I.', ['I.'])]

@pytest.mark.parametrize('text,expected_sents', SYNTOK_RULES)
def test_en_sbd_on_syntok_rules(text, expected_sents):
    """SBD tests from Pragmatic Segmenter"""
    segmenter = pysbd.Segmenter(language="en", clean=False, char_span=False)
    segments = segmenter.segment(text)
    assert segments == expected_sents
