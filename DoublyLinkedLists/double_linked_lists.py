# Doubly LL has a prev compared to LL
# sample of how a Doubly LL impl will look like (not the actual impl)
head = {
    "value": 11,
    "next": None,
    "prev": None
}


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # append at end of Doubly LL
    def append(self, value):
        next_node = Node(value)
        # if head points to None
        if self.head == None:
            self.head = next_node
            self.tail = next_node
        # if alr have existing node
        # points the tail to the next node to append
        else:
            self.tail.next = next_node
            # for Doubly LL, need set prev to the curr tail
            next_node.prev = self.tail
            # shift the tail
            self.tail = next_node
        # increment length of Doubly LL by 1
        self.length += 1
        return True

    # pop - remove last node of Doubly LL
    def pop(self):
        # case for Doubly LL to have 0 items before pop
        if self.length == 0:
            return None
        temp = self.tail
        # case for Doubly LL to have only 1 item before pop
        if self.length == 1:
            # set head and tail to None
            self.head = None
            self.tail = None
        # normal cases
        else:
            # do not need to iterate with head to get the prev node
            self.tail = self.tail.prev
            # set the new tail to point to None
            self.tail.next = None
            # remove the temp (Node that is being popped) by setting the temp.prev to None
            temp.prev = None
        # decrement length of Doubly LL
        self.length -= 1
        return temp

    # prepend - add a node at the beginning of Doubly LL
    def prepend(self, value):
        new_node = Node(value)
        # case for Doubly LL to have 0 items before prepend
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # normal cases
        else:
            # set the new node to point to the curr head
            new_node.next = self.head
            # set the curr head to point to the new node
            self.head.prev = new_node
            # shift the head to the new node
            self.head = new_node
        # increment length of Doubly LL
        self.length += 1
        return True

    # pop_first - remove the first node of Doubly LL
    def pop_first(self):
        # case for 0 items before pop_first
        if self.length == 0:
            return None
        # case for 1 item before pop_first
        # set temp to the curr head
        temp = self.head
        # set head and tail to None
        if self.length == 1:
            self.head = None
            self.tail = None
        # normal cases
        else:
            # shift the head to the next node
            self.head = self.head.next
            # set the next node prev to None (remove the pointer pointing back curr head)
            self.head.prev = None
            # remove the temp (Node that is being popped) by setting the temp.next to None
            temp.next = None
        # decrement length of Doubly LL
        self.length -= 1
        return temp

    # get method (very diff impl from singly linked list) - more optimised
    def get(self, index):
        # check for base case
        # if index is less than zero or greater than the length of DLLs -> return None
        if index < 0 or index >= self.length:
            return None
        # set temp var to the head for iteration
        temp = self.head
        # default for loop (similar to SLL impl)
        # however we only want to iterate only if the index is the first half of the DLL
        if index < self.length/2:
            for _ in range(index):
                # iterating through each node moving temp pointer forward
                temp = temp.next
        # the other condition if the index is in the second half (iterate from the back)
        else:
            # set temp to the tail
            temp = self.tail
            # range from the last index to the given index, iterate by decrement by 1 (if -1 not specified is by default increment by 1)
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        # this will return the node in which the index is
        return temp

    # set method (set_value as set is a python keyword)
    def set_value(self, index, value):
        # temp = self.head
        # # base case
        # if index < 0 or index >= self.length:
        #     return None
        # # replace the value for first half
        # if index < self.length/2:
        #     for _ in range(index):
        #         temp = temp.next
        # else:
        #     temp = self.tail
        #     for _ in range(self.length - 1, index, -1):
        #         temp = temp.prev
        # # set the value of the node at the required index with the value
        # temp.value = value

        # more optimised version by using get method we wrote earlier
        temp = self.get(index)

        # check if temp return Node or None (out of index)
        if temp:
            # if temp is not None -> set the value to the input value
            temp.value = value
            return True
        # return false when temp is None
        return False

    # insert method
    def insert(self, index, value):
        # cannot insert before index 0 (start) or out of range
        # check on the index
        if index < 0 or index > self.length:
            return False
        # insert at the start of DLL is prepend
        if index == 0:
            return self.prepend(value)
        # insert at end of DLL is append
        if index == self.length:
            return self.append(value)
        # for the insertion in the middle
        new_node = Node(value)
        # setup before and after for insertion
        # use get method to get the before value for insertion
        # use the .next method to get the after node (O(1) vs O(n) if you use get for after)
        before = self.get(index - 1)
        after = before.next
        # point back the arrows on the new_node back to the original DLL
        new_node.prev = before
        new_node.next = after
        # point the before and after node to the new_node
        before.next = new_node
        after.prev = new_node

        # add length of DLL by 1 after insertion
        self.length += 1
        return True

    # remove method
    def remove(self, index):
        # base case - cannot remove out of range
        if (index >= self.length or index < 0):
            return None
        # reuse pop & pop_first methods for removing first and last elements
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        # remove elements in the middle
        # set up temp - use one variable to remove middle elements method
        # instead of using before and after variables
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        # remove the pointer of temp.prev and temp.next
        temp.next = None
        temp.prev = None

        # minus length of DLL
        self.length -= 1
        # return the removed node
        return temp


