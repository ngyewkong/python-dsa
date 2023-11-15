# Graph Data Structure
# Vertex (Node) and Edge (Line connecting 2 Vertices)
# Non-weighted
# Weighted Edges (Connection with different value attached to it - costs)
# used in GMaps or Network Routing Protocols
# Bidirectional (no arrows on edges node-node eg friend follow you, you follow friend on fb)
# Directional (node->node)
# LinkedLists are a form of Tree & Tree is a form of graph (Directional Graph)

# Adjacency Matrix in Graph (for bidrectional graph)
# eg a pentagon of ABCDE
#   A B C D E
# A 0 1 0 0 1
# B 1 0 1 0 0
# C 0 1 0 1 0
# D 0 0 1 0 1
# E 1 0 0 1 0

# Line of symmetry down the 45deg line of 0s
# for bidirectional graph, it is a mirror image down the 45deg line
# for weighted graph, store the weights in the matriz instead of 1 where there is connecting edges

# Adjacency List (using Dictionary)
# the ref vertex is the key
# eg {
#   'A': ['B', 'E'],
#   'B': ['A', 'C'],
#   'C': ['B', 'D'],
#   'D': ['C', 'E'],
#   'E': ['D', 'A']
# }

# Big(O) of Graph
# Space Complexitty
# Adjacency Matrix vs Adjacency List impl
# Matrix: need to store irrelevant details (other vertices that are not connected)
# List: only store the adjacent vertices
# adding a vertex
# Matrix: O(|V|^2)
# List: O(1) dictionary
# adding a edge
# Matrix: O(1)
# List: O(1)
# removing edge
# Matrix: O(1)
# List: O(|E|) need to iterate through the list and find the values to remove
# removing vertex
# Matrix: O(|V|^2)
# List: O(|V| + |E|)

class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    # add vertex method
    def add_vertex(self, vertex):
        # add vertex and set an empty list
        # check to make sure no duplicates
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False


# sample setup for Graph
print("----- test Graph setup class -----")
my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()
