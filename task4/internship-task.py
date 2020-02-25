s = input("enter your context:")
list_of_sentences = s.split()
list_of_words_wo_e = []
def has_no_e():
    for word in list_of_sentences:
        if "e"  not in word:
            list_of_words_wo_e.append(word)
    return list_of_words_wo_e
#retun will just stop the program execution 
print(has_no_e())
percentage = (len(list_of_words_wo_e)/len(list_of_sentences))*100;
print("the percentage of no e words are: " + str(percentage) + "%")

