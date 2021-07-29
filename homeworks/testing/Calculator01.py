import math
import logging

template = "%(levelname)s: %(asctime)s: %(filename)s: - %(message)s"
logging.basicConfig(level=logging.INFO, filename="logCal.log", filemode="a", format=template)

class NegativeNumber(Exception):
    pass

def operations(first_num):
    if first_num < 0:
        raise NegativeNumber



class Calculator:
    def __init__(self, first_num: float, math_action: str, second_num: float):
        self.first_num = first_num
        self.math_action = math_action
        self.second_num = second_num

    def addition(self):
        result = self.first_num + self.second_num
        print(self.first_num, " ", self.math_action, " ", self.second_num, " = ", result)
        self.first_num = result

    def subtraction(self):
        result = self.first_num - self.second_num
        print(self.first_num, " ", self.math_action, " ", self.second_num, " = ", result)
        self.first_num = result

    def multiplication(self):
        result = self.first_num * self.second_num
        print(self.first_num, " ", self.math_action, " ", self.second_num, " = ", result)
        self.first_num = result

    def division(self):
        try:
            result = self.first_num / self.second_num
        except ZeroDivisionError:
            logging.error("Zero division error")
            print("Error")
        else:
            result = self.first_num / self.second_num
            print(self.first_num, " ", self.math_action, " ", self.second_num, " = ", result)
            self.first_num = result
    def degree(self):
        result: int
        result = self.first_num ** self.second_num
        print(self.first_num, " ", self.math_action, " ", self.second_num, " = ", result)
        self.first_num = result

    def root(self):
        try:
            operations(self.first_num)
        except NegativeNumber:
            logging.error("Negative Number error")
            print("Error")
        else:
            result = self.first_num ** (1/self.second_num)
            print(self.first_num, " ", self.math_action, " ", self.second_num, " = ", result)
            self.first_num = result

    def percentages(self):
        try:
            operations(self.first_num)
        except NegativeNumber:
            logging.error("Negative Number error")
            print("Error")
        else:
            result = self.second_num * 100 / self.first_num
            print(self.first_num, " ", self.math_action, " ", self.second_num, " = ", math.ceil(result), "%")
            print(self.first_num, " ", self.math_action, " ", self.second_num, " = ", result)
            self.first_num = result


    def calculations(self):
      logging.info(f"Choice of math action")
      if self.math_action == "+":
        logging.info(f"Perform addition {self.first_num} , {self.second_num}")
        Calculator.addition(self)

      elif self.math_action == "-":
        logging.info(f"Perform subtraction {self.first_num} , {self.second_num}")
        Calculator.subtraction(self)

      elif self.math_action == "*":
        logging.info(f"Perform multiplication {self.first_num} , {self.second_num}")
        Calculator.multiplication(self)

      elif self.math_action == "/":
        logging.info(f"Perform division {self.first_num} , {self.second_num}")
        Calculator.division(self)

      elif self.math_action == "^":
        logging.info(f"Performing elevation to the degree {self.first_num} , {self.second_num}")
        Calculator.degree(self)

      elif self.math_action == "^(1/":
        logging.info(f"Performing elevation to the root  {self.first_num} ")
        Calculator.root(self)

      elif self.math_action == "%":
        logging.info(f"Performing the calculation of percentages {self.first_num} , {self.second_num}")
        Calculator.percentages(self)



    def substitute(self):
        logging.info(f"Introduction of a new action ")
        print(self.first_num)
        self.math_action = (input())
        self.second_num = float(input())

logging.info("Programm started")

calculator = Calculator(2, "*", 3)
i = 0
on = 0
while on == 0:
  if i == 1:
    calculator.substitute()
    calculator.calculations()
  elif i == 0:
    calculator.calculations()
  i = 1
