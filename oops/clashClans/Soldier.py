from abc import ABC, abstractmethod
class Soldier(ABC):
    
    def gather(self):
        return "Soldiers gather"

    @abstractmethod
    def attack(self):
        pass


if __name__=='__main__':
    obj1 = Soldier()
    print(obj1.gather())
