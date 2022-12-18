# class Laptop:
#     def __init__(self,name,processor) -> #Nontes: #its work auto matically
#         self.name=name
#         self.processor=processor

#     def printOutput(self):
#         print("my laptop name is :",self.name,"and the processoris:",self.processor)

# Laptop1=Laptop("asus","i7")
# Laptop2=Laptop("nokia","i5")

# Laptop1.printOutput()
# Laptop2.printOutput()
# class person:
#     def __init__(self,name,roll_no) -> None:
#         self.name=name
#         self.roll_no=roll_no
#     def printOutput(self):
#         print("your name is =",self.name,"and your roll_no=",self.roll_no)

# person1=person("Ankit",'2')
# person2=person("yogesh","1")
# person1.printOutput()
# person2.printOutput()
# class Person:
#     def __init__(self):
#         self.name="king"
#         self.age=18
#     def updateName(self,name,age):
#         self.name=name
#         self.age=age
#     def compareAge(self,other): #template
#         if(self.age==other.age):
#             return True
#         else:
#             return false
# person1=Person()
# person2=Person()
# if person1.compareAge(person2):
#     print("they are of same age")
# else:
#     print("they are of diffrent age")
# person2.updateName("ankit",78)
# print(person1.name,person1.age)
# print(person2.name,person2.age)
# class variable=global,for whole class
#instance variable=relate with class can change
# class car:
#     wheels=4
#     def __init__(self,brand,mil):
#         self.brand=brand
#         self.mil=mil
# car1=car("hyundai",10)
# car2=car("tesla",80)
# car.wheels=3 #class variable
# print(car1.brand,car1.mil,car1.wheels)
# print(car2.brand,car2.mil,car2.wheels)

# class student:
#     def __init__(self,marks1,marks2,marks3):
#         self.science=marks1 #variables=parameters
#         self.maths=marks2
#         self.geo=marks3
#         def averageCalc(self):
#             print((self.science+self.maths+self.geo)/3)
# @staticmethod
# def staticMethodExample():
#     print("")


# student1=student(10,10,10)
# student2=student(90,90,90)
# student3=student(20,20,20)
# student1.averageCalc()
# student2.averageCalc()
# student3.averageCalc()
#   INHERITANCE
# class A:
#     def method1(self):
#         print("this is method 1")
# class B(A):
#     def method2(self):
#         print("print this method 2")
# # class C(B,A):   #multiple in heritance
# #     def mehod3(self):
# #         print("this is method 3")
# objA=A()
# objB=B()
# # objC=C()

# objC.method2()
 

# class A:
#     def __init__(self):
#         print("This is init of method A")

#     def method1(self):
#         print("This is method 1")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("This is init of method B")

#     def method2(self):
#         print("This is method  2")

# class C(B,A):
    
#     def method3(self):
#         print("This is method 3")

# objB = B()


