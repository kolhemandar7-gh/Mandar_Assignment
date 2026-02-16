# Merge two sets of numbers; use intersection and union, print differences with loop.

# Define two sets of numbers
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# ---------------- UNION ----------------
union_set = set1.union(set2)
print("Union:", union_set)

# ---------------- UNION ----------------
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# ---------------- DIFFERENCE ----------------
difference_s1 = set1.difference(set2)
print("Elements in set1 but not in set2:")
for num in difference_s1:
    print(num)

difference_s2 = set2.difference(set1)
print("Elements in set2 but not in set1:")
for num in difference_s2:
    print(num)