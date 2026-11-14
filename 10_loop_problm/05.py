
   
# FIND THE FIRST NON-REPEATING CHARACTER
# PROBLEM: Find the first non-repeating character from a given string.

utk = input("Enter the string: ")

for i in utk:
    if utk.count(i) == 1:
        print(i)
        break

else:
    print("No non-repeating character found")
