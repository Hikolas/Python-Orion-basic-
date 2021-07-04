# 1. Define the id of next variables:

print("1. Define the id of next variables:")

int_a = 55
print("int_a- ", id(int_a))

str_b = 'cursor'
print("str_b- ", id(str_b))

set_c = {1, 2, 3}
print("set_c- ", id(set_c))

lst_d = [1, 2, 3]
print("lst_d- ", id(lst_d))

dict_e = {'a': 1, 'b': 2, 'c': 3}
print("dict_e-", id(dict_e))


# 2. Append 4 and 5 to the lst_d and define the id one more time.

# print("2. Append 4 and 5 to the lst_d and define the id one more time.")

# lst_d = [1, 2, 3, 4, 5]
# print("lst_d- ", id(lst_d))


# 3. Define the type of each object from step 1.

print("3. Define the type of each object from step 1.")

print("int_a- ", type(int_a))

print("str_b- ", type(str_b))

print("set_c- ", type(set_c))

print("lst_d- ", type(lst_d))

print("dict_e-", type(dict_e))


# 4*. Check the type of the objects by using isinstance.

print("4*. Check the type of the objects by using isinstance.")

print("int_a- ", isinstance(int_a, float))

print("str_b- ", isinstance(str_b, str))

print("set_c- ", isinstance(set_c, (int, set)))

print("lst_d- ", isinstance(lst_d, set))

print("dict_e-", isinstance(dict_e, dict))


# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."


# 5. With .format and curly braces {}

print("5. With .format and curly braces {}")

print("Anna has {} apples and {} peaches.".format(5, 3))


# 6. By passing index numbers into the curly braces.

print("6. By passing index numbers into the curly braces.")

print("Anna has {a} apples and {b} peaches.".format(a=5, b=3))


# 7. By using keyword arguments into the curly braces.

print("7. By using keyword arguments into the curly braces.")

print("Anna has {a} apples and {b} peaches.".format(a=5, b=3))


# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("8*. With indicators of field size (5 chars for the first and 3 for the second)")

print("Anna has {0:5} apples and {0:3} peaches.".format(5, 3))


# 9. With f-strings and variables

print("9. With f-strings and variables")

apple = 5
peacher = 1
print(f"Anna has {apple} apples and {peacher} peaches.")

print(f"Anna has {apple} apples and {peacher} peaches, {apple + peacher} fruits")


# 10. With % operator

print("# 10. With % operator")

print("Anna has %s apples and %s peaches" % (5, 1))


# 11*. With variable substitutions by name (hint: by using dict)

print("11*. With variable substitutions by name (hint: by using dict)")

apple = "ten"
peacher = "five"
data_dict = {"app": apple, "peach": peacher}
print("Anna has %(app)s apples and %(peach)s peaches" % data_dict)


# 12. Convert (1) to list comprehension

print("12. Convert (1) to list comprehension")

lst_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_comp)

# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)


# 13. Convert (2) to regular for with if-else

print("13. Convert (2) to regular for with if-else")

lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)

# list_comp = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
# print(list_comp)


# 14. Convert (3) to dict comprehension.

print("14. Convert (3) to dict comprehension.")

d_comp = {x: x ** 2 for x in range(1, 11) if x % 2 == 1}
print(d_comp)

# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)


# 15*. Convert (4) to dict comprehension.

print("15*. Convert (4) to dict comprehension.")

d_comp = {x: x ** 2 if x % 2 == 1 else x // 0.5 for x in range(1, 11) }
print(d_comp)

d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)


# 16. Convert (5) to regular for with if.

print("16. Convert (5) to regular for with if.")

d = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
print(d)

# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
# print(dict_comprehension)


# 17*. Convert (6) to regular for with if-else.

print("17*. Convert (6) to regular for with if-else.")

d = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        d[num] = num ** 3
    else:
        d[num] = num
print(d)


# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# print(dict_comprehension)

# Lambda:

# foo = lambda x, y, z: z if y < x and x > z else y

# 18. Convert (7) to lambda function

print("18. Convert (7) to lambda function")

foo = lambda x, y: x if x < y else y

# def foo(x, y):(7)
#     if x < y:
#         return x
#     else:
#         return y


# 19*. Convert (8) to regular function

print("19*. Convert (8) to regular function")

def foo (x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

# foo = lambda x, y, z: z if y < x and x > z else y (8)


# _________________________________________________________________________________________________________________________
# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]


# 20. Sort lst_to_sort from min to max

print("20. Sort lst_to_sort from min to max")

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print (sorted(lst_to_sort))


# 21. Sort lst_to_sort from max to min

print("21. Sort lst_to_sort from max to min")

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort, reverse=True))


# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

print("22. Use map and lambda to update the lst_to_sort by multiply each element by 2")

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
new_lst = (list(map(lambda x: x * 2, lst_to_sort)))
print(new_lst)


# 23*. Raise each list number to the corresponding number on another list:

print("# 23*. Raise each list number to the corresponding number on another list:")

list_A = [2, 3, 4]
list_B = [5, 6, 7]

list_A = (list(map(lambda x, y: x**y, list_A, list_B)))
print(list_A, ' = ', list_B)
# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

print("24. Use reduce and lambda to compute the numbers of a lst_to_sort.")

from functools import reduce

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
sum_lst_to_sort = reduce(lambda x, y: x + y, lst_to_sort)
print(sum_lst_to_sort)


# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

print("25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.")

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
filter_lst_to_sort = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(filter_lst_to_sort)


# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

print(" 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.")

print(list(filter(lambda  x: (x < 0), range(-10, 10))))


#27*. Using the filter function, find the values that are common to the two lists:

print("27*. Using the filter function, find the values that are common to the two lists:")

list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print(list(filter(lambda x: x in list_1, list_2)))
