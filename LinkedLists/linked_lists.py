# Lists vs Linked Lists (LL)
# Lists have indexes LL do not
# LL have variable/pointer called head which points to the first node in the LL
# LL have variable/pointer called tail which points to the last node in the LL
# LL last node points to None
# each node in LL points to the next node (they can be at different places in memory need not be in sequential)

# LL Big O
# LL methods
# append (end node) -> O(1)
# pop (end node) -> O(n) (need to iterate through from head)
# prepend (start node) -> O(1)
# remove (start node) -> O(1)
# insert (middle of list) -> O(n)
# remove (middle of list) -> O(n)
# lookup (getter by value or by index) -> O(n)
# reverse

# Node contains the value as well as the pointer -> similar to a dictionary

# sample of how a LL impl will look like (not the actual impl)
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": {
                    "value": 4,
                    "next": None
                }
            }
        }
    }
}

# to get the value of the third node (23)
# print(head['next']['next']['value'])

# Actual way to get value 23 using the Linked List correct impl
# print(my_linked_list.head.next.next.value)

# Node class -> helper for node creation in LL
# Node simply has value and next attributes
# calling Node class from LL methods
# just need to pass in the value for the specific instance of Node


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# LinkedList impl with three methods append, prepend & insert


class LinkedList:
    # realise that creation of node is in the constructor, append, prepend and insert methods
    # create another class called Node for Node creation
    # which the 4 methods will call to create node when required

    # constructor going to initialize a new LinkedList instance
    # create a Starting Node with the value passed in
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node  # points the head of LL to this starting node
        self.tail = new_node  # points the tail of LL to this starting node
        self.length = 1  # keep track of the length of the LL

    # create a print LL values function to track the values in the LL
    def print_linked_list(self):
        temp = self.head  # set temp to head of LL which contains Node instance
        while temp is not None:
            print(temp.value)

            # shift temp pointer to the nxt node
            temp = temp.next

    # append is going to create a new Node to the end of the LL
    def append(self, value):
        next_node = Node(value)
        # if head pointer points to None (initial case)
        if self.head == None:
            self.head = next_node
            self.tail = next_node
        else:
            # already have existing node
            # shift current tail pointer to the next_node
            self.tail.next = next_node
            # set tail pointer to the next_node
            self.tail = next_node
        # increment LL length by 1
        self.length += 1
        # for other methods that might use the append method & require it to return boolean
        return True

    # pop is going the remove the Node at the end of LL
    def pop(self):
        # edge case 1 -  when the LL both head & tail pointers point to None
        if self.length == 0:
            return None
        # normal case - set the tail to prev and set the next to None
        # trick here is to set 2 pointers that tracks if it goes to end of LL (points to None)
        temp = self.head
        pre = self.head
        while (temp.next is not None):
            pre = temp
            temp = temp.next
        # set the tail to prev Node and next to None
        # decrement length of LL by 1
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # edge case 2 - when the LL only has 1 Node
        if self.length == 0:
            self.head = None
            self.tail = None
        # return the node that was removed
        return temp

    # prepend is going to create a new Node to the start of the LL
    def prepend(self, value):
        # create new node
        new_starting_node = Node(value)
        # edge case 1 - empty LL
        if self.length == 0:
            self.head = new_starting_node
            self.tail = new_starting_node
        else:
            # do not need a new var to store the curr head value (optimised)
            new_starting_node.next = self.head
            self.head = new_starting_node
        # rmb to increment the length of LL
        self.length += 1
        return True

    # pop first item out of LL
    def pop_first(self):
        # edge case 1 - when LL has 0 Node
        if self.length == 0:
            return None
        # normal case - sets a var to the curr head -> shift head to next
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # edge case 2 - when LL has 1 Node
        # when there is only 1 Node the decrement will cause length to go 0
        # which trigger the setting of tail to None
        if self.length == 0:
            self.tail = None
        return temp

    # getter & setter
    def get(self, index):
        # check for valid index (negative or out of bounds index -> invalid)
        if index < 0 or index >= self.length:
            return None
        # set a temp variable to start at head
        temp = self.head
        # use _ instead of i if we are not using the value of i
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        # check for valid index using getter
        temp = self.get(index)
        # when temp is valid
        if temp is not None:
            temp.value = value
            return True
        return False

    # insert is going to create a new Node to the whereever the index being passed in
    def insert(self, index, value):
        # initialise the new node to be inserted
        new_node = Node(value)
        # check for valid index
        if index < 0 or index > self.length:
            return False
        # add at start -> same as prepend (using self -> this instance of LL)
        if index == 0:
            return self.prepend(value)
        # add at end -> same as append
        if index == self.length:
            return self.append(value)
        # insert anywhere in the middle
        # need a temp variable that keep track of the node before the insertion
        # for pointing the prev Node to the new Node
        temp = self.get(index - 1)
        # set the new node to point to the curr next node
        new_node.next = temp.next
        # set the prev next node to the new node
        temp.next = new_node
        # increment length of LL
        self.length += 1
        # will return True if successful and False if not
        return True

    # remove at any index
    def remove(self, index):
        # check for valid index
        if index < 0 or index > self.length:
            return False
        # remove at start -> same as pop_first
        if index == 0:
            return self.pop_first()
        # remove at end -> same as pop
        if index == self.length - 1:
            return self.pop()
        # remove anywhere in the middle of the LL
        prev = self.get(index - 1)
        # using self.get for curr not optimised O(n) vs O(1)
        # curr = self.get(index)
        curr = prev.next
        # the prev next node shld point to the curr next node when removing the curr node
        prev.next = curr.next
        # remove node
        curr.next = None
        # decrement LL by 1
        self.length -= 1
        return curr

    # reverse the LL
    def reverse(self):
        # reverse the head and tail
        curr = self.head
        self.head = self.tail
        self.tail = curr
        # 2 more variables one before and after curr
        before = None
        after = curr.next
        for _ in range(self.length):
            after = curr.next
            # flip the arrow
            curr.next = before
            before = curr
            curr = after


