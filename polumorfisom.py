# def add(a,b,c=0):
#     return a+b+c
# print(add(1,2,3))
# print(add(1,2,3))
# class rect:
#     def calculateArea(self,length=None,breadth=None):
#         if length !=None and breadth !=None:
#          return length*breadth
#     def calculateArea(self,length):
#         return length * length
# rectangle = Rect(2,3)
# class birds:
#     def category(self):
#         print("this is a bird")
#     def fly(self):
#         print("i can fly")
# class sparrow(birds):
#     def size(self):
#         print("i am small in size")
# class crow(birds):
#     pass
# class ostrich(birds):
#     def fly(self):
#         print("i cant fly")
# objbirds=birds()
# objsparrow=sparrow()
# objcrow=crow()
# objostrich=ostrich()

# objbirds.category()
# objbirds.fly()
# objsparrow.category()
# objsparrow.fly()
# objcrow.category()
# objcrow.fly()
# objostrich.category()
# objostrich.fly()
  
# class vechile:
#     def seats(self):
#         print("there are four seats")

# class cars(vechile):
#     def brand(self):
#         print("ferrari")
# class Bus(vechile):
#     def brand(self):
#         print("thar")
#     def seats(self):
#         print("there are 4 seats")

# objvechile=vechile()
# objcars=cars()
# objBus=Bus()

# objvechile.seats()

# objcars.seats()
# objcars.brand()
# objBus.seats()
# objBus.brand()
class person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
person1=person("ankit",19)
print(person1._person__name)


