# # from abc import ABCMeta, abstractmethod
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def printarea(self):
#         return 0
#
# class Rectangle(Shape):
#     type = "Rectangle"
#     sides = 4
#     def __init__(self):
#         self.length = 6
#         self.breadth = 7
#
#     def printarea(self):
#         return self.length * self.breadth
#
# rect1 = Rectangle()
# print(rect1.printarea())
#
# class Employee:
#     __pr = 10 # private variable
#     def __init__(self,name,salary,age):
#         self.name = name
#         self.salary = salary
#         self.age = age
#
#     @classmethod
#     def from_dash(cls,str):
#         return cls(*str.split("-"))
#
#     def __add__(self, other): # dunder methods
#         return int(self.salary) + int(other.salary)
#
#
# rohan = Employee.from_dash("Rohan-255-30")
# print(rohan.salary)
# tanay = Employee.from_dash("Rohan-55-50")
# print(rohan+tanay) # object overloading
# print(rohan._Employee__pr) # name mangling
# print(dir(tanay)) # object introspection

# super
# class Electronic():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# class Phone(Electronic): #Single inheritance
#     def __init__(self,name,age,size):
#         super().__init__(name,age) # super
#         self.size = 10
#
#
# mi = Phone("mi",21,212)
# print(mi.name)
# print(mi.age)
# print(mi.size)