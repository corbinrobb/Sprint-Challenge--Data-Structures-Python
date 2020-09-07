import time


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif self.value <= value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif self.value < target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)



start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# runtime: ~6.727s

# first pass
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)
# runtime: ~1.50s

# second pass
# duplicates = [n1 for n1 in names_1 if n1 in names_2]
# runtime: ~1.48s -- no improvement

tree = BSTNode(names_2[0])

for n2 in range(1, len(names_2)):
    tree.insert(names_2[n2])

# 3 using binary search tree
for name_1 in names_1:
    if tree.contains(name_1):
        duplicates.append(name_1)
# runtime: 0.134s -- best 





#  !!! stretch attempt !!! 
# duplicates = list(set(names_1) & set(names_2))
# runtime: ~0.004s --- clear winner

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


