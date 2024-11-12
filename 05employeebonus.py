class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def method(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Salary:",self.salary)    


class manager(Employee):
    def __init__(self, performance,salary):
        self.performance=performance
        self.salary=salary

    def calculation(self):
        if self.performance=="low":
            return self.salary*1.10
        elif self.performance=="medium":
            return self.salary*1.15
        else:
            self.performance=="high"
            return self.salary*1.20
        

class developer(Employee):
    def __init__(self, performance,salary):
        self.performance=performance
        self.salry=salary

    def calculation(self):
        if self.performance=="low":
            return self.salary*1.08
        elif self.performance=="medium":
            return self.salary*1.13
        else:
            self.performance=="high"
            return self.salary*1.18
        

name=input("Enter your name: ")
id=input("id: ")     
salary=int(input("salary: "))
Designation=input("Enter Designation: ")

emp=Employee(name,id,salary)
emp.method()

performance=input("Rate performance: ")
if Designation=="manager":
    man=manager(performance,salary)
    print(f" Salary with Bonus: {man.calculation()}")
else:
    dev=developer(performance,salary)
    print(f" Salary with Bonus: {dev.calculation()}")    
