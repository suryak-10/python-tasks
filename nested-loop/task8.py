# Task 8: Flatten a 2D List
# Sample Input:
#     List: [[1, 2], [3, 4]]
# Expected Output:
#     Flattened List: [1, 2, 3, 4]


list1=[[1,2],[3,4]]
flat_list=sum(list1,[])
print(flat_list)


# import itertools
# my_list=[[1,2],[3,4]]
# flat_list=list(itertools.chain(*my_list))
# print(flat_list)