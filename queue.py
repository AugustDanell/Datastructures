# Queue
# The queue is, one can say, the inverse of the stack. It is only possible to pop the first element rather than the last.
# The queue is very easily conceptualized, it is just to close one's eyes and imagine oneself in a queue outside the
# best carusel or attraction of one's child hood. The queue works exactly like a regular queue that is you push a value
# and that value that is pushed to the queue kindly awaits its turn to enter. This is implemented using a linked list as
# a linked list can easily remove the first element in constant time O(1) you only need a pointer for that. A generalized
# graph traversal using a queue will amount to a BFS.

import linked_list
class queue:
    def __init__(self):
        self.linkedList = linked_list.linked_list()
        self.size = 0

    def push(self, element):
        self.linkedList.insertion(element)
        self.size += 1

    def pop(self):
        try:
            pop_element = self.linkedList.remove_first()
            self.size -= 1

            return pop_element
        except:
            print("You cannot pop from an empty queue!")

    def peek(self):
        return self.linkedList.top_node.value

    def element_wise_print(self):
        self.linkedList.element_wise_print()
