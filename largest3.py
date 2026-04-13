a = int(input("Enter first A= "))
b = int(input("Enter second B= "))
c = int(input("Enter third C= "))
if a > b and a > c:
    print("A is largest")
elif b > c:
    print("B is largest")
else:
    print("C is largest")