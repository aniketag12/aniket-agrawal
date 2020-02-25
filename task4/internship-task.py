
s = input("enter your context:")
n_list = s.split()
other_list = []
def has_no_e():
    for i in n_list:
        if "e"  not in i:
            return other_list.append(i)
        
print(has_no_e())

print("the percentage of no e words are :" , (len(other_list)/len(n_list))*100)
        



