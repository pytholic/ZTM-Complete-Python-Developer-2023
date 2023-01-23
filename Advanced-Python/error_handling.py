# Error handling

# try:
#     age = int(input("What is your age? "))
#     print(age)
# except:
#     print("please enter a number.")

# while True:
#     try:
#         age = int(input("What is your age? "))
#         print(age)
#     except:
#         print("please enter a number.")
#     else:
#         print("Thank you!")
#         break

# while True:
#     try:
#         age = int(input("What is your age? "))
#         10 / age  # 0 division
#     except ValueError:
#         print("please enter a number.")
#     except ZeroDivisionError:
#         print("please enter a number higher than 0.")
#     else:
#         print("Thank you!")
#         break


# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(err)


# def sum(num1, num2):
#     try:
#         return num1 / num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)


# print(sum("1", 0))

# while True:
#     try:
#         age = int(input("What is your age? "))
#         10 / age  # 0 division
#     except ValueError:
#         print("please enter a number.")
#         continue
#     except ZeroDivisionError:
#         print("please enter a number higher than 0.")
#         break
#     else:
#         print("Thank you!")
#     finally:
#         print("ok, finally done!")
#     print("can you hear me?")  # doesn't run if we break out of the loop


# What if we want to stop the program with error??
# while True:
#     try:
#         age = int(input("What is your age? "))
#         10 / age  # 0 division
#         # raise ValueError("Hey, cut it out!")
#         raise Exception("Hey, cut it out!")
#     except ZeroDivisionError:
#         print("please enter a number higher than 0.")
#         break
#     else:
#         print("Thank you!")
#     finally:
#         print("ok, finally done!")
#     print("can you hear me?")  # doesn't run if we break out of the loop
