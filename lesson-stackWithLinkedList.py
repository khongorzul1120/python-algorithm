class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node('tolgoi')
        self.hemjee = 0

    def getSize(self):
        return self.hemjee

    def isEmpty(self):
        return self.hemjee == 0

    def peek(self):
        if self.isEmpty():
            raise Exception('Stack hooson bn')

        return self.head.next.value

    def append(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.hemjee += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack hooson bn')
        value = self.head.next.value
        self.head.next = self.head.next.next

        self.hemjee -= 1
        return value
    
    def __str__(self) -> str:
        odoo = self.head
        p = []
        while odoo:
            p.append(str(odoo.value))
            odoo = odoo.next
        return '->'.join(p)

s = Stack()

s.append(1)
s.append(2)
s.append(4)
s.append(3)
s.append(5)

print(s.pop())



print(s)