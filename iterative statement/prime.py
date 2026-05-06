x=int(input("enter the number to check ="));
for i in range(2,x):
    if x%i==0:
        print(x,"is not prime");
        break;
else:
    print(x,"is prime");
    