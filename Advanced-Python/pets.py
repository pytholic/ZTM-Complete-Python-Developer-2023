"""
Inheritance exercise.
"""


class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Simon(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Sally(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Swift(Cat):
    def sing(self, sounds):
        return f"{sounds}"


cat1 = Simon("simon", 10)
cat2 = Simon("sally", 12)
cat3 = Simon("swift", 8)

my_cats = [cat1, cat2, cat3]

my_pets = Pets(animals=my_cats)
my_pets.walk()
