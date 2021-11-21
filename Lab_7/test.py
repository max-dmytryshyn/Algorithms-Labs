from rabin_karp import rabin_karp
import unittest


class TestRabinKarp(unittest.TestCase):
    def setUp(self):
        self.text_1 = "abcaamabcaamdfethg"
        self.pattern_1_1 = "abc"
        self.pattern_1_2 = "aam"
        self.pattern_1_3 = "mab"
        self.text_2 = "rybybyb aboba yb"
        self.pattern_2_1 = "yb"
        self.pattern_2_2 = "byb"
        self.not_matchable_pattern = "Max"

    def test_1(self):
        self.assertTupleEqual(rabin_karp(self.text_1, self.pattern_1_1), (0, 6))

    def test_2(self):
        self.assertTupleEqual(rabin_karp(self.text_1, self.pattern_1_2), (3, 9))

    def test_3(self):
        self.assertTupleEqual(rabin_karp(self.text_1, self.pattern_1_3), tuple([5]))

    def test_4(self):
        self.assertTupleEqual(rabin_karp(self.text_2, self.pattern_2_1), (1, 3, 5, 14))

    def test_5(self):
        self.assertTupleEqual(rabin_karp(self.text_2, self.pattern_2_2), (2, 4))

    def test_no_matches(self):
        self.assertTupleEqual(rabin_karp(self.text_1, self.not_matchable_pattern), ())
