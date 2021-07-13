# 1. Create a Vehicle class with max_speed and mileage instance attributes

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     def __init__(self, seating_capacity, max_speed, mileage):
#         super().__init__(max_speed, mileage)
#         self.seating_capacity = seating_capacity


# 3. Determine which class a given Bus object belongs to (Check type of an object)

# school_bus = Bus(30, 80, 9053)
# print("Checking type of an object (class Bus)", type(school_bus))
# print("Checking type of an class Bus", type(Bus))


# 4. Determine if School_bus is also an instance of the Vehicle class

# check = isinstance(school_bus, Bus)
# print("School_bus belongs to", check)


# 5. Create a new class School with get_school_id and number_of_students instance attributes

# class School:
#     def __init__(self, get_school_id, number_of_students):
#         self.get_school_id = get_school_id
#         self.number_of_students = number_of_students
#
#
# # 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color
#
# class SchoolBus(School, Bus):
#     def __init__(self, get_school_id, number_of_students, seating_capacity, max_speed, mileage, bus_school_color):
#         School.__init__(self, get_school_id, number_of_students)
#         Bus.__init__(self, seating_capacity, max_speed, mileage)
#         self.bus_school_color = bus_school_color

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

# class Bear:
#
#     def make_sound(self, sound=''):
#         print(sound)
#         print('Grow')
#
#
# class Wolf:
#
#     def make_sound(self, sound=''):
#         print(sound)
#         print('yyyyyyyyyyy')
#
#
# bear = Bear()
# wolf = Wolf()
#
# for animal in (bear, wolf):
#     animal.make_sound()


# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".

# class City:
#
#     def __int__(self, name, population):
#         self.name = name
#         self.population = population
#
#
#     def __new__(cls, name, population):
#             x = super(City, cls).new(cls)
#
#             if population < 1500:
#                 return print('Your city is too small')
#             else:
#                 return x


# 9. Override a printable string representation of the City class and return: The population of the city {name} is {population}
# class City:
#
#     def __str__(self):
#         return f'The population of the city {self.name} is {self.population}'
#
#
# city_1 = City('Lviv', 3000000)
# print(city_1)
#
# city_2 = City('Fastiv', 41000)
# print(city_2)


# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.

# class Add:
#     def __init__(self, a):
#         self.a = a
#
#     def __add__(self, other):
#        if self.a > 10:
#             return self.a * other.a
#        else:
#             return self.a + other.a
#
# a1 = Add(11)
# a2 = Add(7)
# print(a1 + a2)


# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class Sum:
    def __call__(self, a, b):
        d = a + b
        return d


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False

# class MyOrder:
#     def __init__(self, cart, customer):
#         self.cart = cart
#         self.customer = customer
#
#     def __bool__(self):
#         return len(self.cart) > 0
#
# order_1 = My0rder(['a', 'b', 'c'], 'd')
# order_2 = My0rder([], 'a')
#
# print(bool(order_1))
# print(bool(order_2))
