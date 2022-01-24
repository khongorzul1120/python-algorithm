# List gedeg ni a = [5] 5 hemjeetei list uusgewel ug. List urt uuruu ugnu
# List deer dahin utga nemehed hemjee duurwel dahin shine pointer uusgeed ter ni array-iin urtnaas 2 dahin ih hemjeetei list uusdeg buguud list shine pointer luu zaana umnud list ee copy-ood garbage collection ni ustdag

class DynamicArray:
    def __init__(self):
        self.arr = [0] * 5 
        self.bagtaamj = 5
        self.odoo = 0
    
    def nemeh(self, shineToo):
        if self.odoo == self.bagtaamj:
            turZuur = [0] * (self.bagtaamj * 2)

            for i in range(self.odoo):
                turZuur[i] = self.arr[i]
            
            self.bagtaamj *= 2
            self.arr = turZuur

        self.arr[self.odoo] = shineToo
        self.odoo += 1

    def print(self):
        too = 0 
        while too < self.odoo:
            print(self.arr[too])
            too += 1
    def get(self,index):
        return self.arr[index]


a = DynamicArray()

a.nemeh(1)
a.nemeh(2)
a.nemeh(3)
a.nemeh(2)
a.nemeh(3)
a.nemeh(2)
a.nemeh(3)
a.nemeh(2)
a.nemeh(3)
# a.print()
print(a.get(4))
    