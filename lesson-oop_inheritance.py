#Inheritance - gedeg ni neg negeesee udamshih gsen ug. Parent classiinhaa function-iig ashiglah bolomjtoi.

class TegshUntsugt:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def talbai(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a * self.b) * 2


class Kvadrat(TegshUntsugt):
    def __init__(self, a):
        super().__init__(a, a)

    def perimeter(self):
        return "Zul"
  
w = TegshUntsugt(3,4)
print(w.perimeter())
k = Kvadrat(3)
print(k.perimeter())
print(k.talbai())