import unittest
# Use the imports below to test either your array-based stack
# or your link-based version
from stack_linked import Stack



# from stack_linked import Stack

class TestLab2(unittest.TestCase):

    def test_linked_list(self):
        stack1 = Stack(3)
        stack1.push(0)
        stack1.push(1)
        stack1.push(2)

        self.assertFalse(stack1.is_empty())
        self.assertTrue(stack1.is_full())

        self.assertEqual(stack1.peek(), 2)
        with self.assertRaises(IndexError): #stack is full
            stack1.push(5)

        self.assertEqual(stack1.pop(), 2)
        self.assertEqual(stack1.pop(), 1)
        self.assertEqual(stack1.peek(), 0)
        self.assertEqual(stack1.pop(), 0)
        with self.assertRaises(IndexError): #stack is empty
            stack1.pop()
            stack1.peek()


if __name__ == '__main__':
    unittest.main()