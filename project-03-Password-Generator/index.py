import random
import string

print("\n=== Password Generator ===")

try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if length < 1:
    print("Password length must be at least 1.")
    exit()

upper_case = input("Include uppercase letters? (y/n): ").lower()
lower_case = input("Include lowercase letters? (y/n): ").lower()
numbers = input("Include numbers? (y/n): ").lower()
symbols = input("Include symbols? (y/n): ").lower()

character_pool = ""

if upper_case == "y":
    character_pool += string.ascii_uppercase

if lower_case == "y":
    character_pool += string.ascii_lowercase

if numbers == "y":
    character_pool += string.digits

if symbols == "y":
    character_pool += string.punctuation

if not character_pool:
    print("Cannot generate a password with no characters.")
    exit()

while True:
    password = ""

    for i in range(length):
        password += random.choice(character_pool)

    print(f"\nYour password: {password}")

    answer = input("\nGenerate another password? (y/n): ").lower()

    if answer == "n":
        print("Goodbye!")
        break
    