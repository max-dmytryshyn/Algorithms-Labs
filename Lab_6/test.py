from ijones import solve_ijones
import unittest


class TestIjonesSolution(unittest.TestCase):
    def setUp(self):
        self.w1 = 3
        self.h1 = 3
        self.corridor1 = [
            "aaa",
            "cab",
            "def"
        ]

        self.w2 = 10
        self.h2 = 1
        self.corridor2 = [
            "abcdefaghi"
        ]

        self.w3 = 7
        self.h3 = 6
        self.corridor3 = [
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa"
        ]

        self.w4 = 5
        self.h4 = 4
        self.corridor4 = [
            "fgbjo",
            "fmbjo",
            "fgbjo",
            "gbfhf",
            "dgdgd",
            "aaaaa"
        ]

    def test1(self):
        self.assertEqual(solve_ijones(self.w1, self.h1, self.corridor1), 5)

    def test2(self):
        self.assertEqual(solve_ijones(self.w2, self.h2, self.corridor2), 2)

    def test3(self):
        self.assertEqual(solve_ijones(self.w3, self.h3, self.corridor3), 201684)

    def test4(self):
        self.assertEqual(solve_ijones(self.w4, self.h4, self.corridor4), 14)

