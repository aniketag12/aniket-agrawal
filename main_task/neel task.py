#import codecs

#for lines in file_read:
filename = r"C:\Users\ANISH\Downloads\bbc\bbc\business\001.txt"
destination_file = r"C:\Users\ANISH\Downloads\bbc_backup\destination_folder\destination_file.txt"

with open(filename, encoding="utf-8") as file_1 , open(destination_file , 'a') as file_2:
    data = file_1.read()
    new_data = data.replace("\n", "")
    file_2.write(new_data)
    
    



   

