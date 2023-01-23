# Pure fuctions
# is a pure function
# def multiply_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list


# print(multiply_by_2([1, 2, 3]))

# not a pure function
# def multiply_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return print(new_list)  # print statement with outside world e.g. display


# new_list = []


# def multiply_by_2(li):
#     for item in li:
#         new_list.append(item * 2)
#     return new_list


# print(multiply_by_2([1, 2, 3]))  # interacts with outer list

# map filter zip reduce
# map
# my_list = [1, 2, 3]


# def multiply_by_2(item):
#     return item * 2


# print(list(map(multiply_by_2, my_list)))
# print(my_list)  # does not affect the original list

# filter
# my_list = [1, 2, 3]


# def only_odd(item):
#     return item % 2 != 0


# print(list(filter(only_odd, my_list)))

# zip
# my_list = [1, 2, 3]
# your_list = [4, 5, 6]
# their_list = [7, 8, 9]
# print(list(zip(my_list, your_list, their_list)))

# reduce
# from functools import reduce

# my_list = [1, 2, 3]


# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item  # result becomes the new acc


# print(reduce(accumulator, my_list, 10))  # param3 is initial value for acc

# Exercise
from functools import reduce

# my_pets = ["sisi", "bibi", "titi", "carla"]


# def upper(item: str):
#     return item.upper()


# print(list(map(upper, my_pets)))

# my_string = ["a", "b", "c", "d", "e"]
# my_numbers = [5, 4, 3, 2, 1]
# # print(list(zip(my_string, sorted(my_numbers))))

# scores = [73, 20, 65, 19, 100, 88, 76]


# def is_greater(val):
#     return val > 50


# print(list(filter(is_greater, scores)))

# my_numbers = [5, 4, 3, 2, 1]
# scores = [73, 20, 65, 19, 100, 88, 76]


# def accumulator(acc, item):
#     return acc + item


# print(reduce(accumulator, my_numbers + scores, 0))

# Lambda expressions
# """
# lambda param: action(param)
# """

# my_list = [1, 2, 3]


# print(list(map(lambda item: item * 2, my_list)))
# print(list(filter(lambda item: item % 2 != 0, my_list)))
# print(reduce(lambda acc, item: acc + item, my_list))

# Exercise
# square
# my_list = [5, 4, 3]
# print(list(map(lambda x: x**2, my_list)))

# # sorting based on second item
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# # a.sort()  # sorts based on first item
# # print(a)
# a.sort(key=lambda x: x[1])  # we cans et key
# print(a)

# Comprehensions
# list, set, dict

# loop way
# my_list = []
# for char in "hello":
#     my_list.append(char)
# print(my_list)

# list comprehension
# my_list = [char for char in "hello"]
# print(my_list)
# s

# Set and dict comprehension
# set
# my_set = {char for char in "hello"}

# # dict
# simple_dict = {"a": 1, "b": 2}
# my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}
# print(my_dict)
