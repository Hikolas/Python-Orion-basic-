import math
import random
# from __future__ import annotations
from typing import Dict, Any
import uuid

class Animal:

    def __init__(self):
        pass

    def animal_generator(self, number_of_animal):
        self.number_of_animal = number_of_animal
        animal_list = []
        lst = [Predator, Herbivorous]
        random_animal = random.choice(lst)
        self.animals = [random_animal() for animal in range(0, self.number_of_animal)]
        for animal in self.animals:
            animal_list.append(animal)
        print(animal_list)

    def print_status(self):
        for animal in self.animals:
            print(animal)
        print("____________________________________________________________")

    def hunting(self):
        self.animal1 = random.choice(self.animals)
        self.animal2 = random.choice(self.animals)
        while self.animal1.id != self.animal2.id:
          self.animal2 = random.choice(self.animals)
        if self.animal1.type == "Herbivorous":
            print(self.animal1)
            return self.animal1
        else: print(self.animal1), print(self.animal2),
        return self.animal1, self.animal2

    def __str__(self):
        return f'{self.type} animal, {self.random_speed} speed, {self.random_power} power'

    def eat(self):
        Animal.hunting(self)
        if self.animal1.type == "Predator":
            Predator.eat(self)
            print("____________________________________________________________")
        elif self.animal1.type == "Herbivorous":
            Herbivorous.eat(self)
            print("____________________________________________________________")


class Predator(Animal):

    def __init__(self):
        self.type ="Predator"
        self.id = uuid.uuid4
        self.random_speed = random.randint(50, 100)
        self.random_power = random.randint(50, 100)

    def eat(self):
        max_pawer_a1 = self.animal1.random_power

        hunting_probability = random.randint(1, 10)
        if hunting_probability < 3 and hunting_probability > 0:
            print("Animal did not find food ")
            beark
        elif self.animal1.random_speed < self.animal2.random_speed or self.animal1.random_power < self.animal2.random_power or self.animal2.type == "Predator" :
            self.animal1.random_power = self.animal1.random_power - self.animal1.random_power * 30 / 100
            self.animal2.random_power = self.animal2.random_power - self.animal2.random_power * 30 / 100
        else:
            self.animal1.random_power = self.animal1.random_power + self.animal1.random_power * 50 / 100
            self.animal2 = "-"
        if self.animal1.random_power > max_pawer_a1:
            self.animal1.random_power = max_pawer_a1
        self.animal1.random_power = math.floor(self.animal1.random_power)
        self.animal2.random_power = math.floor(self.animal2.random_power)
        print(self.animal1, self.animal2)
        return self.animal1, self.animal2

    def __str__(self):
        return f'{self.type} animal, {self.random_speed} speed, {self.random_power} power'
    pass

class Herbivorous:

    def __init__(self):
        self.type = "Herbivorous"
        self.id = uuid.uuid4
        self.random_speed = random.randint(25, 100)
        self.random_power = random.randint(25, 100)

    def eat(self):
        max_pawer_a1 = self.animal1.random_power

        hunting_probability = random.randint(1, 10)
        if hunting_probability < 2 and hunting_probability > 0:
            print("Animal did not find food ")
            beark
        elif hunting_probability > 2 and hunting_probability <= 10:
            self.animal1.random_power = self.animal1.random_power + self.animal1.random_power * 50 / 100
        if self.animal1.random_power > max_pawer_a1:
            self.animal1.random_power = max_pawer_a1
        self.animal1.random_power = math.floor(self.animal1.random_power)
        self.animal2.random_power = math.floor(self.animal2.random_power)
        print(self.animal1)
        return self.animal1

    def __str__(self):
        return f' {self.type} animal, {self.random_speed} speed, {self.random_power} power'
    pass

    # def any_predator_left(self):
    #     for animal in self.animals:
    #         if animal_list[0][0] == "Predator":
    #             True
    #     True
    #     Pass


# _____________________________________________________________________________________________________________________

# animal = Animal()
#
# if __name__ == "__main__":
#    animal.animal_generator(5)
#
#    while True:
#        if not animal.any_predator_left():
#            break
#        for animals in animal:
#            animal.eat(animal=animal)
#        time.sleep(1)

# _____________________________________________________________________________________________________________________

animal = Animal()
animal.animal_generator(5)
animal.print_status()
animal.eat()
animal.eat()
animal.print_status()

