import os
from  pathlib import Path 

#for lines in file_read:
folder_path = Path(input(r"C:\Users\ANISH\Downloads\bbc\bbc")) #path will automatically concert forward or back slashes according to right operating system 

destination_path = Path(input(r"C:\Users\ANISH\Downloads\bbc_backup\destination_folder"))  # removing the path of file
if not os.path.exists(destination_path):
    os.makedirs(destination_path)
if os.path.isdir(folder_path):
    sub_folders_having_dir = [sub_folder for sub_folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, sub_folder))]
 # sub_folder = r"C:\Users\ANISH\Downloads\bbc\bbc" + 
    for category in sub_folders_having_dir :
        file_path = folder_path + "\\" + category
        list_of_files = os.listdir(file_path)
        file_path_split_array = file_path.split("\\")
        for one_file in list_of_files:
            source_filename = one_file
            destination_filename = file_path_split_array[len(file_path_split_array)-1] + "-" + source_filename
            destination_file_path = destination_path + "\\" +  destination_filename
            source_file_path = file_path + "\\" +  source_filename

            file_1 = open(source_file_path, encoding="utf-8")
            file_2 = open(destination_file_path , 'w')
            data = file_1.read()
            new_data = data.replace("\n", "")
            file_2.write(new_data)
else:
    print("you entered wrong file_path")
