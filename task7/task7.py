a = input()
list1 = a.split()
list2 = []
for items in list1:
    if items not in list2:
        list2.append(items)

print(" the duplicate items are " , str(list2))

