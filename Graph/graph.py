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

    # add edge method
    # eg.
    # {
    #   1: [2],
    #   2: [1]
    # }
    def add_edge(self, vertex1, vertex2):
        # append the list of the key or vertex1 with the value of vertex2
        # only want to append if both vertices are present in the adj list
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False

    # remove edge method
    def remove_edge(self, vertex1, vertex2):
        # check if both the vertices exist as keys in adj list
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            # need to handle edge case of vertices that are not connected by edges
            # this means the vertices will not have each other as keys in adj list
            # handle by try-except
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
            except ValueError:
                # if ValueError happened pass and continue on
                pass
            return True
        return False

    # remove vertex method
    # bidirectional connections have efficiency
    # if D has an edge with another vertex A
    # this implies the other vertex has an edge connection with D
    def remove_vertex(self, vertex):
        # check in vertex exist in the adj list
        if vertex in self.adj_list.keys():
            # if vertex exist in adj list -> loop through the list
            for other_vertex in self.adj_list[vertex]:
                # go through the list of edges associated with vertex
                # remove the edge it has with the vertex that we are removing out of Graph
                self.adj_list[other_vertex].remove(vertex)
            # after removing all the related connection vertices
            # del the vertex key from the adj list
            del self.adj_list[vertex]
            return True
        return False


# sample setup for Graph
print("----- test Graph setup class -----")
my_graph = Graph()

print("----- add_vertex method -----")
my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.print_graph()  # 1: [] 2: []

print("----- add_edge method -----")
my_graph.add_edge(1, 2)

my_graph.print_graph()  # 1: [2] 2: [1]

print("----- remove_edge method -----")
my_graph_remove_edge = Graph()

# set up (adding vertices and edges)
my_graph_remove_edge.add_vertex('A')
my_graph_remove_edge.add_vertex('B')
my_graph_remove_edge.add_vertex('C')
my_graph_remove_edge.add_vertex('D')

my_graph_remove_edge.add_edge('A', 'B')
my_graph_remove_edge.add_edge('B', 'C')
my_graph_remove_edge.add_edge('C', 'A')

my_graph_remove_edge.print_graph()  # A: ['B', 'C'] B: ['A', 'C'] C: ['B', 'A']

# remove edge
print("----- removing edge -----")

my_graph_remove_edge.remove_edge('A', 'B')
my_graph_remove_edge.print_graph()  # A: ['C'] B: ['C'] C: ['B', 'A']

# ValueError (x not in list) as edge case was not handled in remove_edge method yet
my_graph_remove_edge.remove_edge('A', 'D')
my_graph_remove_edge.print_graph()  # A: ['C'] B: ['C'] C: ['B', 'A'] D: []

# remove vertex
print("----- remove_vertex method -----")
my_graph_remove_vertex = Graph()
my_graph_remove_vertex.add_vertex('A')
my_graph_remove_vertex.add_vertex('B')
my_graph_remove_vertex.add_vertex('C')
my_graph_remove_vertex.add_vertex('D')

my_graph_remove_vertex.add_edge('A', 'B')
my_graph_remove_vertex.add_edge('A', 'C')
my_graph_remove_vertex.add_edge('A', 'D')
my_graph_remove_vertex.add_edge('B', 'D')
my_graph_remove_vertex.add_edge('C', 'D')

# A : ['B', 'C', 'D'] B : ['A', 'D'] C : ['A', 'D'] D : ['A', 'B', 'C']
my_graph_remove_vertex.print_graph()

# removing vertex
print("----- removing vertex -----")
my_graph_remove_vertex.remove_vertex('D')

my_graph_remove_vertex.print_graph()  # A: ['B', 'C'] B: ['A'] C: ['A']
