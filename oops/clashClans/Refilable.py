from abc import ABC, abstractmethod
class Refillable():

    @abstractmethod
    def refil(self):
        pass

class TimeBasedRefil(Refillable):
    def refil(self):
        return "Time based refil"

class WeaponBasedRefil(Refillable):
    def refil(self):
        return "Weapon based refil"


if __name__=='__main__':
    print("Objects cant be created for an abstract class")
