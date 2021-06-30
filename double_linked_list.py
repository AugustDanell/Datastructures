# double_linked_list
# This is the actual data structure that employs the use of nodes. We can traverse back and forth, to insert an element
# we can travel to that element through the list and this travel can be done in both ends. Insertion can, as in a normal
# list, be done in constant time. Deletion of the last element can also be done on constant time, in the double linked
# list, however, since we can travel one step back to the previous node and remove its pointer to the last node.
# Example: a -> b -> c, now we want to remove c, we do not have to traverse the entire list all we do is:
# 1. c (backwards) -> b, 2. remove the reference to c. Voila. This is one powerful advantage with the double linked list
# as compared to the single linked list.

# node
# This is a class that defines the behaviour of a node in the double linked list. A node has a connections both forwards
# as well as backwards, that is the "double-link" if you so will. The node also holds a value as such we can traverse the
# nodes and pick out a value, every node stores another node, and so it is liked the single linked list almost like a chain.
# The differance is, however, that in this list we can approach it from both ends, making operations such as deletion much
# quicker, much better.

class node:
    def __init__(self, value = None):
        self.val = value
        self.forward = None
        self.backward = None

class double_linked_list:
    def __init__(self):
        self.bot_node = None
        self.top_node = None
        self.size = 0

    # insertion()
    # A function that appends an element taken in as argument, in the form of a node, onto the list. One can conceptualize
    # it as appending a metal ring on a chain, we can save our last node and do this insertion in constant time.

    def insertion(self, element):
        currentNode = node(element)
        if(self.size == 0):
            self.bot_node = currentNode
            self.top_node = currentNode

        else:
            self.top_node.forward = currentNode
            currentNode.backward = self.top_node
            self.top_node = currentNode

        self.size += 1

    # there_and_back_again()
    # This function tests both forward and backward traversal in travelling from the start node to the end node, and then
    # from the end node to the start node, all while printing the current node.

    def there_and_back_again(self):
        currentNode = self.bot_node

        print("Forward Check:")
        print("Node:  1", currentNode.val)
        for i in range(1,self.size):
            currentNode = currentNode.forward
            print("Node: ", i + 1, currentNode.val)

        print("\nBackward Check:")
        for i in range(0, self.size):
            print("Node: ", self.size-i, currentNode.val)
            currentNode = currentNode.backward