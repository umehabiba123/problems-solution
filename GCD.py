def greater_common_divisor(num1,num2):
    max_num = max(num1,num2)
    max_num = int(max_num/2)
    i=max_num
    while i>0:
        
        if num1%i==0 and num2%i==0:
            return i
        i-=1
    
while True:
    num1 = int(input("Enter 1st number :"))
    num2 = int(input("Enter 2nd number :"))
    print(f"Greaater common divisor of {num1} and {num2} is",greater_common_divisor(num1,num2))

    a = int(input("if you want to exit enter 0 else enter 1 "))
    if a==0:
        break

