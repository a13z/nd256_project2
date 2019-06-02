import sys

class Node(object):

    def __init__(self, data=None, freq=None):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_freq(self, freq):
        self.freq = freq

    def get_freq(self, freq):
        return self.freq

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_data()})"

    def __str__(self):
        return f"Node({self.get_data()})"

class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root


def huffman_encoding(data):

    char_frequencies = {}
    encoded_data = ""

    if len(data) == 0:
        return "0", None

    for char in data:
        if char not in char_frequencies:
            char_frequencies[char] = 1
        else:
            char_frequencies[char] += 1

    freq_list = sorted([(value, key) for key, value in char_frequencies.items()])

    while freq_list is not None:
        if len(freq_list) == 1:
            tree = Tree()
            # Case when data has more than 1 char,
            # then freq_list only element has a third field which
            # is the pointer to the parent node of the tree
            if len(freq_list[0]) > 2:
                tree.set_root(freq_list.pop(0)[2])
                traverse_tree(tree.get_root(), "")
                for char in data:
                    encoded_data = encoded_data + codes[char]
            else:
            # Case when data contains just 1 char,
            # then freq_list only element is unique and therefore
            # there is only 1 node in the tree. Use 0 to encode it.
                node = freq_list.pop(0)
                tree.set_root(Node(node[1],node[0]))
                traverse_tree(tree.get_root(), "")
                for char in data:
                    encoded_data = encoded_data + '0'

            return encoded_data, tree

        lowest1 = freq_list.pop(0)
        lowest2 = freq_list.pop(0)

        node1 = Node(lowest1[1], lowest1[0])
        node2 = Node(lowest2[1], lowest2[0])

        node_sum = Node(lowest1[1] + lowest2[1], lowest1[0] + lowest2[0])


        if len(lowest1) > 2:
            node_sum.set_left_child(lowest1[2])
        else:
            node_sum.set_left_child(node1)
        if len(lowest2) > 2:
            node_sum.set_right_child(lowest2[2])
        else:
            node_sum.set_right_child(node2)

        sum_lowests = (lowest1[0] + lowest2[0], lowest1[1] + lowest2[1], node_sum)

        freq_list.append(sum_lowests)

        freq_list = sorted(freq_list)


def huffman_decoding(data,tree):
    if tree is None or len(data) == 0:
        return ""

    node = tree.get_root()
    decoded_data = ""

    for char in data:
        if char == "0":
            if node.has_left_child():
                node = node.get_left_child()
            if not node.has_left_child() and not node.has_right_child():
                decoded_data = decoded_data + node.get_data()
                node = tree.get_root()

        elif char == "1":
            if node.has_right_child():
                node = node.get_right_child()
            if not node.has_left_child() and not node.has_right_child():
                decoded_data = decoded_data + node.get_data()
                node = tree.get_root()

    return decoded_data

def traverse_tree(tree,code):

    # if tree.get_left_child() is None and tree.get_right_child() is None:
    #     print("There is only one node in the tree")
    #     codes[tree.data] = '1'
    #     return

    if tree.get_left_child() is None and tree.get_right_child() is None:
        codes[tree.data] = code
        return

    if tree.has_left_child():
        code = code + "0"
        traverse_tree(tree.get_left_child(),code)
        code = code[:-1]

    if tree.has_right_child():
        code = code + "1"
        traverse_tree(tree.get_right_child(),code)
        code = code[:-1]

def test_function(test_case):
    sentence = test_case[0]
    solution_sentence_size = test_case[1][0]
    solution_encoded_sentence = test_case[1][2]
    solution_encoded_size = test_case[1][1]

    encoded_data, tree = huffman_encoding(sentence)

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The content of the data is: {}\n".format(sentence))

    if sys.getsizeof(sentence) == solution_sentence_size and \
        encoded_data == solution_encoded_sentence and \
        sys.getsizeof(int(encoded_data, base=2)) == solution_encoded_size and \
        decoded_data == sentence:
        print("Pass")
    else:
        print("Failed")

if __name__ == "__main__":
    codes = {}

    sentence = ''
    solution = [49, 24, '0']
    test_case = [sentence, solution]
    test_function(test_case)

    sentence = 'a'
    solution = [50, 24, '0']
    test_case = [sentence, solution]
    test_function(test_case)

    sentence = 'AAAAAAAA'
    solution = [57, 24, '00000000']
    test_case = [sentence, solution]
    test_function(test_case)

    sentence = 'The bird is the word'
    solution = [69, 36, '1110000100011011101010100111111001001111101010001000110101101101001111']
    test_case = [sentence, solution]
    test_function(test_case)