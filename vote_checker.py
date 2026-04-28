while True:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible to vote ✅")
    else:
        print("You are not eligible to vote ❌")

    choice = input("Do you want to check again? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you!")
        break