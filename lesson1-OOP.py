# Object oriented programming
class Mashin:
    # Class attribute
    dugui = 4

    # class-iin init function ene zaawal self defaultaar awna. Init function gedeg ni Mashin gesen Object duudagdah uyd hamt duudagddag function yum.
    def __init__(self, make, brand, price = 10000, year=2010):
        self.make = make
        self.brand = brand
        self.price = price
        self.year = year
    
    def odoonii_une(self):
        return max(400, self.price - (2021 - self.year) * 500)

    def __eq__(self, nuguuMashin) -> bool:
        return self.make == nuguuMashin.make and self.brand == nuguuMashin.brand
    # str function override hiij bn, Herew bijihgui default str function duudagna. f ni format gesen ug 
    def __str__(self):
        return f'Minii mashin: {self.make} {self.brand} {self.year}'

    def __add__(self, nuguuMashin):
        return self.price + nuguuMashin.price

    def __sub__(self, nuguuMashin):
        return self.price - nuguuMashin.price

    #Ene self keyboard gui bsn ch gesn ajillna. staticmethod tuslamjtaigaar self -guigeer ajillah bolomjtoi function gesen ug
    @staticmethod #Decorator
    def huuchin_ugui_yu(year):
        return 2021 - year > 20

    @classmethod
    def mashin_gehdee_nasaar_ni(cls, brand, make, price=1000, year=2021):
        return cls(brand, make, price ,2021 - year)

a = Mashin("Benz","G class", 5000)
b = Mashin("Benz","G class")
c = Mashin.mashin_gehdee_nasaar_ni("Benz","G class", 5000,3)

print(a == b) #False yagad gewel memory location uur uchraas. Python hamgiin ehleed memory location -g haritsuuldag
print(a+b)
print(a.odoonii_une())
print(a.huuchin_ugui_yu(2000))
#staticMethod -g ingej ashiglaj bolno
print(Mashin.huuchin_ugui_yu(22))
print(c)
