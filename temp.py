# primes = {1, 2, 3, 5, 7, 11}
# odds = {1, 3, 5, 7, 9, 11}
# threes = {1, 3, 6, 9, 12}


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

set1 = s1 | s2
set2 = s2 | s3

print(set1.symmetric_difference(set2))
print(set1 ^ set2)
# print(primes | odds)
# print(threes | odds)