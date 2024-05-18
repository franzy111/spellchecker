import unittest
from SpellChecker import SpellChecker


class CheckingHyphensTest(unittest.TestCase):
    def setUp(self):
        self.spl = SpellChecker("..//dict.txt")

    def test_no_hyphens_words(self):
        word = "большой"
        self.assertTrue(self.spl.check_for_hyphens(word))

    def test_hyphens_words1(self):
        word = "-хочумост-"
        self.assertFalse(self.spl.check_for_hyphens(word))

    def test_hyphens_words2(self):
        word = "большой-мост"
        self.assertTrue(self.spl.check_for_hyphens(word))

    def test_hyphens_words3(self):
        word = "большой-пэ"
        self.assertFalse(self.spl.check_for_hyphens(word))

    def test_empty_word(self):
        word = ""
        self.assertEqual(word, self.spl.check_compound_words(word))


if __name__ == "__main__":
    unittest.main()
