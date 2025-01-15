def create_file(path:str):
    file = open(path, "w")
    file.write("#hello! I have created the content!")
    file.close()


create_file('surya.txt')
create_file('surya1.txt')