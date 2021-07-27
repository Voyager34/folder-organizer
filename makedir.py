import os
import sys

create_folder = sys.argv[1]

answer = input(f"\nare you sure of creating a new directory named {create_folder},   Y  or  N ? ")
if answer == 'Y': # or 'yes' or 'Yes' or 'YES':
      print (f"\n new directory created : \n {create_folder}")
      new_folder = os.mkdir(create_folder)
else: 
     print ("\n No folder created! Always nice to be sure :D")



     
##print(f"\n Are you sure of creating a directrory named {create_folder}/n")
##print("Y  or  N  ??")

