import re
 
def check_string(s):
    pattern = r'^[a-zA-Z0-9]+$'
    if re.match(pattern, s):
        return True
    return False
 
test_strings = ["Hello123", "Hello_123", "Python3", "Hello World"]
 
for s in test_strings:
    if check_string(s):
        print(f"'{s}' contains only allowed characters (a-z, A-Z, 0-9)")
    else:
        print(f"'{s}' contains invalid characters")
 
user_string = input("\nEnter a string to check: ")
if check_string(user_string):
    print(f"'{user_string}' is valid - contains only letters and digits")
else:
    print(f"'{user_string}' is invalid - contains special characters or spaces")
