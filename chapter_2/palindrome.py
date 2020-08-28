
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def palindrome1(head):
    current = head
    new_current = None
    while current != None:
        new_node = Node(current.data)
        new_node.next = new_current
        new_current = new_node
        current = current.next
    current = head
    while current != None:
        if current.data != new_current.data:
            return False
        current = current.next
        new_current = new_current.next
    return True



b = (Node("A", Node("B", Node("B", Node("A", Node("V"))))))
print(palindrome1(b))
