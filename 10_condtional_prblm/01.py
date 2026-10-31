# AGE GROUP CATEGARIZATON 
# Less than 13 is Child
# 13-19 teenager
# 20-59 adult
# 60+ senor


age=int(input("enter the age - "))
if(age<0):
     print("invalid")
else:
    if age<13:
         print("he/she is child")
    elif 19>age>12:
         print("he/she is teenager")
    elif  19<age<60:
         print("he/she is adult")
    else:
         print("he/she is senior")
