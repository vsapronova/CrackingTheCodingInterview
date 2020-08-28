

class Node:
    def __init__(self, head, number):
        self.head = head
        self.number = number
        self.next = None


# class Animal_Shelter:
#     def __init__(self):
#         self.dog = []
#         self.cat = []


    def enqueue(self, animal):
        cur = self.head
        self.number = 0
        animal = Node(animal, self.number)
        self.number += 1
        while cur.next != None:
            cur = cur.next
        cur.next = animal

    def dequeue_any(self):
        cur = self.head
        prev = None
        while cur.next != None:
            prev = cur
            cur = cur.next
        removed = cur
        prev.next = cur.next
        return removed


    def dequeue_dog(self):
        cur = self.head
        removed = cur.next
        cur = cur.next.next
        return removed



    def dequeue_cat(self, head):
        pass



dogs_list = Queue()
cats_list = Queue()