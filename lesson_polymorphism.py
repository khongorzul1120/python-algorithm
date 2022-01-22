# Polymorphism - Olon turliin baij chadna --  classiinhaa turliig uuruu hurwuuleh
# Olon class - function --uud neg turultei bh 
# jishee ni 2.3 + 2 neg turul hurwuulelt hiij bn gsen ug

class TegshUntsugt:
    def turul(self):
        print("Ene bol tegsh untsugt yuoom")

    def talbai(self):
        print("Talbaig olohdoo -> a * b")

class Kvadrad:
    def turul(self):
        print("Ene bol kvadrat youm")

    def talbai(self):
        print("Talbaig olohdoo => a * a ") 

def durs_print(durs):
    durs.talbai()
    durs.turul()

a = TegshUntsugt()
b = Kvadrad()
# print(durs_print(a))
# print(durs_print(b))

for i in (a, b):
    i.talbai()
    i.turul()

