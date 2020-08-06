class Student: # Class
    def __init__(self,name,age): # Constructor
        self.name = name #Instance variables
        self.age = age

def printdetails(self):
    return f"The name of the student is {self.name} and his age is {self.age}"


Tanay = Student("Tanay",65) # Object
Ayushman = Student("Ayushman",80)
print(printdetails(Ayushman))