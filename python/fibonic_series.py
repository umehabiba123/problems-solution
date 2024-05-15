def fibonic(a,b,lis):
    add = a + b
    if(add<=100):
        lis.append(add)
        return fibonic(b,add,lis)
    else:
        print(lis)

first = 0
second = 1
lis =[first,second]
fibonic(first,second,lis)


