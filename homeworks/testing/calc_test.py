from unittest import TestCase
from Calculator01 import Calculator
import math


class TestCalc(TestCase):
    def setUp(self) -> None:
        self.nums_1 = Calculator(2, "*", 3)

    def test_001(self):
        self.assertIsInstance(self.nums_1.first_num, int)
        self.assertIsInstance(self.nums_1.math_action, str)
        self.assertIsInstance(self.nums_1.second_num, int)

    def test_002(self):
        addition = self.nums_1.first_num + self.nums_2.second_num
        self.assertListEqual((self.nums_1.first_num + self.nums_1.second_num), addition)
        self.assertIsInstance(addition, int)

    def test_003(self):
        mul = self.nums_1.first_num * self.nums_2.second_num
        self.assertListEqual((self.nums_1.first_num * self.nums_1.second_num), mul)
        self.assertIsInstance(mul, int)

    def test_004(self):
        subtraction = self.nums_1.first_num - self.nums_2.second_num
        self.assertListEqual((self.nums_1.first_num - self.nums_1.second_num), subtraction)
        self.assertIsInstance(subtraction, int)

    def test_005(self):
        division = self.nums_1.first_num / self.nums_2.second_num
        self.assertListEqual((self.nums_1.first_num / self.nums_1.second_num), division)
        self.assertIsInstance(division, float)

    def test_006(self):
        degree = self.nums_1.first_num ** self.nums_2.second_num
        self.assertListEqual((self.nums_1.first_num ** self.nums_1.second_num), degree)
        self.assertIsInstance(degree, int)

    def test_007(self):
        root = math.sqrt(self.nums_1.first_num)
        self.assertListEqual((math.sqrt(self.nums_1.first_num)), root)
        self.assertIsInstance(root, float)

    def test_006(self):
        percentages = self.nums_1.second_num * 100 / self.nums_1.first_num
        self.assertListEqual((self.nums_1.second_num * 100 / self.nums_1.first_num), percentages)
        self.assertIsInstance(percentages, int)

