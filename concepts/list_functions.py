def list_group_by_even(acc, element):
    if element % 2 == 0:
        acc['even'].append(element)
    else:
        acc['odd'].append(element)
    return acc

def square(acc:list, element):
    acc.append(element ** 2)
    return acc

def list_total(acc:int, num):
    acc += num
    return acc