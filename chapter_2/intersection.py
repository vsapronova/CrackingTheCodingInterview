

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def intersection (head1, head2):
    # Method 1
    nodes = {}
    node = head1
    while node != None:
        nodes[node] = True
        node = node.next
    node = head2
    while node != None:
        if node in nodes:
            return node.data
        node = node.next
    return None

def intersection2(head1, head2):
    # Method 2
    if head1 == None or head1 == None: return None
    size1 = find_size(head1)
    size2 = find_size(head2)
    tail1 = find_tail(head1)
    tail2 = find_tail(head2)
    if tail1 != tail2: return None
    if size1 > size2:
        shorter, longer = head2, head1
    else:
        shorter, longer = head1, head2
    n = abs(size1 - size2)
    longer = getnthnode(longer, n)
    while longer != shorter:
        shorter = shorter.next
        longer = longer.next
    return longer.data


def getnthnode(head, n):
    current = head
    while n > 0 and current != None:
        current = current.next
        n -= 1
    return current


def find_size(head):
    if head == None: return None
    current = head
    size = 1
    while current.next != None:
        size += 1
        current = current.next
    return size


def find_tail(head):
    if head == None: return None
    current = head
    while current.next != None:
        current = current.next
    current_tail = current
    return current_tail


node = Node(70,Node(80))
head1 = Node(50,Node(20,node))
head2 = Node(60,Node(90,Node(10,node)))

# print(intersection2(head1, head2))
print(intersection(head1, head2))