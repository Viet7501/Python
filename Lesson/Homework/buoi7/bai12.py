set1 = {0, 1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9, 0, 1}

# set1.difference_update(set2)
# set1.intersection_update(set2)
print(set1.issubset(set2))
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
set1.symmetric_difference_update(set2)

print(set1)
