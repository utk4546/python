#   creating a set 

s={10,20,30,30,40}
s.add(60) 
#  it will add a element in set s 
s.remove(10)
# it will remove a element in set s 
s.discard(30)
# it will also delelte a element but if the element is not present it will be fine but remove() give an error 
print(s)
print(len(s))