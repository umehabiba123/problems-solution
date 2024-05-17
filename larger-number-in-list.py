def larger_number_in_list(lis):
    for i in range(len(lis)-1):
        if lis[i]>lis[i+1]:
            temp = lis[i]
            lis[i] = lis[i+1]
            lis[i+1] = temp
    return f"The greater number in list is {lis[i+1]}"

lis = [1,8,9,44,7,69,78,-9]
print(larger_number_in_list(lis))

    