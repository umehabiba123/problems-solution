string='hellow 1234 hi 56657'
def filter_digit(b):
    # try:
        new_digit=""
        new_string=""
        for i in b:
            if i.isdigit():
                new_digit +=i
            else:
                new_string +=i
        return(new_digit , new_string)   
    #  except = Exception as error
    #     print(error)
d,s= filter_digit(string)
print(d,s)
print("hellow how are you...")
print('hi i am fine')

