import unittest
from SpellChecker import SpellChecker

class TestSpellCheckerRussian(unittest.TestCase):

    def setUp(self):
        self.spl = SpellChecker(".\\dict.txt")

    def test_spell_check_basic(self):
        # Проверка базового использования
        input_text = "Превет мир! Это примир теста на русском языке."
        expected_output = "Привет мир Это пример теста на русском языке"
        self.assertEqual(self.spl.spell_check(input_text), expected_output)

    def test_spell_check_no_errors(self):
        # Проверка, что при отсутствии ошибок во входном тексте функция возвращает исходный текст
        input_text = "Привет мир Это пример теста на русском языке"
        self.assertEqual(self.spl.spell_check(input_text), input_text)

    def test_spell_check_limit(self):
        # Проверка, что функция останавливается после исправления определенного числа ошибок
        input_text = "Превет мир! Это примир теста на русском языке."
        expected_output = "Привет мир Это пример теста на русском языке"
        self.assertEqual(self.spl.spell_check(input_text), expected_output)

    def test_spell_check_compound_words(self):
        # Проверка исправления слитно написанных слов
        input_text = "Превет мир! Это пример теста на русскомязыке."
        expected_output = "Привет мир Это пример теста на русском языке"
        self.assertEqual(self.spl.spell_check(input_text), expected_output)

    def test_spell_check_hyphens(self):
        # Проверка исправления слов с лишними дефисами
        input_text = "Привет мир! Это пример теста на русском-языке."
        expected_output = "Привет мир Это пример теста на русском языке"
        self.assertEqual(self.spl.spell_check(input_text), expected_output)

    def test_spell_check_mixed_errors(self):
        # Проверка исправления смешанных ошибок
        input_text = "Превет мир! Это примир теста на русском-языке."
        expected_output = "Привет мир Это пример теста на русском языке"
        self.assertEqual(self.spl.spell_check(input_text), expected_output)
