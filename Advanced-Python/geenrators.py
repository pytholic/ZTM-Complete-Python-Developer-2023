# Generator


# def generator_function(num):
#     for i in range(num):
#         yield i * 2


# g = generator_function(100)
# print(g)
# print(next(g))
# next(g)
# next(g)
# print(next(g))

# for item in generator_function(1000):
#     print(item)

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# from time import time


# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f"Took {t2-t1} sec.")
#         return result

#     return wrapper


# @performance
# def long_time():
#     print("1")
#     for i in range(100000000):
#         i * 5


# @performance
# def long_time2():
#     print("2")
#     for i in list(range(100000000)):
#         i * 5


# long_time()
# long_time2()

# for loop
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])

# range
class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration  # no more things to iterate over


gen = MyGen(0, 100)
for i in gen:
    print(i)
