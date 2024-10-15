import unittest
from katas.cache_list import CacheList


class TestCacheList(unittest.TestCase):
    def test_initialization(self):
        cache_list = CacheList(3)
        self.assertEqual(len(cache_list), 0)
        self.assertEqual(cache_list.cache_capacity(), 3)

    def test_append_within_cache_size(self):
        cache_list = CacheList(3)
        cache_list.append(1)
        cache_list.append(2)
        cache_list.append(3)
        self.assertEqual(cache_list, [1, 2, 3])

    def test_append_exceed_cache_size(self):
        cache_list = CacheList(3)
        cache_list.append(1)
        cache_list.append(2)
        cache_list.append(3)
        cache_list.append(4)
        cache_list.append(5)
        self.assertEqual(cache_list, [3, 4, 5])

    def test_append_cycle_within_cache_size(self):
        cache_list = CacheList(3)
        cache_list.append(1)
        cache_list.append(2)
        cache_list.append(3)
        cache_list.append(4)
        cache_list.append(5)
        cache_list.append(6)
        self.assertEqual(cache_list, [4, 5, 6])

    def test_append_cycle_exceed_cache_size(self):
        cache_list = CacheList(3)
        cache_list.append(1)
        cache_list.append(2)
        cache_list.append(3)
        cache_list.append(4)
        cache_list.append(5)
        cache_list.append(6)
        cache_list.append(7)
        self.assertEqual(cache_list, [5, 6, 7])

