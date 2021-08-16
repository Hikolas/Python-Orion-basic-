import random
import time
import math
from threading import Thread


class MyThread(Thread):
    def __init__(self, a, b, c):
        Thread.__init__(self)
        self.a = a
        self.b = b
        self.c = c

    def run(self):
        des = (self.b**2)-4*self.a*self.c
        print("Des =", des)
        d = math.sqrt(des)
        if des > 0:
            result = (-self.b + d) / 2 * self.a
            result1 = (-self.b - d) / 2 * self.a
            print("x1 = ", result, " x2 = ", result1)
        if des < 0:
            print("None")
        if des == 0:
            result = (-b + d)/2*a
            print("x = ", result)

    def condition_check(self):
        pass

Num1 = [1, 3, -6]
Num2 = [1, 2, -4]
def create_threads():
    for i in range(2):
        if i == 1:
            my_thread = MyThread(Num1[0], Num1[1], Num1[2])
        else:
            my_thread = MyThread(Num2[0], Num2[1], Num2[2])
        my_thread.start()

print("Threads starting")
create_threads()

