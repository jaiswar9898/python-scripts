#In this script we will see how to create folders using Python and manipulate them!

#mkdir allow to create folder 

import os 

path = r"C:\Users\admin\main\newfolder"
file_name = 'revenue.txt'
try:
    os.mkdir(path)
    print("folder created")
    # Creating a file at specified folder
    # join directory and file path
    with open(os.path.join(path, file_name), 'w') as fp:
    # uncomment below line if you want to create an empty file
       fp.write('This is a new line')
       
except FileExistsError:
    print("folder already exist")







