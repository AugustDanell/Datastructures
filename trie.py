'''
   Trie
   Trie is an interesting datastructure though presumably with a specialized use as compared to many other datastructures.
   Trie is a tree where every node has a list of children, and in our implementation we map that with a key, so that key
   can naturally be seen as an edge, if you so will. current_node.children_list[a] = new_node, means that from one node,
   we can traverse down an edge to a new node. The edges are letters and the nodes form networks of these letters as well
   as holding a truth value val. If val is set as true that means that the combination of edges down to
'''

class trie_node():
    def __init__(self):
        self.children_list = {}
        self.val = False
        self.size = 0

    def __len__(self):
        return self.size


    def has_child(self, letter):
        if(self.children_list.__contains__(letter)):
            return True
        else:
            return False

    '''
       insert_word()
       Simply iterates over each character or letter in an inserted word and inserts them as nodes
    '''

    def insert_word(self, word):
        self.size += 1
        current_node = self
        word_length = len(word)

        for i in range(word_length):
            letter = word[i]

            if(not current_node.has_child(letter)):
                current_node.create_child(letter)

            current_node = current_node.children_list[letter]


        current_node.val = True

    def does_word_exist(self, word):
        current_node = self
        word_length = len(word)

        for i in range(word_length):
            letter = word[i]
            if(current_node.has_child(letter)):
                current_node = current_node.children_list[letter]
            else:
                return False

        return current_node.val

    def create_child(self, letter):
        inserted_node = trie_node()
        inserted_node.val = False
        self.children_list[letter] = inserted_node