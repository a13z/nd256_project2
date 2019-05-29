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

        # TODO: Write function to prepend here
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
    # Your Solution Here

    sorted_list = sort_list(llist_1)
    list2 = llist_2.head

    while list2:

        # print("list2 value", list2.value)
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
                # time.sleep(2)
                # print("sorted list ", sorted_list)
                # print("list2 value ", list2.value)
                # print("sorted list value ", sorted_list_head.value)

                if list2.value == sorted_list_head.value:
                    list2 = list2.next
                    break
                #if list2.value < sorted_list_head.next.value:
                elif list2.value < sorted_list_head.next.value:
                    new_node = Node(list2.value)
                    new_node.next = sorted_list_head.next
                    sorted_list_head.next = new_node
                    break
                else:
                    sorted_list_head = sorted_list_head.next

    return sorted_list

def intersection(llist_1, llist_2):
    # Your Solution Here

    intersection_list = LinkedList()

    sorted_list = sort_list(llist_1)
    list2 = sort_list(llist_2).head
    #list2 = llist_2.head

    # print("Intersection of ")
    # print("sorted list 1 ", sorted_list)
    # print("list 2  ", llist_2)

    while list2:

        # print("list2 value", list2.value)
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
                # time.sleep(2)
                # print("sorted list ", sorted_list)
                # print("list2 value ", list2.value)
                # print("sorted list value ", sorted_list_head.value)

                if list2.value == sorted_list_head.value:
                    intersection_list.append(list2.value)
                    list2 = list2.next
                    sorted_list_head = sorted_list.head

                elif list2.value < sorted_list_head.next.value:
                    list2 = list2.next

                else:
                    sorted_list_head = sorted_list_head.next

        #print("Intersection list ", intersection_list)

    return intersection_list


def sort_list(list):

    sorted_list = LinkedList()
    node = list.head

    if node is None:
        return None

    while node:

        # print("Inside first loop. the list to sort. Node value ", node.value)
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
                # print("sorted_list_head ", sorted_list_head)
                # print("Inside second loop. the sorted list head value ", sorted_list_head.value)
                # print("Inside second loop. the list node value ", node.value)
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
        # print(sorted_list)
    return sorted_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# sort_list(linked_list_1)
print("Test case 1")

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2
print("Test case 2")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
