import random
import time
import logging


class OutOfWater (Exception):
    pass

def Water0(amount_of_water):
    if amount_of_water == 0:
        raise OutOfWater

class WaterRunsOut (Exception):
    pass

def Water20(amount_of_water):
    if amount_of_water <= 20:
        raise WaterRunsOut

class IsOverFlowing (Exception):
    pass

def tank_fullness100(tank_fullness):
    if tank_fullness == 100:
        raise IsOverFlowing

class IsAlmostFull(Exception):
    pass

def tank_fullness75(tank_fullness):
    if tank_fullness > 75:
        raise IsAlmostFull

class VacuumСleanerturnedoff(Exception):
    pass

def battery20(battery_charge):
    if battery_charge <= 20:
        raise VacuumСleanerturnedoff

class VacuumСleaner:
    def __init__(self, battery_charge, tank_fullness, amount_of_water):
        self.battery_charge = battery_charge
        self.tank_fullness = tank_fullness
        self.amount_of_water = amount_of_water

    def wash(self):
        water_consumption = random.randint(4, 10)
        charge = random.randint(1, 1)
        if self.amount_of_water > 0:
            self.amount_of_water = self.amount_of_water - water_consumption
            self.battery_charge = self.battery_charge - charge
            if self.amount_of_water <= 0:
                self.amount_of_water = 0
        if self.amount_of_water == 0:
            try:
                Water0(self.amount_of_water)
            except OutOfWater:
                print('Out of water')

        elif self.amount_of_water <= 20:
            try:
                Water20(self.amount_of_water)
            except WaterRunsOut:
                print('The water runs out')
        print(".")


    def vacuum_cleaner(self):
        waste = random.randint(5, 10)
        charge = random.randint(1, 1)
        if self.tank_fullness < 100:
            self.tank_fullness = self.tank_fullness + waste
            self.battery_charge = self.battery_charge - charge
            if self.tank_fullness >= 100:
                self.tank_fullness = 100
        if self.tank_fullness == 100:
            try:
                tank_fullness100(self.battery_charge)
            except IsOverFlowing:
                print('Garbage is overflowing  ')

        elif self.tank_fullness > 75:
            try:
                tank_fullness75(self.battery_charge)
            except IsAlmostFull:
                print('The dump is almost full   ')

        print(".")

    def move(self):
        charge = random.randint(1, 3)
        if self.battery_charge > 0:
            self.battery_charge = self.battery_charge - charge
            if self.battery_charge <= 0:
               self.battery_charge = 0
               raise VacuumСleanerturnedoff
        if self.battery_charge <= 20:
            try:
                battery20(self.battery_charge)
            except VacuumСleanerturnedoff:
                print('The vacuum cleaner ALMOS turned off ')
        print(".")

    def function_check(self):
        pass


Vacuumсleaner = VacuumСleaner(100, 0, 100)
on = 0
while on == 0:
  time.sleep(1)
  Vacuumсleaner.move()
  time.sleep(2)
  Vacuumсleaner.vacuum_cleaner()
  Vacuumсleaner.wash()
