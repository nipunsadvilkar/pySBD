import pytest
import pysbd
from unittest import TestCase

import syntok.segmenter as segmenter
from syntok.tokenizer import Token, Tokenizer

TOKENIZER = Tokenizer()

def make_sentences(segmented_tokens):
    for sentence in segmented_tokens:
        yield "".join(str(token) for token in sentence).strip()


class TestSegmenter(TestCase):
    def test_simple(self):
        tokens = list(
            map(lambda v: Token("", v, 0), ["This", "is", "a", "sentence", "."])
        )
        # noinspection PyTypeChecker
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_empty(self):
        tokens = []
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([], result)

    def test_one_token(self):
        tokens = [Token("", "I", 0)]
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_two_tokens(self):
        tokens = [Token("", "I", 0), Token("", ".", 1)]
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_two_sentences(self):
        tokens = Tokenizer().split("This is a sentence. This is another sentence.")
        sep = 5
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_two_exclamations(self):
        tokens = Tokenizer().split("This is a sentence! This is another sentence!")
        sep = 5
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_two_questions(self):
        tokens = Tokenizer().split("Is this a sentence? Is this another sentence?")
        sep = 5
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_two_sentences_with_parenthesis_in_second(self):
        tokens = Tokenizer().split("This is a sentence. (This is another sentence.)")
        sep = 5
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_two_sentences_with_parenthesis_in_first(self):
        tokens = Tokenizer().split("(This is a sentence.) This is another sentence.")
        sep = 7
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_two_sentences_with_quotes_in_second(self):
        tokens = Tokenizer().split('This is a sentence. "This is another sentence."')
        sep = 5
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentence_with_single_quotes(self):
        tokens = Tokenizer().split("This is a sentence. 'This is another sentence.'")
        sep = 5
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_two_sentences_with_quotes_in_first(self):
        tokens = Tokenizer().split('"This is a sentence." This is another sentence.')
        sep = 7
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_two_sentences_with_quotes_in_both(self):
        tokens = Tokenizer().split('"This is a sentence." "This is another sentence."')
        sep = 7
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_two_sentences_with_quotes_and_prenthesis_in_both(self):
        tokens = Tokenizer().split(
            '{"This is a sentence."} ["This is another sentence."]'
        )
        sep = 9
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentences_with_simple_abbreviations(self):
        tokens = Tokenizer().split("This is Mr. Motto here. And here is Mrs. Smithers.")
        sep = 7
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentences_with_nasty_abbreviations(self):
        tokens = Tokenizer().split(
            "This is Capt. Motto here. And here is Sra. Smithers."
        )
        sep = 7
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentences_with_special_abbreviations(self):
        tokens = Tokenizer().split("This f.e. here. And here is med. help.")
        sep = 5
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentences_with_nasty_special_abbreviations(self):
        tokens = Tokenizer().split("This f. e. here. And here is unknwn. help.")
        sep = 7
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentences_with_enumerations(self):
        tokens = Tokenizer().split("1. This goes first. 2. And here thereafter.")
        sep = 6
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentences_with_letter_enumerations(self):
        tokens = Tokenizer().split("A. This goes first. B. And here thereafter.")
        sep = 6
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentences_with_Roman_enumerations(self):
        tokens = Tokenizer().split("I. This goes first. II. And here thereafter.")
        sep = 6
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_one_word_sentences(self):
        tokens = Tokenizer().split("Who did this? I. No! Such a shame.")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:4], tokens[4:8], tokens[8:]], result)

    def test_brackets_before_the_terminal(self):
        tokens = Tokenizer().split(
            "Brackets before the terminal [2]. You know I told you so."
        )
        sep = 8
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentence_marker_after_abbreviation(self):
        tokens = Tokenizer().split(
            "Let's meet at 14.10 in N.Y.. This happened in the U.S. last week."
        )
        sep = 9
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentence_ends_in_abbreviation(self):
        tokens = Tokenizer().split("operating at 2.4 GHz. Its power stage")
        sep = 5
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentence_ends_in_single_letter_and_starts_with_starter_word(self):
        tokens = Tokenizer().split("got an A. And then he")
        sep = 4
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_split_with_dot_following_abbreviation(self):
        tokens = Tokenizer().split("in the E.U.. But they are")
        sep = 5
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_split_with_complext_abbreviation_pattern(self):
        tokens = Tokenizer().split("resp.). Indicate")
        sep = 4
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_sentence_with_abbreviation_indictated_by_punctuation(self):
        tokens = Tokenizer().split("Don't splt., please!")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_sentence_with_abbreviation_with_dot(self):
        tokens = Tokenizer().split("The U.S. Air Force is here.")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_sentence_with_single_letter_abbreviation(self):
        tokens = Tokenizer().split(
            "The basis for Lester B. Pearson's policy was later."
        )
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_sentence_with_single_letter_at_end(self):
        # Sadly, this one cannot split if we want to capture author abbreviations
        tokens = Tokenizer().split("got an A. Mathematics was")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_abbreviation_followed_by_large_number(self):
        tokens = Tokenizer().split("This is abcf. 123 here.")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_abbreviation_no_followed_by_alnum_token(self):
        tokens = Tokenizer().split("This is no. A13 here.")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_abbreviation_followed_by_parenthesis(self):
        tokens = Tokenizer().split("This is abcf. (123) in here.")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_do_not_split_short_text_inside_parenthesis(self):
        tokens = Tokenizer().split(
            "This is (Proc. ABC with Abs. Reg. Compliance) not here."
        )
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_do_not_split_short_text_inside_parenthesis2(self):
        tokens = Tokenizer().split(
            "This is (Proc. ABC with Abs. Reg. Compliance) not here."
        )
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_do_not_split_short_text_inside_parenthesis3(self):
        tokens = Tokenizer().split(
            "ET in the 112 ER+ patients (HR=2.79 for high CCNE1, p= .005 and .HR=1.97 for CCNE2, p= .05) is wrong."
        )
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_do_not_split_short_text_inside_parenthesis4(self):
        tokens = Tokenizer().split(
            "This was shown by (A. Author et al.) a few months ago."
        )
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_split_long_text_inside_parenthesis(self):
        tokens = Tokenizer().split(
            "This is one. (Here is another view of the same. And then there is a different case here.)"
        )
        sep1 = 4
        sep2 = 13
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep1], tokens[sep1:sep2], tokens[sep2:]], result)

    def test_split_long_text_inside_parenthesis2(self):
        tokens = Tokenizer().split(
            "This is one (Here is another view of the same. And then there is a different case here.)"
        )
        sep1 = 3
        sep2 = 12
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep1], tokens[sep1:sep2], tokens[sep2:]], result)

    def test_split_with_complex_parenthesis_structure(self):
        tokens = Tokenizer().split("What the heck? (A) First things here.")
        sep = 4
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep], tokens[sep:]], result)

    def test_split_with_a_simple_parenthesis_structure(self):
        tokens = Tokenizer().split(
            "And another sentence on the same line. "
            "(How about a sentence in parenthesis?) "
            'Or a sentence with "a quote!"'
        )
        sep1 = 8
        sep2 = 17
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens[:sep1], tokens[sep1:sep2], tokens[sep2:]], result)

    def test_no_split_with_simple_inner_bracketed_text(self):
        tokens = Tokenizer().split("Specimens (n = 32) were sent for 16S rRNA PCR.")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_no_split_on_strange_text(self):
        tokens = Tokenizer().split("Four patients (67%) with an average response of 3.3 mos. (range 6 wks. to 12 mos.)")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_no_split_on_strange_text2(self):
        tokens = Tokenizer().split("Packed cells (PRBC) for less than 20,000 thousand/micro.L, repsectively.")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)

    def test_no_split_on_strange_text3(self):
        tokens = Tokenizer().split("This is Company Wag.B.H., truly.")
        result = segmenter.split(iter(tokens))
        output = [sent for sent in make_sentences(result)]
        print((" ".join(output), output))
        self.assertEqual([tokens], result)
