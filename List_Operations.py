# ---------- LIST OPERATIONS ----------
print("----- LIST OPERATIONS -----")
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

fruits.append("mango")
print("After append:", fruits)

fruits.insert(1, "orange")
print("After insert:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

popped = fruits.pop()
print("Popped element:", popped, "-> List:", fruits)

fruits.sort()
print("After sort:", fruits)

fruits.reverse()
print("After reverse:", fruits)

print("Index of 'apple':", fruits.index("apple"))
print("Count of 'apple':", fruits.count("apple"))

