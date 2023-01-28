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
        # if length of LL is 0 -> create node as per new node in constructor
        if self.length == 0:
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

    # # prepend is going to create a new Node to the start of the LL
    # def prepend(self, value):

    # # insert is going to create a new Node to the whereever the index being passed in
    # def insert(self, index, value):


# create a new LinkedList Instance with starting node value of 4
my_linked_list = LinkedList(4)
# append another node with value 12
my_linked_list.append(12)

# print(my_linked_list.value) # this give error (rmb LinkedList gt no value attributes)
# print(my_linked_list.head.value)  # print 4 the first node value

# print the whole LL
print(my_linked_list.print_linked_list())  # 4 -> 12 -> None
