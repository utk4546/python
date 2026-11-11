# SUM OF EVEN NUMBERS
# PROBLEM- CALCLUATE THE SUM OF EVEN NUMBER UP TO GIVEN NUMBERN N 

n=int(input("enter the number upto to want to calculate even sum :"))
even_sum=0

for i in range(1,n+1):
    if(i%2==0):
        even_sum=even_sum+i
print(even_sum)
    
        
        
    
      