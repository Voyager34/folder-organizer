import os
import sys

create_folder = sys.argv[1]

if create_folder == "--help":
    print("HERE IS HELP MENU BELOW:: HAVE FUN LOSER!!\n")
    print(" 1. PASS DIRECTORY AS 1ST ARGUMENT \n 2. SIT BACK AND RELAX \n ")
    quit()


answer = input(
    f"Are you sure of creating a new directory named {create_folder},  Y  or  N ?"
)


if answer[0].lower() == "y":
    print(f"\n New directory created : {create_folder}")
    new_folder = os.mkdir(create_folder)

else:
    print("\nNo folder created! Always nice to be sure :D")
