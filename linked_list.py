class node:
    def __init__(self, val = None):
        self.value = val
        self.nextVal = None

class linked_list:
    def __init__(self):
        self.bot_node = None
        self.size = 0

    # Insertion is of O(n), we exhaust the entire list to get to the last val:
    def insertion(self, val):
        new_node = node(val)
        if(self.size > 0):
            currentNode = self.bot_node
            for i in range(1, self.size):
                currentNode = currentNode.nextVal
            currentNode.nextVal = new_node
        else:
            self.bot_node = new_node

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
