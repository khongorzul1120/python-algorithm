#OOP - Encapsulation - gedeg ni neg class baina, Ter class -n gadnaas handah function bolon huvisagchiig private bolon public bolgohiig helne.


class Toirog:
    # huvisagchaa private bolgosnoor gadnaas handaj chadhgui bolon harah bolomjgui yum.Private huvisagchiig harah bolvol get, set function ashiglana.
    __pi = 3.14 # private

    def __init__(self, radius):
        # instance atribute
        self.radius = radius

    def get_pi(self):
        return self.__pi

    def set_pi(self, pi):
        self.__pi = pi

        
    def talbai(self):
        return self.radius * self.__pi * self.radius

    def perimeter(self):
        return self.__diameter() * self.__pi

    # private function bolgosnoor gadnaas handah bolomjgui.
    def __diameter(self):
        return 2 * self.radius

# Instance gedeg ni a gedeg huvisagchiig helj baigan 
a = Toirog(3)

print(a.talbai())
print(a.perimeter())
