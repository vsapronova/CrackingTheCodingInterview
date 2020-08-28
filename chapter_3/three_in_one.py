

class Stack:
    def __init__(self):
        self.capacity = 3
        self.array = [0] * self.capacity
        self.top = 0

class MultiStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [0] * 3 * self.capacity
        self.top = [0, 0, 0]

    def push(self, value, stack_number):
        if stack_number < 3 and stack_number >= 0:
            self.array[stack_number * self.capacity + self.top[stack_number]] = value
            self.top[stack_number] += 1
        if self.top[stack_number] >= self.capacity:
            self.top[stack_number] = self.capacity - 1
        return self.array

    def pop(self, stack_number):
        if stack_number < 3 and stack_number >= 0:
            removed = self.array[self.top[stack_number]]
            self.array[self.top[stack_number]] = None
            self.top[stack_number] -= 1
            return removed


stack = MultiStacks(3)
print(stack.push(44, 0))
print(stack.push(45, 1))
print(stack.push(47, 2))
print(stack.push(48, 2))
print(stack.push(49, 2))
print(stack.pop(2))

