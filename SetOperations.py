# Define two sets
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# Perform set operations
union_set = E | N  # Union
intersection_set = E & N  # Intersection
difference_set = E - N  # Difference (Elements in E but not in N)
symmetric_difference_set = E ^ N  # Symmetric Difference

# Print results
print("Union of E and N is", union_set)
print("Intersection of E and N is", intersection_set)
print("Difference of E and N is", difference_set)
print("Symmetric difference of E and N is", symmetric_difference_set)
