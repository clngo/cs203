import unittest
from huffman import *

class HuffmanTest(unittest.TestCase):
    def test_1_create_code_helper(self):
        test_1 = cnt_freq("file1.txt")
        test_1_huff_tree = create_huff_tree(test_1)
        test_1_code = create_code_helper(test_1_huff_tree, "", [""]*256)
        self.assertEqual(test_1_code[96:103], ["", "0000", "001", "01", "1", "", "0001"])

    def test_2_create_code_helper(self):
        test_2 = cnt_freq("file2.txt")
        test_2_huff_tree = create_huff_tree(test_2)
        test_2_code = create_code_helper(test_2_huff_tree, "", [""]*256)
        self.assertEqual(test_2_code[96:102], ["", "11", "01", "101", "100", ""])
        self.assertEqual(test_2_code[32:34], ["00", ""])

    def test_3_empty(self):
        test_3 = cnt_freq("file3.txt")
        test_3_huff_tree = create_huff_tree(test_3)
        test_3_create = create_code_helper(test_3_huff_tree, "", [""]*256)
        self.assertEqual(test_3_create, [""]*256)

if __name__ == "__main__":
    unittest.main()