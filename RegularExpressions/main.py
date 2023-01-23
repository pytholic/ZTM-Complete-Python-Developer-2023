# import re

# pattern = re.compile("this")
# pattern2 = re.compile("search this inside of this text please!")
# pattern3 = re.compile("search this inside of this text please!")
# string = "search this inside of this text please! hehe"

# # print("search" in string)
# # print(re.search("this", string))

# # a = re.search("this", string)
# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern3.fullmatch(string)
# d = pattern3.match(string)
# # print(a.start())
# # print(a.group())
# print(b)
# print(c)
# print(d)


# import re

# pattern = re.compile(r"([a-zA-Z]).([a])")  # raw string
# string = "search this inside of this text please! hehe"

# a = pattern.search(string)
# print(a.group())
# print(a.group(1))
# print(a.group(2))
