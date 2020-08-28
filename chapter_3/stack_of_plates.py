


class SetOfStacks:
    def __init__(self, stack_size):
        self.array = []
        if stack_size < 1:
            raise NameError("Not possible")
        else:
            self.stack_size = stack_size

    def push(self, value):
        if self.array == []:
            self.array.append([value])
        else:
            if len(self.array[-1]) >= self.stack_size:
                self.array.append([value])
            else:
                self.array[-1].append(value)
        return self.array

    def pop(self):
        if self.array == []:
            raise NameError("Empty stack")
        else:
            removed = self.array[-1][-1]
            if len(self.array[-1]) == 1:
                del self.array[-1]
            else:
                del self.array[-1][-1]
        return removed

stacks = SetOfStacks(3)
stacks.push(1)
stacks.push(2)
stacks.push(3)
print(stacks.push(4))
print(stacks.pop())