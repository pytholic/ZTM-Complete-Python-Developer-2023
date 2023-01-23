# Walrus operator :=
# a = "helloooooooo"
# if len(a) > 10:
#     print(f"Too long {len(a)} elements")
# if (n := len(a)) > 10:
#     print(f"Too long {n} elements")

# while (n := len(a)) > 1:
#     print(n)
#     a = a[:-1]
# print(a)

# Scope
# a = 1


# def confusion():
#     a = 5  # only in function scope
#     return a


# print(a)
# print(confusion())

# global keyword
# total = 0


# def count():
#     global total
#     total = 3
#     return total


# print(count())
# print(total)

# Dependency injection, detach dependency
# total = 0


# def count(total):
#     total += 1
#     return total


# print(count(count(count(total))))

# nonlocal keyword
# def outer():
#     x = "local"

#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)

#     inner()
#     print("outer:", x)
