def find_missing_numbers(lst):
    n = len(lst) + 1
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    list_sum = sum(lst)
    missing_numbers = []
    for i in range(1, n + 1):
        if i not in lst:
            missing_numbers.append(i)
    return missing_numbers

lst = [1, 2, 4, 6]
print("The missing numbers are:", find_missing_numbers(lst))




