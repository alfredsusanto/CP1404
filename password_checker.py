import string
import random

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = string.punctuation

def check_password(pw,validator):
    for each in pw:
        if each in validator:
            return True
    return False

print("Please enter a valid password\n"
      "Your password must be between 5 and 15 characters, and contain:\n"
      "\t1 or more uppercase characters\n"
      "\t1 or more lowercase characters\n"
      "\t1 or more numbers\n"
      "\t1 or more special characters: !@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|\n")



password=input(">> ")

while True:
    if len(password)>15 or len(password)<5:
        print("Invalid password")
        password=input(">> ")
    elif not check_password(password,UPPER):
        print("Invalid password")
        password=input(">> ")
    elif not check_password(password,LOWER):
        print("Invalid password")
        password=input(">> ")
    elif not check_password(password,DIGITS):
        print("Invalid password")
        password=input(">> ")
    elif not check_password(password,SPECIAL):
        print("Invalid password")
        password=input(">> ")
    else:
        break

print("Password accepted")













"""
new_password= "" #password generator
for i in range(random.randint(5,15)):
    rand_choice=random.randint(1,4)
    if rand_choice == 1:
        new_password += random.choice(LOWER)
    elif rand_choice == 2:
        new_password += random.choice(UPPER)
    elif rand_choice == 3:
        new_password += random.choice(DIGITS)
    else:
        new_password += random.choice(SPECIAL)

print(new_password)
print(new_password[0] in LOWER)
print(new_password[0] in UPPER)
"""