'''
   Linked List
   A linked list is a datastructure where each node holds a value and a reference to the next node. It is like a chain
   where one can find a value through another node, traversing the chain until a value is found. The linked list is slow
   when we either want to remove/find/add an element in the middle O(N), or if we want to remove the very last element.
   Remember, we cannot traverse backwards and to remove an element is like 'unhooking' its links, and so we must have the
   element before whatever element we want to remove. As such removing the last element is always of time complexity N.
'''

class node:
    def __init__(self, val = None):
        self.value = val
        self.nextVal = None

class linked_list:
    def __init__(self):
        self.bot_node = None
        self.top_node = None
        self.size = 0

    def __len__(self):
        return self.size

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

    def find_element(self, val):
        current_node = self.bot_node
        for i in range(self.size):
            if(current_node.value == val):
                return True
            current_node = current_node.nextVal

        return False

    def replace_on_index(self,val,i):
        assert self.size > i, "Linked List Insertion: The index has to be within the list."
        insertion_node = node(val)
        index = 0
        current_node = self.bot_node
        while(index -1 < i):
            current_node = current_node.nextVal
            index += 1

        insertion_node.nextVal = current_node.nextVal
        current_node.nextVal = insertion_node

    def remove_on_index(self, index):
        assert self.size > index, "Unvalid operation, linked list out of bounds."
        current_node = self.bot_node
        i = 0
        while(not i+1 == index):
            current_node = current_node.nextVal
            i+= 1

        if(i+2 == self.size):
            current_node.nextVal = None
        else:
            current_node.nextVal = (current_node.nextVal).nextVal
        self.size -= 1

    def remove_last(self):
        self.remove_on_index(self.size-1)
