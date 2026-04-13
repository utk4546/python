a = int(input("Enter number A= "))
b = int(input("Enter number B= "))
c = int(input("Enter number C= "))
if a > b and a > c:
    print("A is largest")
elif a==b==c:
    print("a , b , c are eqal ")
elif b==c and b>a and c>a:
    print("b and c  is eqal and larger than a ")
elif b==a and b>c and a>c :
    print("a and b  is eqal and larger than c")
elif a==c and a>b and c>b :
    print("a and c  is eqal and larger than b")
elif b > c:
    print("B is largest")
else:
    print("c is largest")
