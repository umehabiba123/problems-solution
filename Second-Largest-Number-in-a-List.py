import numpy as np
def second_largest(numbers):
    sorted_list = np.sort(numbers)
    index = len(numbers)-2
    return sorted_list[index]

print("Second Largest Number in List is :",second_largest([3,4,6,2,9,55]))
print("Second Largest Number in List is :",second_largest([3,4,66,2,79,55]))