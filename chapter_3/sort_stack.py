

class Stack:
    def __init__(self):
        self.array = []


    def push(self, value):
        self.array.append(value)

    def pop(self):
        if not len(self.array): return None
        return self.array.pop()

    def __len__(self):
        return len(self.array)

    def move_from_to(self):
        while len(stack) != 0:
            temp_stack.push(stack.pop())

    def peek(self):
        if self.array == []: return None
        return self.array[-1]


def sort_stack1(stack):
    temp = Stack()
    while len(stack) != 0:
        removed = stack.pop()
        while len(temp) != 0 and temp.peek() > removed:
            stack.push(temp.pop())
        temp.push(removed)
    while len(temp) != 0:
        stack.push(temp.pop())
    return stack.array

stack = Stack()
temp_stack = Stack()

stack.push(3)
stack.push(5)
stack.push(1)
stack.push(2)
stack.push(8)
print(sort_stack1(stack))



