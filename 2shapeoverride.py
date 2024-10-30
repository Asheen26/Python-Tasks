class Shape:
    def area(self):
        print("Calculating area...")

class circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*(self.radius**2)

class rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

s=Shape()
c=circle(6)
s.area()
print(c.area())
r=rectangle(5,3)
print(r.area())


        