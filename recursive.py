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

# Partial and recursive functions
from functools import partial
def table(count,table_number):
    if count<=10:
        print(table_number,"*",count,"=",table_number*count)
        return tablee(count = count+1)
    else:
        breakpoint
tablee = partial (table,table_number=6)
tablee(1)

