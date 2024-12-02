class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name: {self.name} age:  {self.age}")    

class teacher(Person):
    def __init__(self,subject):
        self.subject=subject

    def display(self,name,age):
        persn=Person(name,age)
        persn.display()
        print("Subject:", self.subject)

class student(Person):
    def __init__(self,student_id):
        self.student_id=student_id

    def display(self,name,age):
        persn=Person(name,age)
        persn.display()
        print("student id: ",self.student_id)

name=input("enter your name: ") 
age=input("enter age: ")
a=input("teacher: 1  |  student: 2 :")  
if a=="1":
    sub=input("enter subject: ") 
    t=teacher(sub)
    t.display(name,age)
else:
    sid=input("enter id: ") 
    s=student(sid)
    s.display(name,age)



