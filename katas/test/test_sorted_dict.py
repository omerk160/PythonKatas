import unittest
from python_katas.sorted_dict import SortedDict


class TestSortedDictL2(unittest.TestCase):
    def test_initialization(self):
        s_dict = SortedDict()
        self.assertEqual(len(s_dict), 0)

    def test_setitem(self):
        s_dict = SortedDict()
        s_dict['banana'] = 'ccc'
        s_dict['apple'] = 'aaa'
        s_dict['orange'] = 'bbb'
        self.assertEqual(list(s_dict.keys()), ['apple', 'banana', 'orange'])
        self.assertEqual(list(s_dict.values()), ['aaa', 'ccc', 'bbb'])
        self.assertEqual(list(s_dict.items()), [('apple', 'aaa'), ('banana', 'ccc'), ('orange', 'bbb')])

    def test_setitem_order(self):
        s_dict = SortedDict()
        s_dict['a'] = None
        s_dict['t'] = None
        s_dict['h'] = None
        s_dict['q'] = None
        s_dict['b'] = None
        self.assertEqual(list(s_dict.items()), [('a', None), ('b', None), ('h', None), ('q', None), ('t', None)])


if __name__ == '__main__':
    unittest.main()
