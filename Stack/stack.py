class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# similar to how a LinkedList is setup
# do not need to keep track of bottom as stack is LIFO
# only need to keep track of top for push and pop methods


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    # print method helper
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


# sample print stack
print("----- test stack setup class -----")
my_stack = Stack(4)
my_stack.print_stack()  # 4
