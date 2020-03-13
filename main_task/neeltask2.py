#import codecs

#for lines in file_read:
file_path = r"C:\Users\ANISH\Downloads\bbc\bbc\business\001.txt"
destination_path = r"C:\Users\ANISH\Downloads\bbc_backup\destination_folder"  # removing the path of file
file_path_split_array = file_path.split("\\")
source_filename = file_path_split_array[len(file_path_split_array)-1]
destination_filename = file_path_split_array[len(file_path_split_array)-2] + "-" + source_filename
destination_file_path = destination_path + "\\" +  destination_filename
with open(file_path, encoding="utf-8") as file_1 , open(destination_file_path , 'w') as file_2:
    data = file_1.read()
    new_data = data.replace("\n", "")
    file_2.write(new_data)
   
   
    
    
    



   