my_doubly_linked_list = DoublyLinkedList(7)
# my_doubly_linked_list.print_list()
print(my_doubly_linked_list.print_list())  # 7 None

print("----- append -----")
# append
my_doubly_linked_list.append(2)
print(my_doubly_linked_list.print_list())  # 7 2 None

print("----- pop -----")
# pop - 7 <-> 2 <-> None
# 2 is being popped
print("{} is being popped".format(my_doubly_linked_list.pop().value))
print(my_doubly_linked_list.print_list())  # 7 None
# 7 is being popped
print("{} is being popped".format(my_doubly_linked_list.pop().value))
print(my_doubly_linked_list.print_list())  # None
# None is being popped
print("{} is being popped".format(my_doubly_linked_list.pop()))
print(my_doubly_linked_list.print_list())  # None

print("----- prepend -----")
# prepend
# setting up Doubly LL with 2 items
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
print(my_doubly_linked_list.print_list())  # 2 3 None
# prepend 1
my_doubly_linked_list.prepend(1)
print(my_doubly_linked_list.print_list())  # 1 2 3 None

print("----- pop_first -----")
# pop_first
# setting up Doubly LL with 2 items
my_doubly_linked_list_popfirst = DoublyLinkedList(2)
my_doubly_linked_list_popfirst.append(1)
print(my_doubly_linked_list_popfirst.print_list())  # 2 1 None

# pop_first - 2 <-> 1 <-> None
# 2 is being popped
print("{} is being popped first".format(
    my_doubly_linked_list_popfirst.pop_first().value))
print(my_doubly_linked_list_popfirst.print_list())  # 1 None
# 1 is being popped
print("{} is being popped first".format(
    my_doubly_linked_list_popfirst.pop_first().value))
print(my_doubly_linked_list_popfirst.print_list())  # None
# None is being popped
print("{} is being popped first".format(
    my_doubly_linked_list_popfirst.pop_first()))
print(my_doubly_linked_list_popfirst.print_list())  # None

print("----- get -----")
# get(index)
# setup DLL with nodes 2, -3, 5, 1
my_doubly_linked_list_get = DoublyLinkedList(2)
my_doubly_linked_list_get.append(-3)
my_doubly_linked_list_get.append(5)
my_doubly_linked_list_get.append(1)
print(my_doubly_linked_list_get.print_list())  # 2 -3 5 1 None
print("The node at index 0 is {}".format(
    my_doubly_linked_list_get.get(0).value))  # 2
print("The node at index 2 is {}".format(
    my_doubly_linked_list_get.get(2).value))  # 5

print("----- set -----")
# set(index)
# setup DLL with nodes
my_doubly_linked_list_set = DoublyLinkedList(2)
my_doubly_linked_list_set.append(-3)
my_doubly_linked_list_set.append(5)
my_doubly_linked_list_set.append(1)
print(my_doubly_linked_list_set.print_list())  # 2 -3 5 1 None
print("The node at index 1 is {}".format(
    my_doubly_linked_list_set.get(1).value))  # -3
# set the node value to 100 at index 1
my_doubly_linked_list_set.set_value(1, 100)
# print node value
print("The node at index 1 is {}".format(
    my_doubly_linked_list_set.get(1).value))  # 100

print("----- insert -----")
# insert(index, value) method
# setup DLL with nodes
my_doubly_linked_list_insert = DoublyLinkedList(1)
my_doubly_linked_list_insert.append(3)
# print initial DLL
print(my_doubly_linked_list_insert.print_list())  # 1 3 None
# invoke insert method at index 1 (2nd element)
my_doubly_linked_list_insert.insert(1, 2)
print(my_doubly_linked_list_insert.print_list())  # 1 2 3 None

print("----- remove -----")
# remove(index)
# setup DLL with nodes 0 1 2
my_doubly_linked_list_remove = DoublyLinkedList(0)
my_doubly_linked_list_remove.append(1)
my_doubly_linked_list_remove.append(2)
print(my_doubly_linked_list_remove.print_list())  # 0 1 2 None
# remove element at indec 1
print("The node removed at index 1 is {}".format(
    my_doubly_linked_list_remove.remove(1).value
))
print(my_doubly_linked_list_remove.print_list())  # 0 2 None
