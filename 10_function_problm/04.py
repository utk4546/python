import math

def circle_stats(r):
     area=math.pi*r**2  
     circumference=2*math.pi*r   
     return area,circumference

a,c=circle_stats(1)

print("area of the cicle = ",a)
print("circumference of the circle= ",c)