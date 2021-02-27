from Soldier import Soldier
from Refilable import TimeBasedRefil

# Single inheritence implementation
class Archer(Soldier):
    def attack(self):
        return "Archer attack"
    
    # Invoking refil method of Refillable class
    def refil(self):
        return TimeBasedRefil().refil()

if __name__=='__main__':
    obj1 = Archer()
    print(obj1.gather())
    print(obj1.attack())
    print(obj1.refil())