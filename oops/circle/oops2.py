class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.set_r(r)

    def get_r(self):
        # validate the user
        return  self.__r

    def set_r(self,r):
        # validate the user
        self.__r = r

    def area(self):
        return 3.142*self.r*self.r

    def perimeter(self):
        return 2*3.142*self.r

if __name__=='__main__':
    print("Execution started..")
    c1 = Circle(2,3,1)
    print(c1.get_r())
    c1.set_r(5)
    print(c1.get_r())
