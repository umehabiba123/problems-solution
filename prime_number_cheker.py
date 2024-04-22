def primeNumber(number):
    i= 2
    while i<number:
        if number%i == 0:   
            print(number," is not a Prime number.")
            break
        else:
            i+=1
    if number == i and number ==2:
        print(number," is a Prime number.")
    
primeNumber(29)
      

