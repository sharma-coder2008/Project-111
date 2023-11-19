import os
import shutil

from_dir = "C:/Users/HP/Downloads/Source_Folder"
to_dir = "C:/Users/HP/Downloads/Destination"

list_of_files = os.listdir(from_dir)
print(list_of_files)

#Step 1 :
for file_name in list_of_files :
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)

#Step 2 :
    if extension == "" :
        continue
    if extension in[".gif",".jpg",".jpeg",".png",".jfif",".avif"] :
        path1 = from_dir+"/"+file_name
        path2 = to_dir+"/"+"Image_Files"
        path3 = to_dir+"/"+"Image_Files"+"/"+file_name

#Step 3 :
        if os.path.exists(path2) :
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            shutil.move(path1,path3)

#Extra Practice
    if extension in[".pdf"] :
        path1 = from_dir+"/"+file_name
        path2 = to_dir+"/"+"PDF_FILES"
        path3 = to_dir+"/"+"PDF_FILES"+"/"+file_name

        if os.path.exists(path2) :
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            shutil.move(path1,path3)    