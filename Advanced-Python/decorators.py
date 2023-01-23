# # Higher Order Function HOC
# def greet(func):
#     func()


# def greet2():
#     def func():
#         return 5

#     return func

# Decorator
"""
Enhances another function.
"""


# def hello():
#     print("Hello!")


# def my_decorator(func):
#     def wrap_func():
#         print("*****")
#         func()
#         print("-----")

#     return wrap_func


# @my_decorator
# def hello():
#     print("Hello!")


# @my_decorator
# def bye():
#     print("Bye!")


# # a = my_decorator(hello)  # not pythonic way
# # a()

# hello()
# bye()


# def my_decorator(func):
#     def wrap_func(x):
#         print("*****")
#         func(x)
#         print("-----")

#     return wrap_func


# @my_decorator
# def hello(greeting):
#     print(greeting)


# hello("hii")


# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         # print("*****")
#         func(*args, **kwargs)
#         # print("-----")

#     return wrap_func


# @my_decorator
# def hello(greeting, emoji=":("):
#     print(greeting, emoji)


# hello("hii")
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"Took {t2-t1} sec.")
        return result

    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i * 5


long_time()
