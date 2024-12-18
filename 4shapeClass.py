class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        if length<=0 or width<=0:
            raise ValueError("Length and Width must be non-zero positive values")
    
        self.length=length
        self.width=width

    def area(self):
        print(f"Area is {self.length*self.width}")
    
    def is_square(self):
        if(self.length==self.width):
            print("The Rectangle is a SQUARE")
        else:
            print("The Rectangle is NOT a Square")    
    

def test_rectangle(length,width):
    try:
        R=Rectangle(length,width)
        R.area()
        R.is_square()
    except ValueError as e:
        print(f"Error:{e}")    

test_rectangle(0,5)    
test_rectangle(5,7)    
test_rectangle(5,5)    
test_rectangle(4,0)    

    





 
        
