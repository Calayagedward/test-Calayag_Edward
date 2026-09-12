import os
import shutil
# os.path.exists()
# os.mkdir("newdir")

# var1 = 'randomfile.zip'
# var2 = 'slides.pptx'
# var3 = 'ward.txt'
# var4 = 'oww.png'

# list_of_file = os.listdir()
# print(list_of_file)

store =input("Enter your Folder/File/Path: ")
if os.path.exists(store):
    print("The Folder/File/Path is real!")
    print("")
    print("All folders & files:", os.listdir())

    enter = input("Please enter a Path/Folder/File: ")

    path = os.path.join(os.path.join
                        ,enter)
    print(path)
else:
    print("Errorrrrrr! Don't continue!")