# #
# # class Vehicle:
# #     def __init__(self, max_speed, mileage):
# #         self.max_speed = max_speed
# #         self.mileage = mileage
# #
# # class Bus(Vehicle):
# #     def __init__(self, seating_capacity, max_speed, mileage):
# #         super().__init__(max_speed, mileage)
# #         self.seating_capacity = seating_capacity
# #
# class School:
#     def __init__(self, get_school_id, number_of_students):
#         self.get_school_id = get_school_id
#         self.number_of_students = number_of_students
# #
# class SchoolBus(School, Bus):
#     def __init__(self, name, surname, age, animal_type):
#         School.__init__(self, get_school_id, number_of_students)
#         Bus.__init__(self, seating_capacity, max_speed, mileage)
#
# # class Bear:
# #
# #     def make_sound(self, sound=''):
# #         print(sound)
# #         print("Grew")
# #
# # class Wolf:
# #
# #      def make_sound(self, sound=''):
# #         print(sound)
# #         print("Yyyyy")
# #
# # bear = Bear
# # wolf = Wolf
# #
# # for animal in (bear, wolf):
# #     animal.make_sound('S')
#
# # school_bus = Bus(30, 80, 9053)
# # print("Checking type of an object (class Bus)", type(school_bus))
# # print("Checking type of an class Bus", type(Bus))
# # print(isinstance(Bus, type))
# #
# check = isinstance(school_bus, Bus)
# print("School_bus belongs to", check)
#
#
#
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

class City:

    def __int__(self, name, population):
        self.name = name
        self.population = population


    def __new__(cls, name, population):
            x = super(City, cls).new(cls)

            if population < 1500:
                return print('Your city is too small')
            else:
                return x
