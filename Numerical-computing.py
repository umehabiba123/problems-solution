import numpy as np

def dot_product(array1, array2):
    # Check if the arrays have compatible shapes for dot product
    if array1.shape != array2.shape:
        return "Arrays must have the same shape for dot product."
    
    # Calculate dot product
    result = np.dot(array1, array2)
    return result

# Example usage:
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print("Dot product:", dot_product(array1,  array2))