import hashlib
from datetime import datetime
import time
import random

class Block:

    def __init__(self, data, previous_hash):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(str(self.timestamp)+str(self.data)+self.previous_hash)
        self.next = None

    def calc_hash(self, string):
        sha = hashlib.sha256()
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:

    def __init__(self):
        self.head = None

    def add_block(self, data):
        """ Prepend a value to the beginning of the list. """

        # TODO: Write function to prepend here
        if self.head is None:
            self.head = Block("Genesis block", "0x0")

        previous_node = self.head
        previous_node_hash = previous_node.hash
        new_node = Block(data, previous_node_hash)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        head = self.head
        counter = self.size()
        while head:
            print("Block # ", counter)
            print("Date :", datetime.fromtimestamp(head.timestamp).isoformat())
            print("Data :", head.data)
            print("Block hash :", head.hash)
            print("Previous hash :", head.previous_hash)
            print("")
            head = head.next
            counter -= 1

    def size(self):
        """ Return the size or length of the linked list. """

        # TODO: Write function to get size here
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next

        return counter

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += " -> " + str(cur_head.data)
            cur_head = cur_head.next
        return out_string

blockchain = Blockchain()

blockchain.add_block("Second block in the blockchain")

time.sleep(random.randint(0,5))

blockchain.add_block("Third block in the blockchain")

time.sleep(random.randint(0,5))

blockchain.add_block("Forth block in the blockchain")

blockchain.print()

print(blockchain)

