import time
import math

# Task 1
#
def decor_time_check(func):
    def wrap(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        print(time.time() - t1)
        return result
    return wrap

@decor_time_check
def writebook():
    list_book = []
    a = 0
    while a == 0:
        replica = input(str())
        if replica != "end":
            list_book.append(replica)
        else:
            return list_book
print(writebook())


# Task 2

def decor_complete_answer(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"При катетах", *args,  "– гіпотенуза дорівнює", result)
        return result
    return wrap

@decor_complete_answer
def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c


print(hypotenuse(4, 3))

# Task 3


def decor_filter_(func):
    def wrap(list_):
        new_list = []
        for el in list_:
            if isinstance(el, (int, float)):
                new_list.append(el)
        result = func(new_list)
        return result
    return wrap



@decor_filter_
def sum_list(lst: list):
    sum_ = sum(list(lst))
    return sum_

print(sum_list([2, 4, 55, 5]))

# Task 4

def traducir(func):
    def wrap(*args):
        result = func(*args)
        new_list = [str(el) for el in result]
        return new_list
    return wrap

@traducir
def sum_list(n):
   list_n = list(map(int, str(n)))
   return list_n

print(sum_list(534242))