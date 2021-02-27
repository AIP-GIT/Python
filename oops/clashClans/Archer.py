from Soldier import Soldier
from Refilable import WeaponBasedRefil

# Multi inheritence implementation
class Archer(Soldier,WeaponBasedRefil):
    def attack(self):
        return "Archer attack"

    #overiding of refil method
    #comment out this function to invoke inheritated WeaponBasedRefil
    def refil(self):
        return "Archer refil"


if __name__=='__main__':
    obj1 = Archer()
    print(obj1.gather())
    print(obj1.attack())
    print(obj1.refil())

