import random
import string

print("\tPassword Generator")

try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Invalid input")
    exit()

if length < 1:
    print("The password can't be lessthan 1 character. ")
    exit()

upper_case = input("Include Upper case? y/n: ").lower()
lower_case = input("Include lower case? y/n: ").lower()
numbers = input("Include numbers? (y/n): ").lower()
symbols = input("Include a symbols? y/n: ").lower()

character_pool = ""

if upper_case == "y":
    character_pool += string.ascii_uppercase

if lower_case == 'y':
    character_pool += string.ascii_lowercase

if numbers == 'y':
    character_pool += string.digits

if symbols == 'y':
    character_pool += string.punctuation

if not character_pool:
    print("Nothing to generate password from")
    exit()


while True:
    password = ""
    for i in range(length):
        password += random.choice(character_pool)
    print(f'Your password is: {password}')

    answer = input("Do you want to generate another password? y/n ").lower()
    if answer == 'n':
        break