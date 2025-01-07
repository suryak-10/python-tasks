file = open("taska.txt","a")
file.write("hello! I have created the content!")
file.close()

file = open("task.txt","r")
print(file.read())

# file= open("task.txt", "w")
# file.write("Woops! I have deleted the content!")
# file.close()
#
# file = open("task.txt", "r")
# print(file.read())