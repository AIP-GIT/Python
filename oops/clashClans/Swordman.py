from Soldier import Soldier
class Swordman(Soldier):
    def attack(self):
        return "Swordman attack"


if __name__=='__main__':
    obj1 = Swordman()
    print(obj1.gather())
    print(obj1.attack())
