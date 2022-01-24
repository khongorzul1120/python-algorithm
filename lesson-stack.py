#List 
stack = [1,2, 3,4]

# pop peek append isEmpty

a = stack.pop() # O(1)

#peek - 
print(stack[-1]) # suuliin elementiig awah -1 gej bijne O(-1)

#append
stack.append(2) # O(1)


class StackWithList:
    def __init__(self):
        self.stack = []
    
    def append(self, value):
        self.stack.append(value)

    def pop(self):
       return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def __str__(self) -> str:
        p = []

        for i in self.stack:
            p.append(str(i))

        return ','.join(p)

s = StackWithList()
s.append(1)
s.append(2)
s.append(34)
s.append(5)
s.append(3)
s.append(3)


