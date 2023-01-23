some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)
print(duplicates)
