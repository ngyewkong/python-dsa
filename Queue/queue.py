class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# queue is FIFO
# using LinkedList impl for queue
# take note to use the start of LinkedList to enqueue
# use end of LinkedList to dequeue
# this way both methods are O(1)
class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    # print queue helper method
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # enqueue method (adding to end of queue)
    def enqueue(self, value):
        new_node = Node(value)
        # base case empty queue
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            # update the last pointer to the new_node
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    # dequeue method (remove first node)
    def dequeue(self):
        # base case 1 - no items in the queue
        if self.length == 0:
            return None
        # base case 2 - only got 1 item in the queue
        # initialise variable to hold node that is going to be removed
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            # remove temp.next pointer to remove from original queue
            temp.next = None
        self.length -= 1
        return temp


# sample print stack
print("----- test queue setup class -----")
my_queue = Queue(4)
my_queue.print_queue()  # 4

# enqueue
print("----- enqueue -----")
my_queue.enqueue(8)
my_queue.enqueue(16)
my_queue.print_queue()  # 4 8 16 (FIFO)

# dequeue
print("----- dequeue -----")
print("The node removed from the queue is {}".format(
    my_queue.dequeue().value))  # 4
my_queue.print_queue()  # 8 16
my_queue.dequeue()  # 8 popped
my_queue.dequeue()  # 16 popped
print("The node removed from the queu is {}".format(my_queue.dequeue()))  # None
