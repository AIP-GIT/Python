class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return 3.142*self.r*self.r

    def perimeter(self):
        return 2*3.142*self.r

if __name__=='__main__':
    c1 = Circle(3,2,1)
    c1.r = -2
    print(c1.area())
    print(c1.perimeter())

    c2 = Circle(3,2,2)
    c3 = Circle(1,2,5)

    print(c2.area())
    print(c3.perimeter())