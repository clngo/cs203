import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_1(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())

    def test_add(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(3)
        t_list.add(2)
        t_list.add(5)
        t_list.add(4)
        self.assertEqual(t_list.python_list(), [1, 2, 3, 4, 5])
        self.assertFalse(t_list.remove(10))
        self.assertTrue(t_list.remove(3))
        self.assertFalse(t_list.remove(11))
        self.assertTrue(t_list.remove(1))
        self.assertEqual(t_list.python_list(), [2, 4, 5])
        (t_list.add(3))
        self.assertTrue(t_list.remove(2))
        self.assertTrue(t_list.remove(4))
        self.assertTrue(t_list.remove(5))
        self.assertTrue(t_list.remove(3))

    def test_insert_and_pop(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(3)
        t_list.add(2)
        t_list.add(5)
        t_list.add(4)
        self.assertEqual(t_list.python_list(), [1, 2, 3, 4, 5])
        self.assertEqual(t_list.index(1), 0)
        self.assertEqual(t_list.index(3), 2)
        self.assertEqual(t_list.index(5), 4)
        self.assertEqual(t_list.index(13), None)
        self.assertEqual(t_list.pop(0), 1)
        self.assertEqual(t_list.pop(1), 3)
        self.assertEqual(t_list.python_list(), [2, 4, 5])
        self.assertTrue(t_list.search(4))
        self.assertFalse(t_list.search(3))
        self.assertEqual(t_list.python_list_reversed(), [5, 4, 2])
        self.assertEqual(t_list.size(), 3)

    def test_simple1(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)


if __name__ == '__main__':
    unittest.main()