class Circle:
    def __init__(self,x,y,r):
        print("Inside initializer")
        assert r>0, "Radius can't be zero or negative"
        self.x = x
        self.y = y
        self.r = r

    @property
    def r(self):
        print("Inside getter")
        # validate the user
        return  self.__r
    @r.setter
    def r(self,r):
        # validate the user
        print("inside setter")
        self.__r = r

    def area(self):
        return 3.142*self.r*self.r

    def perimeter(self):
        return 2*3.142*self.r

if __name__=='__main__':
    print("Execution started..")
    c1 = Circle(3,2,-1)
    print(c1.area())
