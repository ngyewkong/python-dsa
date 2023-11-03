# Trees can be perfect, full and/or complete
# All nodes can only have one parent
# One parent 2 Children are Binary Trees
# Nodes with no Childeren nodes are Leaf nodes

# Binary Search Trees (BSTs) if the children node value > parent node it is going the on the right side of parent node
# the filling up of the nodes start from root node
# eg 47, 21, 76, 52, 82, 18, 27 with 47 as root node
#           47            2^1 - 1 = 1 node
#         21  76          2^2 - 1 = 3 nodes
#       18 27 52 82       2^3 - 1 = 7 nodes
# as number of layers in BSTs increase the number of nodes approx 2^n nodes
# lookup a node is O(log n)
# insert a node is O(log n)
# remove a node is O(log n)
# BSTs are very efficient (achieved by divide and conquer)
# assumption is BSTs are forked (if never forked is fundamentally a LinkedList which is O(n))
# comparison btw LinkedList & BSTs
# lookup BSTs is btr [O(n) vs O(log n)]
# remove BSTs is btr [O(n) vs O(log n)]
# insert LinkedList is btr [O(1) vs O(log n)]
# so if they asked for fast insertion and retrieval is not frequent or need to ensure all data are captured
# LinkedList is btr in this case

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        # initialize an empty BST
        self.root = None

    # insert method
    def insert(self, value):
        new_node = Node(value)
        # check for base case if BST root is empty
        if self.root == None:
            self.root = new_node
            # return statement needed as we do not need to run the later parts of code
            # since an insertion has happened
            return True
        # setup temp variable for the rest of the cases
        temp = self.root
        # while loop
        while (True):
            # edge cases
            # when new node is the same value as any existing node return False
            # BST cannot have duplicated node values
            if new_node.value == temp.value:
                return False
            # the logic for smaller value go left bigger value go right of parent node
            if new_node.value < temp.value:
                # check the next node after temp on the left
                if temp.left is None:
                    temp.left = new_node
                    return True
                # if temp.left the next layer has a node
                # shift the temp to next layer to continue traversing
                temp = temp.left
            else:
                # inserting right for greater value
                if temp.right is None:
                    temp.right = new_node
                    return True
                # if there is a node after temp
                # shift the temp to next layer to continue traversing
                temp = temp.right

    # contains method to find a particular value
    def contains(self, value):
        # base case if root is None -> BST is empty return False and exit
        if self.root is None:
            return False
        # need a variable to traverse down the tree
        temp = self.root
        # if temp is not None continue loop
        while (temp is not None):
            # lookup value smaller than temp go left
            if (value < temp.value):
                # traverse next layer
                temp = temp.left
            # # loopup value greater than temp go right
            elif (value > temp.value):
                # traverse the right side
                temp = temp.right
            # if temp is not None and it is traversing till the end
            # loopup node is in the tree
            # return True
            else:
                return True
        # when temp is None after Traversal -> end of tree still no match
        # return False
        return False


# sample setup for BST
print("----- test BST setup class -----")
my_tree = BinarySearchTree()
print(my_tree.root)

# insert
print("----- insert -----")
# setup BST with 2 as root node 1 and 3 as children node
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(1)
print("The root node value is {}".format(my_tree.root.value))  # 2
print("The left child node value is {}".format(my_tree.root.left.value))  # 1
print("The right child node value is {}".format(my_tree.root.right.value))  # 3

# contains
print("----- contains -----")
my_tree.insert(76)
my_tree.insert(52)
my_tree.insert(82)

print("Does node 52 exists in the BST? Ans: {}".format(
    my_tree.contains(52)))  # True
print("Does node 82 exists in the BST? Ans: {}".format(
    my_tree.contains(82)))  # True
print("Does node 10 exists in the BST? Ans: {}".format(
    my_tree.contains(10)))  # False
