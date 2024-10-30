class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def calculate_pay(self):
        return("Calculating Payment...")  


    def details(self):
        return(self.name,self.id)

class hourly(Employee):
    def __init__(self,hourly_rate,hours_worked):
      
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked

    def calculate_pay(self):
         
        return self.hourly_rate*self.hours_worked
    

class salary(Employee):
    def __init__(self,salary):
        self.salary=salary
    def calculate_pay(self):
        return self.salary   
      
Emp=Employee("vini",7) 
print(Emp.calculate_pay())
print(Emp.details())


S=salary(50000)
t=input("enter type of emplyee hour/salary:\n ")
if t=="hour":
    p=int(input("enter hour worked: "))
    H=hourly(1000,p) 
    print(H.calculate_pay())  


else:
    print(S.calculate_pay())

