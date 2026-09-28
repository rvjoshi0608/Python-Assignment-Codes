def is_right_angled(a, b, c):
    sides = sorted([a, b, c])
    x, y, z = sides
    return (x**2 + y**2) == (z**2)
 
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
 
if is_right_angled(a, b, c):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")
