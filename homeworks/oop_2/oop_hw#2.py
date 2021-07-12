# 1.
# class Laptop:
#     def __init__(self, Battery):
#         self.Battery= Battery
#
# class Battery:
#     def __init__(self):
#         pass
#
# battery = Battery()


# 2.
# class Guitar:
#     def __init__(self):
#         GuitarString_1 = GuitarString("E")
#         GuitarString_2 = GuitarString("A")
#         GuitarString_3 = GuitarString("D")
#         GuitarString_4 = GuitarString("G")
#         GuitarString_5 = GuitarString("B")
#         GuitarString_6 = GuitarString("E")
#         self.GuitarString = [GuitarString_1, GuitarString_2, GuitarString_3, GuitarString_4, GuitarString_5, GuitarString_6]
#
# class GuitarString:
#     def __init__(self, note):
#         self.note = note
#
# guitar = Guitar()
# print(guitar.GuitarString)


# 3
# class Clac:
#
#     @staticmethod
#     def add_nams(a, b, c,):
#         d = a + b + c
#         return print(f'a+b+c ={d}')
#
# Clac.add_nams(3, 4, 6)


# 4*.
# class Pasta:
#
#     def init(self, ingredients):
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return f'Pasta({self.ingredients})'
#
#     @classmethod
#     def carbonara(cls):
#         return cls(['forcemeat', 'tomatoes'])
#
#
#     @classmethod
#     def bolognaise (cls):
#         return cls(['bacon', 'parmesan', 'eggs'])
#
#
# print(Pasta.carbonara)
# print(Pasta.bolognaise)


# 5*.
# class Concert:
#
#     def __init__(self, max_visitors_num, visitors_count):
#         self.max_visitors_num = max_visitors_num
#         self.visitors_count = visitors_count
#
#     def count_count(self):
#         if self.visitors_count > self.max_visitors_num:
#             self.visitors_count = self.max_visitors_num
#         return f'{self.visitors_count} people'
#
# concert = Concert(100, 1000)
# print(concert.count_count())  # 50


# 6.
# import dataclasses
#
# @dataclasses.dataclass
# class AddressBookDataClass:
#         key: str
#         name: str
#         phone_number: str
#         address: str
#         email: str
#         birthday: str
#         age: int
#
# addressBookDataClass = AddressBookDataClass("KD342k23kK", "Nick", "+1 646-740-0505",
#                                             "207 Park Ave, Gillespie, IL 62033,USA",
#                                             "Nick_Johan@gmail.com","05.12", 25 )
# print(addressBookDataClass)


# 7. Create the same class (6) but using NamedTuple
# from collections import namedtuple
#
# AddressBookDataClass = namedtuple('AddressBookDataClass', ["key", "name", "phone_number", "address", "email", "birthday", "age"])
#
# author_1 = AddressBookDataClass("KD342k23kK", "Nick", "+1 646-740-0505",
#                                 "207 Park Ave, Gillespie, IL 62033,USA",
#                                 "Nick_Johan@gmail.com","05.12", 25 )
#
# print(author_1[0])
# print(author_1.name)


# 8.
# class AddressBook:
#     def __init__(self, key, name, phone_number, address, email, birthday, age):
#         self.key = key
#         self.name = name
#         self.phone_number = phone_number
#         self.address = address
#         self.email = email
#         self.birthday = birthday
#         self.age = age
#
#     def __str__(self):
#         return f'AddressBookDatsClass(key={self.key}, name={self.name}, phone_number={self.phone_number}, address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age}'
#
#     def __repr__(self):
#         return f'AddressBookDatsClass(key={self.key}, name={self.name}, phone_number={self.phone_number}, address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age}'
#
# addressbook = AddressBook("KD342k23kK", "Nick", "+1 646-740-0505", "207 Park Ave, Gillespie, IL 62033,USA", "Nick_Johan@gmail.com","05.12", 25 )
# print(addressbook)
# print(addressbook.__str__())
# print(str(addressbook))
# print(addressbook.__repr__())


# 9.
# class Person:
#
#     def __init__(self, name, age, country):
#         self.name = name
#         self.age = age
#         self.country = country
#
# John = Person("John", 36, "USA")
# setattr(John, "age", 25)
# print(f'Name: ', getattr(John, 'name'), '\nAge:', getattr(John, 'age'), '\nCountry:', getattr(John, 'country'))


# 10.
# class Student:
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#
# student = Student(0, 'Mike')
# setattr(student, 'student_email', 'N*******T@****.com')
# print(f'Student id: ', getattr(student, 'id'), '\nName:', getattr(student, 'name'), '\nEmail:', getattr(student, 'student_email'))


# 11*.
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature
#
#     @property
#     def transfer(self):
#         Fahrenheit = (self.temperature * 1.8) + 32
#         return f'{Fahrenheit} Fahrenheit'
#
# celsius = Celsius(13)
# print(celsius.transfer)
