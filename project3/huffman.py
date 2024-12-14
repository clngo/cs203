from ordered_list import *
from huffman_bit_writer import *

def cnt_freq(filename:str) -> list[int]: #function opens a txt file (passed as a string)
    """
    Function opens a txt file (passed as a string), reads, and counts the frequency of
    occurences of all the characters. Returns a Python List with 256 entries - counts 
    are initialized to zero. The ASCII value of the characters are used to index into this
    list for the frequency counts
    """
    try:
        file = open(filename, "r")
    except:
        raise FileNotFoundError("File Not Found")
    file_chars = file.read()
    #print(f"{file_chars}")
    result = [0] * 256
    for char in file_chars:
        idx = ord(char)
        result[idx] += 1
    file.close()
    return result


# result = [0] * 256
# idx = ord("~")
# result[idx] = 2
# print(result)
# print(chr(97))
class HuffmanNode:
    def __init__(self, ASCII:int, frequency:int): #either a leaf or an internal node (including the root node)
        self.right = None
        self.left = None
        self.char_ASCII = ASCII
        self.frequency = frequency

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.char_ASCII < other.char_ASCII
        else:
            return self.frequency < other.frequency

def create_huff_tree(list_of_freqs:list[int]):
    orderedlst = OrderedList()
    for idx, freq in enumerate(list_of_freqs): #add huffman nodes into an orderedlist
        if freq > 0:
            orderedlst.add(HuffmanNode(idx, freq))
    if orderedlst.is_empty():
        return
    # if orderedlst.size() == 1:
    #     return list_of_freqs[0]
    #print(orderedlst.size())
    while orderedlst.size() > 1: #While there is more than one node in the list
        #Remove  2 nodes from the beginning of the list (lowest frequencies)
        node_1 = orderedlst.pop(0) #0th idx is the beginning of the list
        node_2 = orderedlst.pop(0) #Because the previous node was removed, the before 2nd node is now the 1st node
        # print(f"pop: {node_1.char_ASCII}")
        # print(f"pop2: {node_2.char_ASCII}")
        #Create a new internal node with these 2 nodes as children
        #Check the lower of the frequencies to be on the left child.
        sum_freq = node_1.frequency + node_2.frequency
        # print(f"sum_freq: {sum_freq}")

        if node_1 < node_2: #d,2; c,2
            if node_1.char_ASCII < node_2.char_ASCII:
                new_internal = HuffmanNode(node_1.char_ASCII, sum_freq)
            else:
                new_internal = HuffmanNode(node_2.char_ASCII, sum_freq)
            new_internal.left = node_1
            new_internal.right = node_2
        elif node_1.frequency > node_2.frequency: #d,2; c,2
            if node_1.char_ASCII < node_2.char_ASCII:
                new_internal = HuffmanNode(node_1.char_ASCII, sum_freq)
            else:
                new_internal = HuffmanNode(node_2.char.ASCII, sum_freq)
            new_internal.left = node_2
            new_internal.right = node_1

        orderedlst.add(new_internal)
        # print(f"diff {orderedlst.size()}")
        # for i in orderedlst.python_list():
        #     print(f"ne: {i.char_ASCII}")
    #print(f"ans: {orderedlst.pop(0).frequency}")
    return orderedlst.pop(0)


def create_code(root_node:HuffmanNode) -> list[str]: #Traverses the Huffman tree and returns an array of 256 strings
    result = [""] * 256
    #traverse HuffmanTree
    if root_node is None:
        return result
    return create_code_helper(root_node, "", result)

def create_code_helper(root_node:HuffmanNode, code:str, result:list[str]) -> list[str]:
    if root_node is None:
        return result
    if (root_node.left is None) and (root_node.right is None): #reached the leaf; has no children Base case
        result[root_node.char_ASCII] = code
        return result
    else:
        if root_node.left:
            result = create_code_helper(root_node.left, code+"0", result)
        if root_node.right:
            result = create_code_helper(root_node.right, code+"1", result)
        return result

def huffman_encode(in_file: str, out_file:str):
    try:
        innfile = open(in_file, "r")
    except:
        raise FileNotFoundError("File Not Found")
    text = innfile.read()
    #print(text)

    count_freq = cnt_freq(in_file)
    header = create_header(count_freq)
    innfile.close()

    # try:
    #     outtfile = open(out_file, "w") #Will overwrite anything that's already inside of the file.
    # except:
    #     raise FileNotFoundError("File Not Found")

    huffman_tree = create_huff_tree(count_freq)
    decoded = create_code(huffman_tree)
    if (huffman_tree is None) or len(decoded) == 0:
        return
    outtfile = HuffmanBitWriter(out_file)
    #Get the 0s and 1s list of strings from code

    # print(decoded)
    for char in header:
        outtfile.write_str(char)
    outtfile.write_str("\n")
    for char in text:
        code = decoded[ord(char)]
        outtfile.write_code(code)


    outtfile.close()


def create_header(list_of_freqs: list[int]) -> str:
    result = ""
    for idx, char in enumerate(list_of_freqs):
        if char != 0:
            result += str(idx) + " "
            result += str(char) + " "
    return result[:-1]




