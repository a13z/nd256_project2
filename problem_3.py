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

    for char in data:
        if char not in char_frequencies:
            char_frequencies[char] = 1
        else:
            char_frequencies[char] += 1

    freq_list = sorted([(value, key) for key, value in char_frequencies.items()])

    while freq_list is not None:
        if len(freq_list) == 1:
            tree = Tree()
            tree.set_root(freq_list.pop(0)[2])

            traverse_tree(tree.get_root(),"")

            for char in data:
                encoded_data = encoded_data + codes[char]

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
    node = tree.get_root()
    decoded_data = ""

    for char in data:
        if char == "0":
            node = node.get_left_child()
            if not node.has_left_child() and not node.has_right_child():
                decoded_data = decoded_data + node.get_data()
                node = tree.get_root()

        elif char == "1":
            node = node.get_right_child()
            if not node.has_left_child() and not node.has_right_child():
                decoded_data = decoded_data + node.get_data()
                node = tree.get_root()

    return decoded_data

def traverse_tree(tree,code):
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

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))