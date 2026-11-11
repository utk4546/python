# MULTIPICATION TABLE PRINTER
# PROBLM-give the multiplication table upto 10 but skip the fifth iteration 

n=int(input("enter the number :"))

for i in range(1,11):
    if(i!=5):
        print(n,"x",i,"=" ,i*n)
        
        
#    USING continue KEYWORD     
# n=int(input("enter the number :"))

# for i in range(1,11):
#     if(i==5):
#         continue
    
#     print(n,"x",i,"=" ,i*n)
    
    
    