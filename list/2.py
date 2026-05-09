li=[22,11,91,77,64,12,90,25,70]

count5 = 0
odd_count = 0

for i in li:

    if i % 5 == 0:
        count5 += 1

    if i % 2 != 0:
        odd_count += 1


if count5 > 2:

    new_list = []

    for i in li:
        if i % 5 != 0:
            new_list.append(i)

    li = new_list


if odd_count > 2:
    li[0] = li[0] + 10


print(li)