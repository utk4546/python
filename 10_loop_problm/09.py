num = list(map(int, input("Enter numbers: ").split()))
utk=set()
# for i in numbers:
#     if numbers.count(i) > 1:
#         print("List contains duplicates")
#         break
# else:
#     print("All elements are unique")
for i in num :
    if i in utk:
        print("duplicate ",i)
        break
    else:
        utk.add(i)
print(utk) 