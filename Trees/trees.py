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


# sample setup for BST
print("----- test BST setup class -----")
my_tree = BinarySearchTree()
print(my_tree.root)
