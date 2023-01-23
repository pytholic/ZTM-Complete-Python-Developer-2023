"""
Object Oriented Programming
"""


# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print("run")


# player1 = PlayerCharacter("Haseeb", 25)
# # player1.run()
# # print(player1.name, player1.age)

# # player1.attack = 50
# # print(player1.attack)

# help(player1)


# class PlayerCharacter:
#     # Class Object Attribute
#     membership = True

#     def __init__(self, name, age):
#         if PlayerCharacter.membership:
#             self.name = name  # attributes
#             self.age = age

#     def run(self, var):
#         print(f"{var} and run {self.name}")


# player1 = PlayerCharacter("Haseeb", 25)
# player1.run(var="hello")

# __init__
# class PlayerCharacter:
#     # Class Object Attribute
#     def __init__(self, name="anonymous", age=0):
#         if age > 18:
#             self.name = name  # attributes
#             self.age = age

#     def shout(self):
#         print(f"My name is {self.name}")


# player1 = PlayerCharacter("Tom", 10)
# print(player1.shout())


# class PlayerCharacter:
#     # Class Object Attribute
#     def __init__(self, name="anonymous", age=0):
#         if age > 18:
#             self.name = name  # attributes
#             self.age = age

#     def shout(self):
#         print(f"My name is {self.name}")


# player1 = PlayerCharacter("Tom", 30)
# player1.shout()

# classmethod and @staticmethod
# class PlayerCharacter:
#     membership = True
#     # Class Object Attribute
#     def __init__(self, name="anonymous", age=0):

#         self.name = name  # attributes
#         self.age = age

#     def shout(self):
#         print(f"My name is {self.name}")

#     @classmethod
#     def adding_things(cls, num1, num2):
#         # return num1 + num2
#         return cls("Teddy", num1 + num2)  # can also instantiate object

#     @staticmethod
#     def adding_things2(num1, num2):
#         # return num1 + num2
#         return num1 + num2


# player1 = PlayerCharacter("Tom", 30)
# print(player1.adding_things(2, 3))
# print(PlayerCharacter.adding_things(2, 3))
# player = PlayerCharacter.adding_things(2, 3)
# print(player.age)

# General structure
# class NameOfClass:
#     class_attribute = "value"

#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2

#     def method(self):
#         pass

#     @classmethod
#     def cls_method(cls, param1, param2):
#         pass

#     @staticmethod
#     def stc_method(param1, param2):
#         pass

# Encapsulation
# """
# Defining methods and attributes in an object instead
# of outside is called encapsulation. We package everything
# in one object.
# We need both attributes and methods to do something useful.
# """
# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print("run")

#     def speak(self):
#         print(f"My name is {self.name}. I am {self.age} years old.")


# player = PlayerCharacter("Haseeb", 25)
# player.speak()

# Abstraction
# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print("run")

#     def speak(self):
#         print(f"My name is {self.name}. I am {self.age} years old.")


# player = PlayerCharacter("Haseeb", 25)
# player.speak()

# Public and private
# class PlayerCharacter:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     def run(self):
#         print("run")

#     def speak(self):
#         print(f"My name is {self.name}. I am {self.age} years old.")


# player = PlayerCharacter("Haseeb", 25)
# player._name = "!!!"
# player._speak = "BOOOOO"

# print(player.speak)

# Inheritance
# class User:
#     def sign_in(self):
#         print("logged in")


# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f"attacking with power of {self.power}")


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f"attacking with arrows, arroes left {self.num_arrows}")


# wizard1 = Wizard("Merlin", 50)
# archer1 = Archer("Robin", 100)

# print(isinstance(wizard1, Wizard))
# print(isinstance(wizard1, User))
# print(isinstance(wizard1, object))

# Polymorphism
# class User:
#     def sign_in(self):
#         print("logged in")

#     def attack(self):
#         print("do nothing.")


# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         User.attack(self)
#         print(f"attacking with power of {self.power}")


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f"attacking with arrows, arrows left {self.num_arrows}")


# wizard1 = Wizard("Merlin", 50)
# archer1 = Archer("Robin", 30)


# # def player_attack(char):
# #     char.attack()


# # player_attack(wizard1)
# # player_attack(archer1)

# # for char in [wizard1, archer1]:
# #     char.attack()

# wizard1.attack()

# init and super()
# class User:
#     def __init__(self, email):
#         self.email = email

#     def sign_in(self):
#         print("logged in")


# class Wizard(User):
#     def __init__(self, name, power, email):
#         super().__init__(email)
#         # User.__init__(self, email)
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f"attacking with power of {self.power}")


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f"attacking with arrows, arrows left {self.num_arrows}")


# wizard1 = Wizard("Marlin", 50, "merlin@gmail.com")
# # print(wizard1.email)

# # introspection
# print(dir(wizard1))

# Dunder methods
# class Toy:
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {"name": "yoyo", "has_pets": False}

#     def __str__(self):
#         return f"{self.color}"

#     def __len__(self):
#         return 5

#     def __del__(self):
#         print("Deleted")

#     def __call__(self):
#         return "yes??"

#     def __getitem__(self, i):
#         return self.my_dict[i]


# action_figure = Toy("red", 0)
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# print(action_figure())  # call method
# # del action_figure
# print(action_figure["name"])

# Exercise: Extend List
# class SuperList(list):
#     def __len__(self):
#         return 1000


# super_list1 = SuperList()
# # print(len(super_list1))
# super_list1.append(5)
# print(len(super_list1))
# print(super_list1[0])
# print(issubclass(SuperList, list))

# Multiple inheritance
# class User:
#     def sign_in(self):
#         print("logged in")


# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f"attacking with power of {self.power}")


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def check_arrows(self):
#         print(f"{self.num_arrows} remaining")

#     def run(self):
#         print("ran really fast")


# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, num_arrows):
#         Archer.__init__(self, name, num_arrows)
#         Wizard.__init__(self, name, power)


# hybrid1 = HybridBorg("borgie", 50, 100)
# hybrid1.run()
# hybrid1.check_arrows()
# hybrid1.attack()
# hybrid1.sign_in()

# MRO Method Resolution Order
# class A:
#     num = 10


# class B(A):
#     pass


# class C(A):
#     num = 1


# class D(B, C):
#     pass


# print(D.num)  # DBCA
# print(D.mro())
# print(D.__mro__)
