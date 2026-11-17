# find factorial of a number using while loop 
utk=int(input("enter the number: "))
fact=1

while utk>0:
    fact=fact*utk
    utk=utk-1
    
print("the factorial of the number is = ",fact)