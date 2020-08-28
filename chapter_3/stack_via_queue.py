

class MyQueue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def add(self, value):
        self.push_stack.push(value)

    def pop_out(self):
        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()

class Stack:
    def __init__(self):
        self.array = []


    def __len__(self):
        return len(self.array)

    def push(self, value):
        self.array.append(value)


    def pop(self):
        if not len(self.array): return "Empty"
        return self.array.pop()

queue = MyQueue()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
print(queue.pop_out())
print(queue.pop_out())
print(queue.pop_out())
print(queue.pop_out())
