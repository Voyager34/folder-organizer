# this is a comment
import os
import sys


user_folder = sys.argv[1]
print(f"Gonna organize this folder : {user_folder}")

list_files = os.listdir(user_folder)
print(f" Here.. All files in the directory: \n  {list_files}")


