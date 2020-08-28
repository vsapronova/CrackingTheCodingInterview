


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def nth_to_last(self, n):
    current = head
    follower = head
    for i in range(n):
        if current == None: return None
        current = current.next
    while current != None:
        current = current.next
        follower = follower.next
    return follower


head = (Node(1, Node(5, Node(2, Node(3, Node(4))))))


print(nth_to_last(head, 1).data)
