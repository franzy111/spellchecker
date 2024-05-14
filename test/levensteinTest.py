import unittest
from SpellChecker import SpellChecker


class LevensteinTest(unittest.TestCase):
    def test_levenstein_same_word(self):
        distance = SpellChecker.levenstein("программирование", "программирование")
        self.assertEqual(distance, 0)

    def test_levenstein_insertion(self):
        distance = SpellChecker.levenstein("програмированиек", "программа")
        self.assertEqual(distance, 8)

    def test_levenstein_deletion(self):
        distance = SpellChecker.levenstein("программирование", "программированиек")
        self.assertEqual(distance, 1)

    def test_levenstein_substitution(self):
        distance = SpellChecker.levenstein("прогрессирование", "программирование")
        self.assertEqual(distance, 3)

    def test_levenstein_case_sensitive(self):
        distance = SpellChecker.levenstein("ПрограМмироВание", "программирование")
        self.assertEqual(distance, 3)

    def test_levenstein_empty_strings(self):
        distance = SpellChecker.levenstein("программирование", "")
        self.assertEqual(distance, 16)


if __name__ == "__main__":
    unittest.main()
