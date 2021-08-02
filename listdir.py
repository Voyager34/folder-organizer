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

# HIDDEN FILE LIST
hidden_file_list = []
for file in list_files:
    if file.startswith("."):
        hidden_file_list.append(file)

print("HERE IS LIST OF HIDDEN FILES: \n")
print(hidden_file_list)
print(f"\n NO OF HIDDEN FILES : \n {len(hidden_file_list)}")

# NEW LIST WITHOUT HIDDEN FILES (USED LIST COMPREHENSION OR SOME S***)
updated_list = [x for x in list_files if x not in hidden_file_list]
print(f"\n UPDATED LIST WITHOUT HIDDEN FILES : \n {updated_list}")
print(f"\n NO OF FILES IN UPDATED LIST : \n {len(updated_list)}")

