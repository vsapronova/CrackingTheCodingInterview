

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = Node()

    def rem_duplicates(self):
        prev_node = None
        cur = self.head
        while cur.next != None:
            prev_node = cur
            cur = cur.next
            if cur.data == cur.next.data:
                prev_node = cur.next
                cur = cur.next.next


    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

head = (Node(1, Node(2, Node(2, Node(3, Node(4, None))))))
linked = Linked_list()
linked.rem_duplicates()
linked.display()