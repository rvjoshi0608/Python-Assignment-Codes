# ---------- TUPLE OPERATIONS ----------
print("\n----- TUPLE OPERATIONS -----")
t = (10, 20, 30, 20, 40)
print("Original Tuple:", t)
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))
print("Length:", len(t))
print("Max:", max(t))
print("Min:", min(t))
print("Sum:", sum(t))

new_t = t + (50, 60)
print("After concatenation:", new_t)

sliced = t[1:3]
print("Sliced tuple (1:3):", sliced)

