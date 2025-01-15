# file = open("taska.txt","a")
# file.write("hello! I have created the content!")
# file.close()
#
# file = open("task.txt","r")
# print(file.read())

# file= open("task.txt", "w")
# file.write("Woops! I have deleted the content!")
# file.close()
#
# file = open("task.txt", "r")

# print(file.read())

import os,sys

root_path = "D:/python/python-tasks/new-task15"

if not os.path.exists(root_path):
    os.mkdir(root_path)
    print("Given folder is not exists and I have created for you.")

# sys.exit()



for i in range(1,101):
    file_name="task"+str(i)+ ".py"
    file_path = root_path + "/" + file_name
    create_file(file_path)