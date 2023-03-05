import unittest

from help_functioins import count_sentences, count_non_declarative, calc_average_sentence_length, \
    calc_average_word_length, calculate_top_k_repeated_n_grams


class TestCountingSentences(unittest.TestCase):

    def EmptyText(self):
        self.assertEqual(count_sentences(''), 0)

    def AbbreviationInText(self):
        self.assertEqual(count_sentences('Thank you, Mr. Chairman. It\'s a honor to meet you here. '), 2)

    def SeveralSymbols(self):
        self.assertEqual(count_sentences('Hello!!! How are you!?'), 2)


class TestCountingNonDeclarative(unittest.TestCase):
    def EmptyText(self):
        self.assertEqual(count_non_declarative(''), 0)

    def AbbreviationInText(self):
        self.assertEqual(count_non_declarative('Thank you, Mr. Chairman! It\'s a honor to meet you here. '), 1)

    def SeveralSymbols(self):
        self.assertEqual(count_non_declarative('Hello!!! How are you!?'), 2)


class TestCalculatingAverageSentenceLength(unittest.TestCase):
    def EmptyText(self):
        self.assertEqual(calc_average_sentence_length(''), 0)

    def AbbreviationInText(self):
        self.assertEqual(calc_average_sentence_length('Thank you, Mr. Chairman! It\'s a honor to meet you here. '), 20)

    def SeveralSymbols(self):
        self.assertEqual(calc_average_sentence_length('Hello!!! How are you!?'), 7)


class TestCalculatingAverageWordLength(unittest.TestCase):
    def EmptyText(self):
        self.assertEqual(calc_average_word_length(''), 0)

    def AbbreviationInText(self):
        self.assertEqual(calc_average_word_length('Thank you, Mr. Chairman! It\'s a honor to meet you here. '),
                         3.64)

    def SeveralSymbols(self):
        self.assertEqual(calc_average_word_length('Hello!!! How are you!?'), 3.5)


class TestCalculatingTopKNGrams(unittest.TestCase):
    def EmptyText(self):
        self.assertEqual(calculate_top_k_repeated_n_grams(''), 'n (4) is bigger than amount of words (0) in this text!')

    def Text(self):
        self.assertEqual(calculate_top_k_repeated_n_grams('This is a test file. It contains some text for testing. '
                                                          'This is a test file!'), [('This is a test', 2),
                                                                                    ('is a test file', 2),
                                                                                    ('a test file It', 1),
                                                                                    ('test file It contains', 1),
                                                                                    ('file It contains some', 1),
                                                                                    ('It contains some text', 1),
                                                                                    ('contains some text for', 1),
                                                                                    ('some text for testing', 1),
                                                                                    ('text for testing This', 1),
                                                                                    ('for testing This is', 1)])

