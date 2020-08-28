
class Tree_node:
    def __init__(self, value):
        self.l_child = None
        self.r_child = None
        self.data = value

    def __str__(self):
        return '(' + str(self.l_child) + ':L ' + "V:" + str(self.data) + " R:" + str(self.r_child) + ')'

class Tree:
    def __init__(self):
        self.root = None


def create_min_tree(arr):
    if len(arr) == 0: return None
    if len(arr) == 1: return Tree_node(arr[0])

    mid = len(arr)//2
    root = Tree_node(arr[mid])
    root.l_child = create_min_tree(arr[:mid])
    root.r_child = create_min_tree(arr[mid+1:])
    return root

array = [1, 2, 3, 4, 5, 6, 7]
min_tree = Tree_node(0)
print(create_min_tree(array))


