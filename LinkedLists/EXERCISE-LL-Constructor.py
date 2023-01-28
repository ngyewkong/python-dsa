class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    #################################


class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
    def __init__(self, value) -> None:
        # pass the value into the Node class to create starting Node instance
        starting_node = Node(value)
        self.head = starting_node
        self.tail = starting_node
        self.length = 1
    ###############################


my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""
