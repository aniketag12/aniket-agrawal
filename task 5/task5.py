list_a = input()
list_b = input()
list1 = list_a.split()
list2 = list_b.split()
def common_elements():
    common_items = 0
    for number in list1:
        for numbers in list2:
            if list1.index(number) == list2.index(numbers):
                common_items+=1
        
    return (" the common items are ",common_items)
print(common_elements())

a = input()
list1 = a.split()
list2 = []
for items in list1:
    if items not in list2:
        list2.append(items)

print(" the duplicate items are " , str(list2))
