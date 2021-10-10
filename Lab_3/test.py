from hamsters import Hamster, max_hamsters_amount
import unittest


class TestFindMaxHamsterAmount(unittest.TestCase):

    def setUp(self):
        self.average_hamsters_1 = [Hamster(1, 2), Hamster(2, 2), Hamster(3, 1)]
        self.average_hamsters_2 = [Hamster(5, 0), Hamster(2, 2), Hamster(1, 4), Hamster(5, 1)]
        self.average_hamsters_3 = [Hamster(5, 0), Hamster(2, 2), Hamster(2, 4), Hamster(5, 1), Hamster(2, 1)]
        self.greedy_hamsters = [Hamster(1, 50000), Hamster(1, 60000)]

    def test_average_cases(self):
        self.assertEqual(max_hamsters_amount(self.average_hamsters_1, 7), 2)
        self.assertEqual(max_hamsters_amount(self.average_hamsters_2, 19), 3)
        self.assertEqual(max_hamsters_amount(self.average_hamsters_3, 30), 4)

    def test_greedy_case(self):
        self.assertEqual(max_hamsters_amount(self.greedy_hamsters, 100), 1)

    def test_no_hamsters(self):
        self.assertEqual(max_hamsters_amount(self.average_hamsters_3, 1), 0)

    def test_all_hamsters(self):
        self.assertEqual(max_hamsters_amount(self.average_hamsters_1, 100), 3)
        self.assertEqual(max_hamsters_amount(self.average_hamsters_2, 100), 4)
        self.assertEqual(max_hamsters_amount(self.average_hamsters_3, 100), 5)
