
import os
import sys


user_folder = sys.argv[1]
print(f"\n Gonna organize this folder : \n {user_folder} \n")

list_files = os.listdir(user_folder)
print(f" Here.. All files in the directory: \n \n {list_files} \n ")

##Print no of files and folders in directory and commit push 
number_files = len(list_files)
print(f"Number of files in current directory : \n {number_files} \n")

##WTBD: Do not include hidden files in number_files


##WTBD 2 : New program : if directory is passed , make a new directory

