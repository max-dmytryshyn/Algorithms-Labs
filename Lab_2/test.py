import unittest
from hash_table import HashTable
from copy import deepcopy


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.keys = ["key1", "key2", "key3", "key4", "key5", "key6", "key7", "key8"]
        self.values = ["value1", "value2", "value3", "value4", "value5", "value6", "value7", "value8"]
        self.hash_table = HashTable(2)
        self.dictionary = {self.keys[i]: self.values[i] for i in range(len(self.keys))}
        for i in range(len(self.keys)):
            self.hash_table.add(self.keys[i], self.values[i])

    def test_get(self):
        for i in range(len(self.keys)):
            self.assertEqual(self.hash_table[self.keys[i]], self.dictionary[self.keys[i]])
            self.assertEqual(self.hash_table[self.keys[i]], self.values[i])

    def test_remove(self):
        hash_table_copy = deepcopy(self.hash_table)
        for i in range(len(self.keys)):
            self.assertEqual(hash_table_copy.remove(self.keys[i]), self.dictionary[self.keys[i]])
        self.assertListEqual(hash_table_copy.array, [None for _ in range(16)])
