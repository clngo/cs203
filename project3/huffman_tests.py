import unittest
from huffman import *

class HuffmanTest(unittest.TestCase):
    def test_1_cnt_freq(self):
        test_1 = cnt_freq("file1.txt")
        self.assertEqual(test_1[96:104], [0, 2, 4, 8, 16, 0, 2, 0])
        #orderedlst = OrderedList()
        # for idx, freq in enumerate(test_1):  # add huffman nodes into an orderedlist
        #     if freq > 0:
        #         orderedlst.add(HuffmanNode(idx, freq))
        # for i in orderedlst.python_list():
        #     print(i.char_ASCII, i.frequency, chr(i.char_ASCII))
        # print(orderedlst.python_list()[0].char_ASCII)

        test_1_huff_tree = create_huff_tree(test_1)
        root = HuffmanNode(97, 32)
        self.assertEqual(test_1_huff_tree.char_ASCII, root.char_ASCII)
        self.assertEqual(test_1_huff_tree.frequency, root.frequency)

        root.left = HuffmanNode(97, 16)
        self.assertEqual(test_1_huff_tree.left.char_ASCII, root.left.char_ASCII)
        self.assertEqual(test_1_huff_tree.left.frequency, root.left.frequency)

        root.right = HuffmanNode(100, 16)
        self.assertEqual(test_1_huff_tree.right.char_ASCII, root.right.char_ASCII)
        self.assertEqual(test_1_huff_tree.right.frequency, root.right.frequency)

        root.left.left = HuffmanNode(97, 8)
        self.assertEqual(test_1_huff_tree.left.left.char_ASCII, root.left.left.char_ASCII)
        self.assertEqual(test_1_huff_tree.left.left.frequency, root.left.left.frequency)

        root.left.right = HuffmanNode(99, 8)
        self.assertEqual(test_1_huff_tree.left.right.char_ASCII, root.left.right.char_ASCII)
        self.assertEqual(test_1_huff_tree.left.right.frequency, root.left.right.frequency)

        root.left.left.left = HuffmanNode(97, 4)
        self.assertEqual(test_1_huff_tree.left.left.left.char_ASCII, root.left.left.left.char_ASCII)
        self.assertEqual(test_1_huff_tree.left.left.left.frequency, root.left.left.left.frequency)

        root.left.left.right = HuffmanNode(98, 4)
        self.assertEqual(test_1_huff_tree.left.left.right.char_ASCII, root.left.left.right.char_ASCII)
        self.assertEqual(test_1_huff_tree.left.left.right.frequency, root.left.left.right.frequency)

        root.left.left.left.left = HuffmanNode(97, 2)
        self.assertEqual(test_1_huff_tree.left.left.left.left.char_ASCII, root.left.left.left.left.char_ASCII)
        self.assertEqual(test_1_huff_tree.left.left.left.left.frequency, root.left.left.left.left.frequency)

        root.left.left.left.right = HuffmanNode(102, 2)
        self.assertEqual(test_1_huff_tree.left.left.left.right.char_ASCII, root.left.left.left.right.char_ASCII)
        self.assertEqual(test_1_huff_tree.left.left.left.right.frequency, root.left.left.left.right.frequency)

        test_1_code = create_code(test_1_huff_tree)
        self.assertEqual(test_1_code[96:103], ["", "0000", "001", "01", "1", "", "0001"])

        test_1_header = create_header(test_1)
        self.assertEqual(test_1_header, "97 2 98 4 99 8 100 16 102 2")

        test_1_file = huffman_encode("file1.txt", "file1_compressed.txt")

    def test_2(self):
        test_2 = cnt_freq("file2.txt")
        self.assertEqual(test_2[96:101], [0, 4, 3, 2, 1])
        self.assertEqual(test_2[32:34], [3, 0])
        test_2_huff_tree = create_huff_tree(test_2)
        root = HuffmanNode(32, 13)
        self.assertEqual(test_2_huff_tree.char_ASCII, root.char_ASCII)

        root.left = HuffmanNode(32, 6)
        self.assertEqual(test_2_huff_tree.left.char_ASCII, root.left.char_ASCII)
        self.assertEqual(test_2_huff_tree.left.frequency, root.left.frequency)

        #print(ord("a")) #97
        root.right = HuffmanNode(97, 7)
        self.assertEqual(test_2_huff_tree.right.char_ASCII, root.right.char_ASCII)
        self.assertEqual(test_2_huff_tree.right.frequency, root.right.frequency)

        root.left.left = HuffmanNode(32, 3)
        self.assertEqual(test_2_huff_tree.left.left.char_ASCII, root.left.left.char_ASCII)
        self.assertEqual(test_2_huff_tree.left.left.frequency, root.left.left.frequency)

        #print(ord("b")) #98
        root.left.right = HuffmanNode(98, 3)
        self.assertEqual(test_2_huff_tree.left.right.char_ASCII, root.left.right.char_ASCII)
        self.assertEqual(test_2_huff_tree.left.right.frequency, root.left.right.frequency)

        #print(ord("c")) #99
        root.right.left = HuffmanNode(99, 3)
        self.assertEqual(test_2_huff_tree.right.left.char_ASCII, root.right.left.char_ASCII)
        self.assertEqual(test_2_huff_tree.right.left.frequency, root.right.left.frequency)

        root.right.right = HuffmanNode(97, 4)
        self.assertEqual(test_2_huff_tree.right.right.char_ASCII, root.right.right.char_ASCII)
        self.assertEqual(test_2_huff_tree.right.right.frequency, root.right.right.frequency)

        #print(ord("d"))
        root.right.left.left = HuffmanNode(100, 1)
        self.assertEqual(test_2_huff_tree.right.left.left.char_ASCII, root.right.left.left.char_ASCII)
        self.assertEqual(test_2_huff_tree.right.left.left.frequency, root.right.left.left.frequency)

        root.right.left.right = HuffmanNode(99, 2)
        self.assertEqual(test_2_huff_tree.right.left.right.char_ASCII, root.right.left.right.char_ASCII)
        self.assertEqual(test_2_huff_tree.right.left.right.frequency, root.right.left.right.frequency)

        test_2_code = create_code(test_2_huff_tree)
        self.assertEqual(test_2_code[96:102], ["", "11", "01", "101", "100", ""])
        self.assertEqual(test_2_code[32:34], ["00", ""])

        test_2_header = create_header(test_2)
        self.assertEqual(test_2_header, "32 3 97 4 98 3 99 2 100 1")

        test_2_file = huffman_encode("file2.txt", "file2_compressed.txt")

    def test_3_empty(self):
        test_3 = cnt_freq("file3.txt")
        test_3_huff_tree = create_huff_tree(test_3)
        self.assertEqual(test_3_huff_tree, None)

        test_3_create = create_code(test_3_huff_tree)
        self.assertEqual(test_3_create, [""]*256)

        test_3_header = create_header(test_3)
        self.assertEqual(test_3_header, "")

        test_3_file = huffman_encode("file3.txt", "file3_compressed.txt")

    def test_4_no_file(self):
        with self.assertRaises(FileNotFoundError):
            self.test_4 = cnt_freq("no.txt")

if __name__ == "__main__":
    unittest.main()