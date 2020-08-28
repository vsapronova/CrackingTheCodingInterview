

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def delete_mid_node(head):
    current = head
    length  = 0
    while current != None:
        current = current.next
        length += 1
    if length <= 2: return None
    middle = length//2
    current = head
    for i in range(middle - 1):
        current = current.next
    deleted = current.next
    current.next = current.next.next
    return deleted


def delete_mid_node2(head):
    fast = head
    slow = head
    prev = None
    while fast != None and fast.next != None:
        prev = slow
        slow = slow.next
        fast = fast.next.next # None
    prev.next = slow.next
    return slow



def display(head):
    elems = []
    cur = head
    while cur != None:
        elems.append(cur.data)
        cur = cur.next
    print(elems)

head = (Node(1, Node(5, Node(2, Node(3, Node(4))))))
head1 = (Node(10, Node(1, Node(5, Node(2, Node(3, Node(4)))))))
# display(head)
# print(delete_mid_node(head).data)
display(head)
print(delete_mid_node(head).data)
display(head)

display(head1)
print(delete_mid_node(head1).data)
display(head1)