

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def sum_lists(list1, list2):
    current1 = list1
    current2 = list2
    new_list = None
    new_list_tail = None
    add_number = 0
    while current1 != None:

        sum_nodes = current1.data + current2.data
        if add_number == 1:
            sum_nodes = sum_nodes + 1
            add_number = 0
        if sum_nodes >= 10:
            sum_nodes = sum_nodes - 10
            add_number = 1

        new_node_number = Node(sum_nodes)
        if new_list == None:
            new_list = new_node_number
            new_list.next = None
        else:
            if new_list_tail == None:
                new_list_tail = new_node_number
                new_list.next = new_list_tail
            else:
                new_list_tail.next = new_node_number
                new_list_tail = new_node_number

        current1 = current1.next
        current2 = current2.next
        if current2 == None and current1 != None:
            if add_number == 1:
                new_node = Node(current1.data + 1)
                new_list_tail.next = new_node
                current1 = current1.next
                add_number = 0
    while current2 != None:
        if add_number == 1:
            new_node = Node(current2.data + 1)
            new_list_tail.next = new_node
            current2 = current2.next
            add_number = 0
    return new_list


def sum_lists2(list1, list2):
    current1 = list1
    current2 = list2
    new_list = None
    new_list_tail = None
    add_number = 0

    while current1 != None or current2 != None:
        sum_value = 0
        if current1 is not None:
            sum_value += current1.data
        if current2 is not None:
            sum_value += current2.data
        if add_number == 1:
            sum_value = sum_value + 1
            add_number = 0
        if sum_value >= 10:
            add_number = 1

        sum_node = Node(sum_value % 10)
        if new_list == None:
            new_list = sum_node
            new_list.next = None
        else:
            if new_list_tail == None:
                new_list_tail = sum_node
                new_list.next = new_list_tail
            else:
                new_list_tail.next = sum_node
                new_list_tail = sum_node

        if current1 is not None:
            current1 = current1.next
        if current2 is not None:
            current2 = current2.next


    if add_number == 1:
        sum_node = Node(1)
        new_list_tail.next = sum_node

    return new_list


def sum_lists3(current1, current2, overflow = False):
    if current1 is None and current2 is None:
        if overflow:
            return Node(1)
        else:
            return None

    sum_value = 0
    if current1 is not None:
        sum_value += current1.data
    if current2 is not None:
        sum_value += current2.data
    if overflow:
        sum_value = sum_value + 1

    new_node = Node(sum_value % 10)

    next1 = None
    if current1 is not None:
        next1 = current1.next
    next2 = None
    if current2 is not None:
        next2 = current2.next

    next_node = sum_lists3(next1, next2, sum_value >= 10)

    new_node.next = next_node

    return new_node


def display(head):
    elems = []
    cur = head
    while cur != None:
        elems.append(cur.data)
        cur = cur.next
    print(elems)


a = (Node(9, Node(7, Node(5))))
b = (Node(2, Node(3, Node(4, Node(9)))))

result = sum_lists3(a, b)
display(result)