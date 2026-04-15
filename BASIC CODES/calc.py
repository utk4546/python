x=float(input("enter value = "))
y=float(input("enter value = "))
print("choose an option ")
print("1 for addition")
print("2 for subtraction")
print("3 for multiply")
print("4 for divide")
z=float(input("enter choice = "))
if z==1:
    print("additon of",x,"and",y,"is =",x+y)
elif z==2:
     print("subtraction of",x,"and",y,"is =",x-y)
elif z==3:
     print("multiplication of",x,"and",y,"is =",x*y)
elif z==4:
    if y==0:
         print("division is not possible")
    else:
         print("division of",x,"and",y,"is =",x/y)
else:
     print("invalid choice")        


    
    