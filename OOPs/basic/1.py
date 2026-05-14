
class Student:

    college_name = "BGIEM"      # static variable

    def __init__(self, name, roll_number):
        self.name = name       # instance variable
        self.roll_number=roll_number


s1 = Student("Utkarsh", 355)
s2 = Student("pushpa", 255)
s3 = Student("samrth",283 )

print("name = ",s1.name,"\nroll number = ",end="")
print(s1.roll_number)
print( "name = ",s2.name,"\nroll number = ",end="")
print(s2.roll_number)
print("name = ",s3.name  ,"\nroll number = ",end="")
print(s3.roll_number)
print("college name = ",Student.college_name)
