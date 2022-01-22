#Abstraction -> gedeg ni abctract class d yu bh ystoin ter funtionuudiig zarlaj ugdug body bhgui bolon abctract class functiond abctractmethod keyboardiing ashiglane. 

from abc import ABC, abstractmethod

class Durs(ABC):
    @abstractmethod
    def talbai(self):
        pass

class Toirog(Durs):
    r = 4
    def talbai(self):
        return 3.14 * self.r**2

class Kvadrat(Durs):
    a = 3
    def talbai(self):
        return self.a * self.a

a = Toirog()
b = Kvadrat()
print(a.talbai())
print(b.talbai())