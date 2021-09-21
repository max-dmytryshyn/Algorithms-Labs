import unittest
from .heap_sort import heap_sort
from copy import deepcopy


class TestHeapSor(unittest.TestCase):

    def setUp(self):
        self.array_sample = [1, 2, 56, 45, -9, 78, 11]
        self.sorted_in_asc = [-9, 1, 2, 11, 45, 56, 78]
        self.sorted_in_desc = [78, 56, 45, 11, 2, 1, -9]

    def test_sorting_in_asc(self):
        self.assertListEqual(heap_sort(deepcopy(self.array_sample), "asc"), self.sorted_in_asc)

    def test_sorting_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(self.array_sample), "desc"), self.sorted_in_desc)

    def test_sorting_asc_in_asc(self):
        self.assertListEqual(heap_sort(deepcopy(self.sorted_in_asc), "asc"), self.sorted_in_asc)

    def test_sorting_asc_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(self.sorted_in_asc), "desc"), self.sorted_in_desc)

    def test_sorting_desc_in_desc(self):
        self.assertListEqual(heap_sort(deepcopy(self.sorted_in_desc), "desc"), self.sorted_in_desc)

    def test_sorting_desc_in_asc(self):
        self.assertListEqual(heap_sort(deepcopy(self.sorted_in_desc), "asc"), self.sorted_in_asc)

