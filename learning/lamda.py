'''r=lambda x,y:x+y


x=r(11,12)
print("addition is", x)'''


r=lambda n:1 if n==1 else n*r(n-1)


print("fatorial is = ",r(int(input("enter a number = "))))
