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

