import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        """ Append a value to the end of the list. """

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        node = self.tail

        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def size(self):
        """ Return the size or length of the linked list. """

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

def union(llist_1, llist_2):
    """ Return a list with the union of two lists given """

    if (llist_1.head is None and llist_2.head is None) or \
            (not isinstance(llist_1, LinkedList) and not isinstance(llist_2, LinkedList)):
        return LinkedList()

    if llist_1.head is None or not isinstance(llist_1, LinkedList):
        return sort_list(llist_2)

    if llist_2.head is None or not isinstance(llist_2, LinkedList):
        return sort_list(llist_1)

    sorted_list = sort_list(llist_1)
    list2 = llist_2.head

    while list2:
        sorted_list_head = sorted_list.head
        sorted_list_tail = sorted_list.tail

        # case 1
        if list2.value < sorted_list_head.value:
            sorted_list.prepend(list2.value)
        # case 2
        elif list2.value > sorted_list_tail.value:
            sorted_list.append(list2.value)
        # case 3 Iterate
        else:
            while sorted_list_head.next:
                if list2.value == sorted_list_head.value:
                    list2 = list2.next
                    break
                elif list2.value < sorted_list_head.next.value:
                    new_node = Node(list2.value)
                    new_node.next = sorted_list_head.next
                    sorted_list_head.next = new_node
                    break
                else:
                    sorted_list_head = sorted_list_head.next

    return sorted_list

def intersection(llist_1, llist_2):
    """ Return a list with the intersection of two lists given """

    intersection_list = LinkedList()

    if llist_1.head is None or llist_2.head is None \
            or not isinstance(llist_1, LinkedList) or not isinstance(llist_2, LinkedList):
        return intersection_list

    sorted_list = sort_list(llist_1)
    list2 = sort_list(llist_2).head

    while list2:

        sorted_list_head = sorted_list.head
        sorted_list_tail = sorted_list.tail

        # case 1
        if list2.value < sorted_list_head.value:
            list2 = list2.next
        # case 2
        elif list2.value > sorted_list_tail.value:
            list2 = list2.next
        # case 3 Iterate
        else:
            while sorted_list_head.next and list2:

                if list2.value == sorted_list_head.value:
                    intersection_list.append(list2.value)
                    list2 = list2.next
                    sorted_list_head = sorted_list.head

                elif list2.value < sorted_list_head.next.value:
                    list2 = list2.next

                else:
                    sorted_list_head = sorted_list_head.next

    return intersection_list


def sort_list(list):
    """ Return a list, sorted, from a given list """

    sorted_list = LinkedList()
    node = list.head

    if node is None:
        return None

    while node:
        if sorted_list.head is None:
            sorted_list.append(node.value)
            sorted_list_head = sorted_list.head
            node = node.next

        sorted_list_head = sorted_list.head
        sorted_list_tail = sorted_list.tail

        # case 1
        if node.value < sorted_list_head.value:
            sorted_list.prepend(node.value)
        # case 2
        elif node.value > sorted_list_tail.value:
            sorted_list.append(node.value)
        # case 3 Iterate
        else:
            while sorted_list_head.next:
                if node.value == sorted_list_head.value:
                    break
                if node.value < sorted_list_head.next.value:
                    new_node = Node(node.value)
                    new_node.next = sorted_list_head.next
                    sorted_list_head.next = new_node
                    break
                else:
                    sorted_list_head = sorted_list_head.next
        node = node.next
    return sorted_list

def test_function(test_case):
    element_1 = test_case[0]
    element_2 = test_case[1]
    solution_union = test_case[2][0]
    solution_intersection = test_case[2][1]

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("List 1 ", linked_list_1)
    print("List 2 ", linked_list_2)

    union_linked_list = union(linked_list_1,linked_list_2)
    intersection_linked_list = intersection(linked_list_1, linked_list_2)

    if union_linked_list.to_list() == solution_union and \
        intersection_linked_list.to_list() == solution_intersection:
        print("Pass")
    else:
        print("Failed")


# Test case 1
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
solution = [[1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65],[4, 6, 21]]
test_case = [element_1, element_2, solution]
test_function(test_case)

# Test case 2
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]
solution = [[1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65],[]]
test_case = [element_1, element_2, solution]
test_function(test_case)

# Test case 3
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = []
solution = [[2, 3, 4, 6, 23, 35, 65],[]]
test_case = [element_1, element_2, solution]
test_function(test_case)

# Test case 4
element_1 = []
element_2 = [1, 7, 8, 9, 11, 21, 1]
solution = [[1, 7, 8, 9, 11, 21],[]]
test_case = [element_1, element_2, solution]
test_function(test_case)

# Test case 5
element_1 = []
element_2 = []
solution = [[],[]]
test_case = [element_1, element_2, solution]
test_function(test_case)

# Test case 6
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = ""
solution = [[2, 3, 4, 6, 23, 35, 65],[]]
test_case = [element_1, element_2, solution]
test_function(test_case)