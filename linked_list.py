# Linked List
# A linked list is a datastructure where each node holds a value and a reference to the next node. It is like a chain
# where one can find a value through another node, traversing the chain until a value is found. The linked list is slow
# when we either want to remove/find/add an element in the middle O(N), or if we want to remove the very last element. 
# Remember, we cannot traverse backwards and to remove an element is like 'unhooking' its links, and so we must have the 
# element before whatever element we want to remove. As such removing the last element is always of time complexity N. 
# TODO: Implement insertions, deletions and find functions.

class node:
    def __init__(self, val = None):
        self.value = val
        self.nextVal = None

class linked_list:
    def __init__(self):
        self.bot_node = None
        self.top_node = None
        self.size = 0

    def insertion(self, val):
        new_node = node(val)
        if(self.size > 0):
            self.top_node.nextVal = new_node
        else:
            self.bot_node = new_node

        self.top_node = new_node
        self.size += 1

    # Element wise print of the linked list:
    def element_wise_print(self):
        currentNode = self.bot_node
        print(currentNode.value)

        for i in range(1, self.size):
            currentNode = currentNode.nextVal
            print(currentNode.value)

    def remove_first(self):
        currentNode = self.bot_node
        self.bot_node = currentNode.nextVal
        self.size -= 1

        return currentNode.value
    
    # TODO
    def find_element(self):
        pass
    
    def insert_on_index(self,val,i):
        pass
    
    def remove_on_index(self, i):
        pass
    
    def remove_last(self):
        pass
