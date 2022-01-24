from collections import deque


class Queue:
    def __init__(self) -> None:
        self.q = []

    #0(1) - 
    def enqueue(self, value):
        self.q.append(value)

    #O(N)
    def dequeue(self):
        return self.q.pop(0)

    def __str__(self) -> str:
        p = []

        for i in self.q:
            p.append(str(i))

        return '<---'.join(p)

d = Queue()
d.enqueue(2)
d.enqueue(1)
d.enqueue(3)
d.enqueue(5)
d.enqueue(6)
d.dequeue()

print(str(d))
