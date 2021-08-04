'''
   binary search tree
   The binary search tree is a datastructure in which every node holds a value and can span from 0-2 nodes, that is have
   one left and one right child, and it is to be organized as such that a value that is inserted for instance is inserted
   to the right hand side of a current node if the new value is grater than that of the previous node. The problem is
   that this can create unbalance. Etc, [1,2,3,4,5,6] would amount to a tree that is completely unbalanced, a right side
   tree, and it would degenerate to a linked list.

   Operations are done by traversing down the nodes of the tree, and the amount of time it will take is entirely dependant
   on the depth of the tree. That is why a balanced search tree naturally performs much better, a so called heap. In such a
   structure we can insert, find and delete values in O(log n) time since the depth will be in logarithmic space, that is for
   each node in existance there are two leaves, and so every row, every layer if you will, will have twice as much space as
   the previous layer, 2^i, where i is the row, starting at row 0 which is the root.
'''

import queue

# Insertion, done in best case: (log n), worst case O(n) if for instance the problem instance might be in this order:
class binary_tree():
    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.data = val

    def insert(self, data):
        val = self.data
        if data < val:
            if self.left_child is None:
                self.left_child = binary_tree(data)
            else:
                self.left_child.insert(data)
        elif data == val:
            self.data = data
        else:
            if self.right_child is None:
                self.right_child = binary_tree(data)
            else:
                self.right_child.insert(data)
    '''
       contains
       Uses a similar logic as does insertion to traverse the tree from the root node, we use the tree structure knowing
       that left nodes are lesser than the current value and right nodes greater, and so we can traverse down the tree.
       Naturally, the time complexity remains the same that is O(N), but best case: theta(log N).
    '''

    def __contains__(self, item):
        if self is None:
            return False

        val = self.data
        if(item == val):
            return True

        elif(item > val):
            if(self.right_child is None):
                return False
            else:
                return self.right_child.__contains__(item)
        else:
            if(self.left_child is None):
                return False
            else:
                return self.left_child.__contains__(item)
    '''
       delete
       See Insertion/Contains to understand why it is O(N) and theta(log N).
       One conundrum that might exist in the deletion of a node is the deletion of a middle node, that is a node that is
       stringing together parts of the tree. The way that such a deletion can be made is to swap nodes down to a leaf and
       then to trim away that specific leaf.
    '''

    def delete(self, item):
        if not self.__contains__(item):
            return False

        # TODO: Vad gör vi om exempelvis en "mittennod" tas bort

    '''
       depth() & maximum_depth()
       A function that traverses down the tree from the root down to a leaf and keeps a counter so as to know what level
       we are in. The function uses recursion, that is it returns the max recursively of a left/right way, and if there
       is only one way to traverse it does just that. depth(), defined below, is a function that starts the recursion that
       is maximum depth, which recurses down until ground floor has been reached.
    '''

    def maximum_depth(self, level):
        if self is None:
            return level -1


        if (not self.right_child is None) and (not self.left_child is None):
            return max(self.right_child.maximum_depth(level + 1), self.left_child.maximum_depth(level + 1))

        elif not self.right_child is None:
            return self.right_child.maximum_depth(level + 1)

        elif not self.left_child is None:
            return self.left_child.maximum_depth(level + 1)


        return level

    def length(self):
        r = self.right_child is None
        l = self.left_child is None

        if(l and r):
            return 1
        elif(l and not r):
            return 1 + self.right_child.length()
        elif(r and not l):
            return 1 + self.left_child.length()
        else:
            return 1 + self.left_child.length() + self.right_child.length()

    def depth(self):
        return self.maximum_depth(1)

    # compare todo
    def compare(self, bin_tree):
        pass

    '''
       print
       A recursive function that much like the depth-recursive call uses recursion to travel down nodes, printing their
       value and their level, right_level and left_level, respectively. These levels start at (0,0), which signifies
       origo, the point of origin. For each traversal in the right the second of these two values increases, and so
       the overall depth, one can say, is left_level + right_level, and since this is commutative there might be a tree
       where two nodes have the same level, if for instane you traverse left, and then right, this node has the same left
       and right level specifically as does the traversal right to left, even though its not the same node.
       The traversal order, and so printing order, is depth first starting from the right side, moving left.
    '''

    def print(self, left_level = 0, right_level = 0, q = queue.queue()):
        if self is None:
            pass
        else:
            print("Data: ", self.data, "At left level:", left_level, "Right level:", right_level)
            if not self.right_child is None:
                self.right_child.print(left_level, right_level +1)

            if not self.left_child is None:
                self.left_child.print(left_level + 1, right_level)

'''
   depth_first_traversal
   Simply traverses down the depth of the tree first, that is, we are traversing down until we come to a leaf with no children.
'''

    def depth_first_traversal(self):
        if(self.left_child is not None):
            self.left_child.depth_first_traversal()

        if(self.right_child is not None):
            self.right_child.depth_first_traversal()
'''
   breath_first_traversal
   Breath first is when we are traversing down the tree "one generation" at a time, if one so will. Both of these traversal functions can in practice
   take in some working function, maybe print (like the member function print above), or do something else. 
'''
    def breath_first_traversal(self, stored_recursions = []):
        print(self.data)

        if(self.left_child is not None):
            stored_recursions.append(self.left_child)

        if(self.right_child is not None):
            stored_recursions.append(self.right_child)

        if(not stored_recursions == []):
            element = stored_recursions[0]
            stored_recursions.remove(element)
            element.breath_first_traversal(stored_recursions)
