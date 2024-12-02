class FileManage:
   
    def read(self):
        try:
            x=open("description.txt","rt")
        except FileNotFoundError as e:
            print("Error: ",e)
        else:
            print(x.read()) 
        finally:
            print("done")

    def write(self,a):
        try:
            x=open("description.txt","w")
        except FileNotFoundError as e:
            print("Error: ",e)
        else:
            x.write(a)
        finally:
            print("done")        

    def append(self,a):
        try:
            x=open("description.txt","a")
        except FileNotFoundError as e:
            print("Error: ",e)
        else:
            x.write(a)
        finally:
            print("done")        
           

file=FileManage()
file.read()  

op=input("enter your operartion: Read-1 | Write-2 | Append-3 :")

if op=="1":
    file.read()
elif op=="2":
    a=input("Enter content to write: ")
    file.write(a)
else:
    a=input("enter content to append: ")  
    file.append(a)      






           
