# Conditional logic
# is_old = True
# is_licensed = True

# if is_old:
#     print("you are old enough to drive.")
# elif is_licensed:
#     print("you can drive.")
# else:
#     print("you cannot drive.")

# if is_old and is_licensed:
#     print("you can drive.")
# else:
#     print("you cannot drive.")

# Truthy and Falsy
# print(bool(5))
# print(bool("hello"))
# print(bool(0))
# print(bool(""))
# password = "123"
# username = "abc"
# if password and username:
#     print("Correct.")

# Ternary Operator
# # condition_if_true if condition else condition_if_false
# is_friend = True
# can_message = "message allowed" if is_friend else "message not allowed."
# print(can_message)

# Short Circuiting
# is_friend = True
# is_user = True
# if is_friend and is_user:
#     print("Best friends.")
# if is_friend or is_user:  # short circuits, care about one condition
#     print("Best friends.")

### Logical Operators ###
# print(4 < 5)
# print("a" > "b")  # based on ASCII
# print("a" > "A")
# print(ord("a"))
# print(ord("A"))
# print(chr(ord("A")))
# print(1 < 2 > 3 < 4)
# print(not (True))

# game exercise
# is_magician = True
# is_expert = False

# if is_magician and is_expert:
#     print("you are a master magician.")
# elif is_magician and is_expert is False:
#     print("at least you're getting there.")
# elif not is_magician:
#     print("you need magic powers.")

# is vs. ==
# # == -> compares value
# print(True == 1)
# print("1" == 1)
# print([] == 1)
# print(10 == 10.0)
# print([] == [])

# # is -> compares location
# print(True is 1)
# print("1" is 1)
# print([] is [])  # memory for each list is different
# print(10 is 10.0)
# print([] is [])

# For loops
# for item in (1, 2, 3, 4, 5):
#     print(item)
# print("done!")

# for x in (1, 2, 3, 4, 5):
#     for y in ("a", "b", "c", "d", "e"):
#         print(x, y)

# Iterables
# user = {"name": "Golem", "age": 5006, "can_swim": False}
# for item in user.items():
#     print(item)
# for k, v in user.items():
#     print(k, v)

# counter exercise
# my_list = list(range(1, 11))
# cnt = 0
# for item in my_list:
#     cnt += item
# print(cnt)

# range
# for i in range(0, 10, 2):
#     print(i)
# for i in range(10, 0, -1):
#     print(i)

# enumerate
# for idx, val in enumerate(["a", "b", "c"]):
#     print(idx, val)
# for idx, val in enumerate(list(range(10))):
#     print(idx, val)
# for idx, val in enumerate(list(range(10))):
#     if val == 5:
#         print(f"Index of 5 is {idx}.")

# While loop
# i = 0
# while i < 50:
#     print(i)
#     i += 1
# print("done!")

# i = 0
# while i < 50:
#     print(i)
#     i += 1
#     break
# else:
#     print("done!")

# while True:
#     response = input("say something: ")
#     if response == "bye":
#         break

# break, continue, pass
# my_list = [1, 2, 3]
# for item in my_list:
#     print(item)
#     break
# for item in my_list:
#     continue
#     print(item)
# for item in my_list:
#     pass
#     print(item)
