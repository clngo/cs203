import unittest
# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack



# from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty(), False)
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)

    def test_mine(self):
        stack1 = Stack(5)
        stack1.push(0)
        stack1.push(1)
        stack1.push(2)

        self.assertEqual(stack1.is_empty(), False)
        self.assertEqual(stack1.size(), 3)
        self.assertFalse(stack1.is_full())
        self.assertEqual(stack1.peek(), 2)
        self.assertEqual(stack1.pop(), 2)
        self.assertEqual(stack1.peek(), 1)
        self.assertEqual(stack1.size(), 2)

        stack2 = Stack(3)
        with self.assertRaises(IndexError):
            stack2.pop()
            stack2.peek()
        stack2.push(0)
        stack2.push(1)
        stack2.push(2)

        with self.assertRaises(IndexError):
            stack2.push(3)
            stack2.peek()

    def test_linked_list(self):
        stack1 = Stack(3)
        stack1.push(0)
        stack1.push(1)
        stack1.push(2)

        self.assertFalse(stack1.is_empty())
        self.assertFalse(stack1.is_full())

        self.assertEqual(stack1.peek(), 2)

if __name__ == '__main__':
    unittest.main()