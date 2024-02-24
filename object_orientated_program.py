from employee import Employee
from person import Person
import platform

x = dir(platform)
print(x)
# Calling a class creates a new instance object
# Calling a class will call code to construct or instantiate an object
# class is not a type
# hasattr(object, __name=)
# messages are sent to objects requesting actions
# duck typing
# if hasattr(x, '__str__'):
#     val = str(x)

# two methods - __new__ and __init__
# new = called when an object is created and first parameter is class name
# init called when an object is initialised and first parameter is object
# implicit return of the current object

# special methods
#
# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self._day = day
#         self._month = month
#         self._year = year
#
#     def __str__(self):
#         return "%02d/%02d/%d" % (
#             self._day, self._month, self._year)
#
#     def __add__(self, value):
#         retn = Date(self._day, self._month, self._year)
#         retn._day = retn._day + value
#         # retn._validate_date()
#         return retn
#
#     def mget(self):
#         return self._day
#
#     def mset(self,day):
#         self._day = day
#
#     # mday = property(mget,mset)
#
#     # @sign indicates a decorator - built in function
#     # def mget(self):
#     #       return self._day
#     # mday = property(mget,mset)
#     @property
#     def mday(self):
#         return self._day
#
#     @mday.setter
#     def mday(self, day):
#         self._day = day
#
#
# today = Date(9, 10, 2015)
# print(today)
# tomorrow = today + 1
# print(tomorrow)
#
#
#
# # class methods
#
# _count = 0
#
# @classmethod
# def get_count(cls):
#     return Date._count

# inheritance - 335
# the relationship between two classes
# derived class inherits all of the attributes and operations of the base class
# polymorphism
# class DerivedClassName(base_classes):
#         def __init__(self, arguments):
#                 base_class.__init__(self,arguments)
# other methods

me = Employee("Fred Bloggs", 'M', 'IT')
print(me)

if isinstance(me, Employee):
    print(me, "is a Employee!")

if isinstance(me, Person):
    print(me, "is a Person!")

if issubclass(Employee, Person):
    print("Employee is a subclass of Person")


    class Vehicle:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def move(self):
            print("Move!")

    # car class is empty so it inherits the brand model and move from vehicle
    class Car(Vehicle):
        pass


    class Boat(Vehicle):
        def move(self):
            print("Sail!")

    # boat and plane inherit from vehicle but overwrite the move method
    class Plane(Vehicle):
        def move(self):
            print("Fly!")


    car1 = Car("Ford", "Mustang")  # Create a Car object
    boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
    plane1 = Plane("Boeing", "747")  # Create a Plane object

    for x in (car1, boat1, plane1):
        print(x.brand)
        print(x.model)
        x.move()
