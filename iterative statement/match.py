import sys

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Exit")

while True:

    print()

    ch = int(input("Enter your choice: "))

    match ch:

        case 1:
            x = int(input("Enter 1st Number: "))
            y = int(input("Enter 2nd Number: "))
            print("Addition is", x + y)

        case 2:
            x = int(input("Enter 1st Number: "))
            y = int(input("Enter 2nd Number: "))
            print("Subtraction is", x - y)

        case 3:
            x = int(input("Enter 1st Number: "))
            y = int(input("Enter 2nd Number: "))
            print("Multiplication is", x * y)

        case 4:
            sys.exit()

        case _:
            print("Invalid Input")