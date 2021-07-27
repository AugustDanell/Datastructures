'''
   Stack
   The stack is a simple datastructure, one typically conceptualize it as a stack of plates, only the plates
   can be of different datatypes, strings, integers etc. As per the pythonic way of storing data in
   lists, where the list does not have to be homogenous in relation to the type of data that is being
   stored, we can imagine the stack as a stack of objects just piled upon each other without care for the
   data being of the same type. A generalized graph traversal using a queue will amount to a DFS.
'''

class stack:
    def __init__(self):
        self.Internal_List = []
        self.size = 0

    def pop(self):
        element = self.Internal_List.pop(self.size-1)
        self.size -= 1

        return element

    def push(self, element):
        self.Internal_List.append(element)
        self.size += 1

    def __len__(self):
        return self.size