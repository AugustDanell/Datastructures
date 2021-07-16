# graph
# A graph is a datastructure with a network of nodes that are glued together by edges. A graph can be either directed or
# undirected. Directed means that one can access node2 from an edge emerging from node1, to node2. An undirected graph
# also makes it so that such a directed edge is symmetric, if one can go from node2 from node 1, one can also go back to
# node 1, from node 2. A graph is undirected by default as per the default value false for the parameter 'directed' below.
# One can also set this to be true when creating the graph, making it so the edges are non-symmetric. The datastructure
# can bind together a network of nodes and make typical graph searches such as DFS and BFS implemented by queues and
# stacks specifically. Moreover there is a function to see if the graph is of a tree structure.

import stack
import queue


class node:
    def __init__(self, name = None):
        self.name = name
        self.edges = []

    def set_neighbors(self,adj_list):
        for node in adj_list:
            self.edges.append(node)

    def __str__(self):
        return self.name

class graph:
    def __init__(self, start, directed = False):
        self.start = start
        self.node_list = []
        self.adjacency_list = {}
        self.add_node(start)
        self.visited = {}
        self.directed = directed

    def add_node(self, node):
        self.node_list.append(node)
        self.adjacency_list[node] = []


    def add_edge(self, node1,node2):
        if(not self.directed):
            self.adjacency_list[node1] += [node2]
            self.adjacency_list[node2] += [node1]
        else:
            self.adjacency_list[node1] += [node2]

    # print_edges()
    # prints the adjacency list of the graph:
    def print_edges(self):
        print("ADJACENCY LIST:")
        for entry in self.adjacency_list:
            l = [e.__str__() for e in self.adjacency_list[entry]]
            print("Entry " + entry.__str__() + ":", l)

    # search()
    # This is a generalized searching method, if one puts in structure = stack it will be a DFS search whereas if one
    # inserts a structure = queue, this will instead be a BFS search. DFS and BFS down below both use this generalized
    # search as a helper function, setting it up with DFS and BFS respectively.

    def search (self, node, level, structure):
        neighbors = structure
        if(not self.visited.__contains__(node)):
            print("Hello I am node:", node, "At search attempt:", level)
            self.visited[node] = True
            nodes = self.adjacency_list[node]       # Returns a list of neighbors.
            for i in range (len(nodes)):
                neighbors.push(nodes[i])            # Pushing neighbors.

            while(neighbors.size > 0):
                self.search(neighbors.pop(), level + 1, structure)

    def DFS(self, node, level):
        print("\nDEPTH FIRST SEARCH: ")
        self.visited = {}
        self.search(node, level, stack.stack())

    def BFS(self, node, level):
        print("\nBREADTH FIRST SEARCH: ")
        self.visited = {}
        self.search(node, level, queue.queue())

    # isTree()
    # A function that goes through the current adjacency list, looking for any cycles. Worth to note is that this is
    # implemented with regard to an undirected graph

    def isTree(self, start):
        tree = True
        for i in self.adjacency_list:
            for j in self.adjacency_list:
                if(i == j):
                    continue
                else:
                    for n in self.adjacency_list[i]:
                        if(n in self.adjacency_list[j] and j in self.adjacency_list[i]):
                            print(n, self.adjacency_list[j])
                            tree = False
                            break

                    if(not tree):
                        break

            if(not tree):
                break

        return tree
