a=100
b=0

try:# u r telling this may hv error,u try
    print(a/b)
    
#except exception :# u saying if error the i handleprint
#print("cant divide any number by zero")

except Exception as e:
    print("Please note,number cant be divided  by zero",e)
    
#to check your prg excecution goes till end or not
print("Bye")

a=10
b=0

try:
    print("resource open")
    print(a/b)

except Exception as e:
    print("Dont give second no as zero",e)

finally: #will get excueted if thr is error  or
    print("Resource closed")

a=10
try:
    b=int(input("Enter the number"))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note,number cant be divided by zero")
except ValueError as e:
    print("Invalid input",e)
except Exception as e:#if not any above errors
    print("other error",e)
finally:
    print("Resource closed")

class computer:     #class definition
   def config(self): #config is a function
       print("YES")
 
lenova=computer()  #object1
lenova.config()

dell=computer()    #object2
dell.config()'''

'''class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def display(self):
        print("ID: %d  \nName : %s

              " % (self.id,self.name))

emp1=Employee("John",101)
emp2=Employee("David",102)

#variables and var access in class and method
class computer():
    a=10
    b=20
    print("class variable inside class",a)

    def config(self):
        c=100
        print("yes")
        print("Instance access",self.b)

lenova=computer()
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()
print("dell",dell.a)



lenova.config()


emp1.display()
emp2.display()



    
