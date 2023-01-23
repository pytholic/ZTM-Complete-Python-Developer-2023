# def say_hello():
#     print("Hello!")


# say_hello()

# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
# ]


# def show_tree():
#     for row in picture:
#         for pixel in row:
#             print("*", end="") if pixel else print(" ", end="")
#         print("")


# show_tree()
# show_tree()

# Positional arguments
# def say_hello(name, emoji):
#     print(f"Hello {name} {emoji}")


# say_hello("Haseeb", "😄")

# Keyword arguments
# def say_hello(name, emoji):
#     print(f"Hello {name} {emoji}")


# say_hello(name="Haseeb", emoji="😄")

# Default parameters
# def say_hello(name="Haseeb", emoji="😃"):
#     print(f"Hello {name} {emoji}")


# say_hello()
# say_hello("abc")

# Return
# def sum(num1, num2):
#     return num1 + num2


# print(sum(2, 5))
# total = sum(10, 5)
# print(sum(10, total))


# def sum(num1, num2):
#     def another_func(num1, num2):
#         return num1 + num2

#     return another_func(num1, num2)  # return a function


# total = sum(10, 5)
# print(total)


# def test(a):
#     """
#     Info: Tests and prints param a
#     """
#     print(a)


# # test(1)
# # help(test)
# print(test.__doc__)

# Clean code
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     elif num % 2 != 0:
#         return False


# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False


# def is_even(num):
#     return num % 2 == 0


# print(is_even(50))

# *args, **kwargs
# def super_func(*args):
#     print(args)
#     return sum(args)


# print(super_func(1, 2, 3, 4, 5))


# def super_func(*args, **kwargs):
#     print(args, kwargs)
#     return sum(args) + sum(items for items in kwargs.values())


# print(super_func(1, 2, 3, 4, 5, num1=10, num2=20))


# def super_func(*args, **kwargs):
#     print(args, kwargs)
#     total = 0
#     for item in kwargs.values():
#         total += item
#     return sum(args) + total


# print(super_func(1, 2, 3, 4, 5, num1=10, num2=20))

# Exercise
# def highest_even(li):
#     evens = []
#     for item in li:
#         if item % 2 == 0:
#             evens.append(item)
#     return max(evens)


# print(highest_even([10, 2, 3, 4, 7]))
