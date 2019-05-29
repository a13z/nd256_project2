class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return str([self.key, self.value])

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        if self.head == None and self.tail == None:
            node = DoubleNode(key, value)
            self.head = node
            self.tail = node
            return node
        else:
            last_node = self.tail
            new_node = DoubleNode(key, value)
            last_node.next = new_node
            new_node.previous = last_node
            self.tail = new_node
            return new_node

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " <-/-> "
            cur_head = cur_head.next
        return out_string


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.num_elements = 0
        self.queue = DoublyLinkedList()
        self.cache = {}

    def status(self):
        cur_head = self.queue.head
        cache_output = []
        while cur_head:
            cache_output.append((cur_head.key, cur_head.value))
            cur_head = cur_head.next
        return cache_output

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        # print("Get ", double_node)
        if key in self.cache:
            double_node = self.cache[key]
            head = self.queue.head
            tail = self.queue.tail

            if head == double_node:
                self.queue.head = double_node.next
                self.queue.tail = double_node
                tail.next = double_node
                double_node.next = None
            elif tail == double_node:
                return
            else:
                double_node.next.previous = double_node.previous
                double_node.previous.next = double_node.next
                double_node.previous = tail
                double_node.next = None
                self.queue.tail = double_node
            return double_node.value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        # print("Set ", key, value)
        # print("Num elements / Capacity ", self.num_elements, self.capacity)

        if key is not None and value is not None:
            if self.num_elements < self.capacity:
                # print("Capacity available in cache. Current status: ", self.queue)
                if key not in self.cache:
                    self.num_elements += 1
                    self.cache[key] = self.queue.append(key, value)
                else:
                    # print("Key is already in cache")
                    return
            else:
                # print("Cache over capacity, reusing LRU", self.queue)
                if key not in self.cache:
                    reuse_lru_element = self.queue.head
                    self.queue.head = reuse_lru_element.next
                    self.cache[key] = self.queue.append(key, value)
                    del self.cache[reuse_lru_element.key]
                    self.num_elements -= 1


# our_cache = LRU_Cache(5)
#
# our_cache.set(1, 1)
# our_cache.set(2, 2)
# print(our_cache.get(1))       # returns 2
# print(our_cache.get(2))       # return -1
# print(our_cache.get(3))      # returns 1

def test_function(test_case, solution):

    cache = LRU_Cache(5)
    output = []
    for command in test_case:
        if command[0] == 'S':
            cache.set(command[1][0],command[1][1])
        elif command[0] == 'G':
            cache.get(command[1])

    output = cache.status()
    print(test_case)
    # print(solution)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

# Test case 1
test_case_1 = [('S',(1,1)),('S',(2,2)),('G',2),('G',3),('S',(3,3)),('G',1),('S',(4,4)),('S',(5,5)),('S',(6,6))]
test_case_1_solution = [(3, 3),(1, 1),(4, 4),(5, 5),(6, 6)]
test_function(test_case_1,test_case_1_solution)

# Test case 2
test_case_2 = [('S',(None,1)),('S',('a',None)),('G',2),('G',3),('S',('b',3)),('G',1),('S',('c',4)),('S',(5,5)),('S',(6,6))]
test_case_2_solution = [('b', 3), ('c', 4), (5, 5), (6, 6)]
test_function(test_case_2,test_case_2_solution)

# Test case 3
test_case_3 = [('S',(112341234123,1)),('S',(2,2)),('G',423432412341234),('G',3),('S',(3,3)),('G',112341234123),('S',(4,4)),('S',(5,1234123434)),('S',(6,6))]
test_case_3_solution = [(3, 3), (112341234123, 1), (4, 4), (5, 1234123434), (6, 6)]
test_function(test_case_3,test_case_3_solution)

