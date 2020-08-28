class Node:
    def __init__(self):
        self.value = 0
        self.next = None


class BT:
    def __init__(self):
        self.root = Node()

class LinkedList:
    def __init__(self):
        self.head = Node()


def list_of_depth(tree_lists, root, level):
    if root == None: return None
    tree_list = None
    if len(tree_lists) == level:
        tree_list = LinkedList()
        tree_lists.append(tree_list)
    else:
        tree_list = tree_lists[level]
    tree_list.append(root)
    list_of_depth(root.)


