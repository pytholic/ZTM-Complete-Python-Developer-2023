### File I/O ###

# Read a file

# my_file = open("test.txt")
# print(my_file.read())
# print(my_file.read())
# print(my_file.read())

# After first read, the cursor will be at the EOF
# So nothing is read in next read()

# my_file = open("test.txt")
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# my_file = open("test.txt")
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# my_file = open("test.txt")
# print(my_file.readlines())

# my_file.close()

# Read, write and append
# Read
# with open("test.txt", mode="r") as f:
#     print(f.readlines())

# Write and append
# with open("test.txt", mode="r+") as f:
#     text = f.write(":)")
#     print(text)

# with open("test.txt", mode="a") as f:
#     text = f.write(":)")
#     print(text)

# with open("test.txt", mode="w") as f:
#     text = f.write(":)")
#     print(text)

# with open("sad.txt", mode="w") as f:
#     text = f.write(":(")
#     print(text)

# File I/O errors
# try:
#     with open("sad.txt", mode="r") as f:
#         print(f.read())
# except FileNotFoundError as err:
#     print("File does not exist.")
#     raise err
# except IOError as err:
#     print("IO error.")
#     raise err

# Exercise
