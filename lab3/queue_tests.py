import unittest

import queue_array
# from queue_array import Queue
from queue_linked import Queue
from queue_array import Queue_array


class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue('thing')
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), 'thing')


        q.enqueue("new")
        q.enqueue("something")
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.dequeue(), "new")
        self.assertEqual(q.dequeue(), "something")

        with self.assertRaises(IndexError): #queue is empty
            q.dequeue()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue("again")
        q.enqueue("fourth")
        q.enqueue("last")
        self.assertEqual(q.size(), 5)
        with self.assertRaises(IndexError): #queue is full
            q.enqueue("error")

    def test_queue_iter(self):
        q = Queue(5)
        for i in range(5):
            q.enqueue(i)
        for i in range(5):
            self.assertEqual(q.dequeue(), i)

    def test_queue_array(self):
        q = Queue_array(5)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue(0)
        q.enqueue(1)
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.dequeue(), 1)

        with self.assertRaises(IndexError): #queue is empty
            q.dequeue()
        self.assertTrue(q.is_empty())
        for i in range(5):
            q.enqueue(i)
        for i in range(5):
            self.assertEqual(q.dequeue(), i)
        self.assertEqual(q.size(), 0)

    def test_queue_array1(self):
        q = Queue_array(3)
        for i in range(2):
            q.enqueue(i)
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 2)




if __name__ == '__main__':
    unittest.main() 