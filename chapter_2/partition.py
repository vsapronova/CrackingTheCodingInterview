

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def partition(head, key):
    current = head
    prev  = None
    larger_head = None
    while current != None:
        if current.data >= key:
            removed = current
            if current == head:
                head = current.next
                current = current.next
                prev = None
            else:
                if current.next == None:
                    prev.next = None
                    current = None
                else:
                    prev.next = current.next
                    prev = current
                    current = current.next
            removed.next = larger_head
            larger_head = removed
        else:
            prev = current
            current = current.next
    if head == None:
        return larger_head
    else:
        prev.next = larger_head
        return head




def display(head):
    elems = []
    cur = head
    while cur != None:
        elems.append(cur.data)
        cur = cur.next
    print(elems)

# head = (Node(1, Node(5, Node(2, Node(3, Node(4))))))
list1 = (Node(0, Node(1, Node(5, Node(2, Node(3, Node(11)))))))

list1 = partition(list1, 0)
display(list1)