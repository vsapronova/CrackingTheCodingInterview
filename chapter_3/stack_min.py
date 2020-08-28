

class Stack:
    def __init__(self):
        self.array = []

    def push(self, value, top):
        cur_min = self.get_min()
        if cur_min == None or cur_min > value:
            cur_min = value
        self.array.append((value, cur_min))
        top += 1
        return self.array

    def pop(self, top):
        return self.array[top]

    def get_min(self):
        if not self.array:
            return None
        return self.array[-1][1]


stack = Stack()
stack.push(1, 0)
stack.push(5, 1)
print(stack.push(-1, 2))
print(stack.get_min())