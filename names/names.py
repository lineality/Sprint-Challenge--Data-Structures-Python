import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Time complexity of original
#
# for name_1 in names_1:                  O(n)
#     for name_2 in names_2:              O(n)
#
#         if name_1 == name_2:            O(1)  just one comparison
#             duplicates.append(name_1)   O(1)  just one append
#                                         n*n = n^2

# Solution Code:
#
# get in list form the common elements between two sets
# note (each set contains no duplicates)
duplicates = list(set(names_1) & set(names_2))


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for
# a very efficient approach to this problem
# What's the best time you can accomplish?
# Thare are no restrictions on techniques or data
# structures, but you may not import any additional
# libraries that you did not write yourself.
