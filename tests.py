import linked_list
import queue
import binary_search_tree as bin_tree_maker
import trie
import stack
import graph
import hotdog

# Stack (Filo, first in, last out):
test_stack = False
if(test_stack):
    st = stack.stack()
    assert st.size == 0
    st.push("hey hey")
    assert st.size == 1
    e = st.pop()
    assert e == "hey hey"
    assert st.size == 0

test_linked_list = False
if(test_linked_list):
    lin_list = linked_list.linked_list()
    lin_list.insertion("Hello")
    lin_list.insertion("There")
    lin_list.element_wise_print()
    lin_list.remove_first()
    lin_list.element_wise_print()

    lin_list.insertion("Hey")
    lin_list.insertion("baby")
    lin_list.insertion("girl")
    assert lin_list.size == 3

test_queue = False
if(test_queue):
    q = queue.queue()
    q.push("General")
    q.push("Kenobi")

    q.element_wise_print()
    print("Popping top element: ", q.pop())
    print("Now printing again: ")
    q.element_wise_print()
    q.pop()

    q.push("hey")
    assert "hey" == q.pop()
    assert q.size == 0

test_graph = True
if(test_graph):
    # Testing the following graph g2, with startnode C3.
    #      1 2  3  4  5
    #    | - -  -  -  -
    # A  |      x
    # B  |      x
    # C  |x  x  o  x  x
    # D  |      x
    # E  |      x

    C1,C2,C3,C4,C5 = graph.node("C1"), graph.node("C2"), graph.node("C3"), graph.node("C4"),graph.node("C5")
    A3, B3, D3, E3 = graph.node("A3"), graph.node("B3"), graph.node("D3"),graph.node("E3")
    g2 = graph.graph(C3)
    g2.add_node(C1)
    g2.add_node(C2)
    g2.add_node(C4)
    g2.add_node(C5)

    g2.add_edge(C1,C2)
    g2.add_edge(C2,C3)
    g2.add_edge(C3,C4)
    g2.add_edge(C4,C5)

    g2.add_node(A3)
    g2.add_node(B3)
    g2.add_node(D3)
    g2.add_node(E3)
    g2.add_edge(C3,B3)
    g2.add_edge(C3,D3)
    g2.add_edge(D3,E3)
    g2.add_edge(B3,A3)
    assert g2.isTree(C3)

test_bin_tree = False
if (test_bin_tree):
    bin_tree = bin_tree_maker.binary_tree(5)
    bin_tree2 = bin_tree_maker.binary_tree(1)
    bin_tree.insert(3)
    bin_tree.insert(7)
    bin_tree.insert(9)
    bin_tree.print()
    assert bin_tree.__contains__(3)
    assert bin_tree.__contains__(5)
    assert not bin_tree.__contains__(4)
    assert bin_tree.depth() == 3
    assert bin_tree2.depth() == 1

test_trie = False
if(test_trie):
    t = trie.trie_node()
    t.insert_word("hi")
    t.insert_word("hit")
    t.insert_word("hitmarker")
    assert t.does_word_exist("hi")
    assert t.does_word_exist("hit")
    assert t.does_word_exist("hitmarker")

    contact_list =trie.trie_node()
    list_of_contacts = ["Daniel", "Tobias", "Dennis", "Simon", "Augustus", "Elenor", "Lucasovic", "Andrej", "Sebastianus", "Johnhannesian"]
    for c in list_of_contacts:
        contact_list.insert_word(c)

    for a in list_of_contacts:
        assert contact_list.does_word_exist(a)

test_hotdog = False
if(test_hotdog):
    hottie = hotdog.hotdog()
    hottie.insert(1)
    hottie.insert(2)
    hottie.insert(3)
    hottie.insert(4)
    pop_element = hottie.pop()
    assert pop_element in [2,3]
    pop_element = hottie.pop()
    assert pop_element in [2,3]
    pop_element = hottie.pop()
    assert pop_element in [1,4]
    pop_element = hottie.pop()
    assert pop_element in [1,4]