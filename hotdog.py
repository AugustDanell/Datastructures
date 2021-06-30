# hotdog
# The hotdog is a datastructure without any seemingly useful utility as I can see right now, just a funny implementation
# of an idea. That idea is specifically to be a combination of a stack and a queue that is to have only the middle
# element being eligble for popping.

class hotdog:
    def __init__(self):
        self.length = 0
        self.flip = True
        self.middle_index = -1
        self.internal_list = []

    def insert(self, element):
        self.length += 1
        self.internal_list.append(element)

        if(self.flip):
            self.middle_index += 1

        self.flip = not self.flip

    def pop(self):
        element = self.internal_list.pop(self.middle_index)
        if not self.flip:
            self.middle_index -= 1

        self.flip = not self.flip
        self.length -= 1

        return element

    def print(self):
        print("Internal List:", self.internal_list, "Middle Element:", self.internal_list[self.middle_index])