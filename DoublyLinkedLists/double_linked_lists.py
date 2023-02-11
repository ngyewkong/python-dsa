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


my_doubly_linked_list = DoublyLinkedList(7)
# my_doubly_linked_list.print_list()
print(my_doubly_linked_list.print_list())  # 7 None

# append
my_doubly_linked_list.append(2)
print(my_doubly_linked_list.print_list())  # 7 2 None

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
