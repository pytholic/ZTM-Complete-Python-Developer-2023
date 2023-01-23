### First command ###
# name = input("What is your name?")
# print(name)

# int and floats
# print(type(4))
# print(type(0.001))

# binary
# print(bin(5))  # 0b101
# print(int("0b101", 2))

# string
# print(type("Iam haseeb."))
# USERNAME = "Haseeb"
# long_string = """
# wow
# omg
# """
# print(long_string)

# first_name = "Haseeb"
# last_name = "Raja"
# full_name = first_name + " " + last_name  # string concatenation
# print(full_name)

# Math functions
# print(round(3.1))
# print(abs(-20))

# Operators precedence
# print((20 - 3) + 2**2)

# Augmented assigment operator
# some_value = 5
# some_value = some_value + 2
# some_value += 2

### String ###
# Escape sequence
# weather = "It's sunny"
# # weather = 'It's sunny'
# # weather = "It's "kind of" sunny"  # need escape sequence
# weather = 'It\'s "kind of" sunny'
# # weather = "It\'s \"kind of\" sunny"
# weather = '\tIt\'s "kind of" \nsunny'

# Formatted strings
# name = "Jonny"
# age = 55
# print("Hi " + name + ". You are " + str(age) + " years old.")
# print(f"Hi {name}. You are {age} years old.")
# print("Hi {}. You are {} years old.".format(name, age))
# print(
#     "Hi {new_name}. You are {new_age} years old.".format(new_name="sally", new_age=30)
# )

# String slicing
# selfish = "0123456789"
# print(selfish[:5])
# print(selfish[5:])
# print(selfish[-1])
# print(selfish[::-1])  # reverse

# String immutability
# selfish = "0123456789"
# selfish[2] = "9"  # immutability error
# selfish = selfish + '8'  # whole new string

# String methods
# quote = "to be or not to be"
# print(quote.upper())
# print(quote.capitalize())
# print(quote.find("be"))
# print(quote.replace("be", "me"))  # new string created
# print(quote)  # will keep original -> immutability

####################################

# Booleans
# print(bool(0))
# print(bool(1))
# print(bool("True"))

# Example: fb provile
# name = "Haseeb Raja"
# age = 50
# relationship_status = "single"
# relationship_status = "It's complicated"
# print(relationship_status)

# birth_year = input("What year were you born in?")
# age = 2023 - int(birth_year)
# print(f"You age is {age}.")

# Password exercide
# print("*" * 10)
# name = input("Enter you name.")
# password = input("Enter password.")
# password_hidden = "*" * len(password)
# pass_length = len(password)
# print(f"{name} your password {password_hidden} is {pass_length} characters long.")

### List ###
# List slicing
# amazon_cart = ["notebooks", "sunglasses", "toys", "grqapes"]
# print(amazon_cart[::2])
# amazon_cart[0] = "laptop"
# print(amazon_cart)
# new_cart = amazon_cart  # we did not use copy, it will modify actual memory location
# new_cart[0] = "gum"
# print(new_cart)
# print(amazon_cart)
# new_cart = amazon_cart.copy()
# new_cart[0] = "gum"
# print(new_cart)
# print(amazon_cart)
# new_cart = amazon_cart[:]
# new_cart[0] = "gum"
# print(new_cart)
# print(amazon_cart)

# Matrix
# matrix = [[1, 2, 3], [2, 4, 6], [7, 8, 9]]
# print(matrix[0][0])

### List actions ###
# adding items
# tmp = [1, 2, 3, 4, 5]
# print(len(tmp))
# tmp.append(100)
# print(tmp)
# tmp.insert(4, 200)
# print(tmp)
# tmp.extend([300, 301, 302])
# print(tmp)

# removing items
# tmp.pop()
# print(tmp)
# tmp.pop(0)
# print(tmp)
# tmp.remove(100)
# print(tmp)

# new_list = ["a", "b", "c"]
# print(new_list.index("b"))
# print(new_list.index("b", 0, 2))
# print("b" in new_list)
# print(new_list.count("b"))

# tmp = ["a", "d", "b", "c"]
# tmp.sort()
# # print(tmp)
# # print(sorted(tmp))  # produces a new list
# tmp.reverse()
# print(tmp)
# print(tmp[::-1])  # creates a new list

# print(list(range(0, 101)))

# new_sentence = " ".join(["hi", "my", "name", "is", "haseeb"])  # creates new item
# print(new_sentence)

# list unpacking
# a, b, c = [1, 2, 3]
# print(a, b, c)
# a, b, c, *other = [1, 2, 3, 4, 5, 6, 7]
# print(a, b, c, other)

############################################

### Dictionary ###
# dictionary = {"a": 1, "b": 2}
# print(dictionary["a"])
# print(dictionary.get("a"))

# new_dict = {"a": [1, 2, 3], "b": "hello", "c": True}
# print(new_dict["a"])

# my_list = [
#     {"a": [1, 2, 3], "b": "hello", "c": True},
#     {"a": [4, 5, 6], "b": "hello", "c": True},
# ]
# print(my_list[0])
# print(my_list[0]["a"])
# print(my_list[0]["a"][2])

# dict keys
# dictionary = {123: [1, 2, 3], True: "hello"}
# print(dictionary)
# dictionary = {123: [1, 2, 3], True: "hello", [100]: True}
# print(dictionary)

# dict methods
# new_dict = {"a": [1, 2, 3], "b": "hello", "c": True}
# # print(new_dict["e"])
# print(new_dict.get("e"))  # avoid error
# print(new_dict.get("e", 10))

# tmp = dict(a=[1, 2, 3], b="hello", c=True)
# print(tmp)

# new_dict = {"a": [1, 2, 3], "b": "hello", "c": True}
# # print("a" in new_dict)
# # print("e" in new_dict)
# # print("a" in new_dict.keys())
# # print("hello" in new_dict.values())
# # print(new_dict.items())
# # tmp = new_dict.copy()
# # print(tmp)
# # print(tmp.pop("a"))
# # print(tmp)
# # print(new_dict.popitem())
# new_dict.update({"a": [4, 5, 6]})
# print(new_dict)

### Tuple ###
# my_tuple = (1, 2, 3, 4, 5)
# new_tuple = my_tuple[1:3]
# print(new_tuple)
# print(my_tuple[0])
# x, y, z, *others = my_tuple
# print(x, y, z, others)

### Set ###
# my_set = {1, 2, 2, 3, 4, 5}
# print(my_set)
# my_set.add(100)
# my_set.add(2)
# print(my_set)

# a = [1, 2, 3, 4, 5, 5]
# a_set = set(a)
# print(list(a_set))
# print(a_set[0])

# set_1 = {1, 2, 3, 4, 5}
# set_2 = {4, 5, 6, 7, 8, 9, 10}
# print(set_1.difference(set_2))
# set_1.discard(5)
# print(set_1)
# set_1.difference_update(set_2)
# print(set_1)
# print(set_1.intersection(set_2))
# print(set_1.isdisjoint(set_2))
# print(set_1.union(set_2))
# print(set_1 | set_2)
# print(set_1 & set_2)

# set_1 = {4, 5}
# set_2 = {4, 5, 6, 7, 8, 9, 10}
# print(set_1.issubset(set_2))
# print(set_1.issuperset(set_2))
# print(set_2.issuperset(set_1))
