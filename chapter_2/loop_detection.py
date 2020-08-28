

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def loop_detect(head):
    if head == None: return False
    slow = head
    fast  = head.next
    while slow != fast:
        if fast == None or fast.next == None: return False
        slow = slow.next
        fast = fast.next.next
    return True


b = (Node("A", Node("B", Node("C", Node("H", Node("V", Node("A")))))))


node1 = Node(600)
node2 = Node(700,Node(800,Node(900,node1)))
node1.next = node2
head2 = Node(500,node1)
print(loop_detect(head2))