# create a new LinkedList Instance with starting node value of 4
my_linked_list = LinkedList(4)
# append another node with value 12
my_linked_list.append(12)

# print(my_linked_list.value) # this give error (rmb LinkedList gt no value attributes)
# print(my_linked_list.head.value)  # print 4 the first node value

# print the whole LL
print(my_linked_list.print_linked_list())  # 4 -> 12 -> None

# print the node that is being removed from the LL
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())

# LL with prepend 3 -> 4 -> 12 -> None
my_linked_list.append(12)
my_linked_list.prepend(4)
my_linked_list.prepend(3)
print(my_linked_list.print_linked_list())  # 3 4 12 None

# pop first Node
my_linked_list.pop_first()
print(my_linked_list.print_linked_list())  # 4 12 None
my_linked_list.pop_first()
print(my_linked_list.print_linked_list())  # 12 None
my_linked_list.pop_first()
print(my_linked_list.print_linked_list())  # None

# getter & setter
my_linked_list_new = LinkedList(0)
my_linked_list_new.append(2)
my_linked_list_new.append(4)
my_linked_list_new.append(6)
print(my_linked_list_new.get(0))
print(my_linked_list_new.get(-1))  # None
print(my_linked_list_new.print_linked_list())  # 0 2 4 6 None

print(my_linked_list_new.set(1, 5))
print(my_linked_list_new.print_linked_list())  # 0 5 4 6 None

# insert
another_linked_list = LinkedList(2)
another_linked_list.prepend(0)
print(another_linked_list.print_linked_list())  # 0 2 None
another_linked_list.insert(1, 1)
print(another_linked_list.print_linked_list())  # 0 1 2 None

# remove
remove_linked_list = LinkedList(11)
remove_linked_list.append(3)
remove_linked_list.append(23)
remove_linked_list.append(7)

print(remove_linked_list.print_linked_list())  # 11 3 23 7 None
remove_linked_list.remove(2)  # remove Node 23 at index 2
print(remove_linked_list.print_linked_list())  # 11 3 7 None

# reverse
print(another_linked_list.print_linked_list())  # 0 1 2 None
another_linked_list.reverse()
print(another_linked_list.print_linked_list())  # 2 1 0 None
