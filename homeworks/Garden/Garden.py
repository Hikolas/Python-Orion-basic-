# The whole project works, but the function "healing" doesn't work.
from abc import abstractmethod
import random


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits):
      self.vegetables = vegetables
      self.fruits = fruits

    def show_the_garden(self):
      print(f'I have such vegetables {self.vegetables}')
      print(f'I have such fruits {self.fruits}')

class Vegetables:
    def __init__(self,vegetable_type):
      self.vegetable_type = vegetable_type

    states = {"0": "None","1": "Flowering","2": "Green","3": "Red"}

    @abstractmethod
    def growth(self):
      raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
      raise NotImplementedError("You missed me")

class Fruits:
    def __init__(self, fruits_type):
      self.fruits_type = fruits_type
    states = {0: "None",1: "Flowering",2: "Green",3: "Red"}

    @abstractmethod
    def growth(self):
      raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
      raise NotImplementedError("You missed me")

class Tomato(Vegetables):
    def __init__(self, vegetable_type, number_of_tomatoes):
     Vegetables.__init__(self,vegetable_type)
     self.number_of_tomatoes = number_of_tomatoes
     self.states = 0
     self.vegetable_type = vegetable_type

    def growth(self):
      if self.states < 3:
        self.states += 1
      self.print_state()

    def print_state(self):
      print(f"{self.vegetable_type}, {self.number_of_tomatoes} , {self.states}")

    def is_ripe(self):
      return self.states == 3

class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples, present_pests):
      Fruits.__init__(self,fruits_type)
      self.present_pests = present_pests
      self.number_of_apples = number_of_apples
      self.health_aplle = 3
      self.states = 0
      self.fruits_type = fruits_type

    def print_state(self):
      if self.health_aplle > 0:
        print(f"{self.fruits_type}, {self.number_of_apples}, {self.states}")
      else:
        print(f"-")

    def check(self):
        if self.health_aplle == 3 or self.health_aplle > 3:
          print('Not pests')
        else:
          print(f"{self.fruits_type}, {self.number_of_apples}, {self.states}, infection, health_aplle {self.health_aplle}")

    def healing(self):
        if self.health_aplle != 3 or self.health_aplle < 3:
          self.health_aplle += 1


    def growth(self):
      if self.present_pests == 1:
        if self.states < 3:
            self.states += 1
            self.health_aplle -= 1
      else:
        if self.states < 3:
            self.states += 1
      self.print_state()

    def is_ripe(self):
      return self.states == 3



class TomatoBush:
  def __init__(self, number_of_tomatoes):
    self.tomatoes = [Tomato('Cherry', index) for index in range(0, number_of_tomatoes - 1)]

  def infection(self):
      pass

  def healingTree(self):
      pass

  def growth_all(self):
    for tomato in self.tomatoes:
     tomato.growth()

  # def all_are_ripe(self):
  #   lst = []
  #   for tomato in self.tomatoes:
  #     ripe_state = tomato.is_ripe()
  #       lst.append(ripe_state)
  #   return all(lst)

  def all_are_ripe(self):
      return all([tomato.is_ripe() for tomato in self.tomatoes])

  def give_away_all(self):
    self.tomatoes = []

class AppleTree:
    def __init__(self, number_of_apples):
      self.apples = [Apple('White', index, random.randint(0,1)) for index in range(0, number_of_apples - 1)]


    def infection(self,): #"""lst_infection = []"""):
      # lst_infection = []
      for apple in self.apples:
        apple.check()
      # lst_infection.append(apple)
      # print(f' {lst_infection}')

    def healingTree(self):
      for apple in self.apples:
        apple.healing()

    def growth_all(self):
      for apple in self.apples:
        apple.growth()

    def all_are_ripe(self):
      return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
      self.apples = []

class Gardener:
    def __init__(self, name, plants):
      self.name = name
      self.plants = plants

    def check_up_pests(self):
      for plant in self.plants:
        plant.infection()
      print('________________________________')

    def sprinkle(self):
      for plant in self.plants:
        plant.healingTree
      print('________________________________')

    def work(self):
      for plant in self.plants:
        plant.growth_all()
      print('________________________________')

    def harvest(self):
      for plant in self.plants:
        if plant.all_are_ripe():
          plant.give_away_all()
        else:
          print('Too early to harvest')
      print('________________________________')

tomato1 = TomatoBush(4)
apple_tree1 = AppleTree(10)

John = Gardener('John', [tomato1, apple_tree1])

garden1 = Garden(tomato1, apple_tree1)

John.work()
John.check_up_pests()
John.sprinkle()
John.check_up_pests()
John.work()
John.work()
John.work()
John.harvest()

print(tomato1.tomatoes)
print(apple_tree1.apples)
