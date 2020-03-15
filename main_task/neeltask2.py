#import codecs
import os

#for lines in file_read:
folder_path = r"C:\Users\ANISH\Downloads\bbc\bbc"

category = "business"

file_path = folder_path + "\\" + category

list_of_files = os.listdir(file_path)
destination_path= r"C:\Users\ANISH\Downloads\bbc_backup\destination_folder"  # removing the path of file

file_path_split_array = file_path.split("\\")

for one_file in list_of_files:
    source_filename = one_file
    destination_filename = file_path_split_array[len(file_path_split_array)-1] + "-" + source_filename

    destination_file_path = destination_path + "\\" +  destination_filename
    source_file_path = file_path + "\\" +  source_filename

    with open(source_file_path, encoding="utf-8") as file_1 , open(destination_file_path , 'w') as file_2:
        data = file_1.read()
        new_data = data.replace("\n", "")
        file_2.write(new_data)
   
   
    
    
    



   

