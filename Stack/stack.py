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

    # push method
    # rmb the LinkedList impl for Stack the pointer point from top (last element)
    def push(self, value):
        new_node = Node(value)

        # base case for no node in the Stack
        if self.height == 0:
            self.top = new_node
        # case to insert node at the end of Stack
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    # pop method (LIFO so only the top element is popped)
    def pop(self):
        # base case if top is None -> return
        if self.height == 0:
            return None
        # case that has nodes to be popped
        # return the node that is going to be popped
        # need a variable to hold the node object
        temp = self.top
        self.top = self.top.next
        # remove the pointer of temp.next to remove from original stack
        temp.next = None
        self.height -= 1
        return temp


# sample print stack
print("----- test stack setup class -----")
my_stack = Stack(4)
my_stack.print_stack()  # 4

print("----- push -----")
my_stack.push(8)
my_stack.push(16)
my_stack.print_stack()  # 16 8 4 (LIFO)

print("----- pop -----")
print("The node that is being popped from stack is {}".format(
    my_stack.pop().value))  # 16
my_stack.print_stack()  # 8 4
