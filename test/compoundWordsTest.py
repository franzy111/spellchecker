import unittest
from SpellChecker import SpellChecker


class CompoundWordsTest(unittest.TestCase):
    def setUp(self):
        self.spl = SpellChecker("C:/Users/User/PycharmProjects/spellchecker/dict.txt")

    def test_no_compound_words(self):
        word = "большой"
        self.assertEqual(word, self.spl.check_compound_words(word))

    def test_compound_words1(self):
        word = "хочумост"
        expected = "хочу мост"
        self.assertEqual(expected, self.spl.check_compound_words(word))

    def test_compound_words2(self):
        word = "большойпёсик"
        expected = "большой пёсик"
        self.assertEqual(expected, self.spl.check_compound_words(word))

    def test_compound_words3(self):
        word = "большойпёсиклесзалноги"
        expected = "большой пёсик лес зал ноги"
        self.assertEqual(expected, self.spl.check_compound_words(word))

    def test_empty_word(self):
        word = ""
        self.assertEqual(word, self.spl.check_compound_words(word))


if __name__ == "__main__":
    unittest.main()
