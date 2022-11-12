# This code determines whether the number given by a user is even or odd using if, else statements

number = int(input("Give me a number between 0 and 100\n\n"))
if (number % 2) == 0:
    print(f"Your number {number} is even")
else:
    print(f"Your number {number} is odd")

