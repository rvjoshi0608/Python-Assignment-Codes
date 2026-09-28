# ---------- DICTIONARY OPERATIONS ----------
print("\n----- DICTIONARY OPERATIONS -----")
student = {"name": "Riya", "age": 20, "course": "CSE"}
print("Original Dictionary:", student)

student.update({"age": 21})
print("After update:", student)

student["grade"] = "A"
print("After adding new key:", student)

removed_value = student.pop("course")
print("Popped 'course':", removed_value, "-> Dict:", student)

print("Get 'name':", student.get("name"))
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student.clear()
print("After clear:", student)