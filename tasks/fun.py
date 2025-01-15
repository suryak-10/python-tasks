def add_num(a, b):
    # a=5
    # b=2
    return a+b


print(add_num(1, 5))
print(add_num(5, 7))
print(add_num(4, 7))
print(add_num(78, 5))


name1 = "surya Kumar"
name2 = "john B"
name3 = "sathish M"


def create_avatar_label(name:str):
    first_name, last_name = name.split(' ')
    return (first_name[0] + last_name[0]).upper()


print(create_avatar_label(name1))
print(create_avatar_label(name2))
print(create_avatar_label(name3))




print(create_avatar_label('Hello surya'))