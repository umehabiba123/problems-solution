# def del_key(*target):
#     a= {
#         'a':"a",
#         'b': {
#             'c':"c",
#             'd':"d",
#             'e':"e",
    
#             },
#         'f':"f"
#       }
#     print(a)
#     for target in target:
#         a.pop(target)
#         print(a)

# del_key("f",{'b':"c"})


    
# del_key('c')
def del_key(actual,target,required):
    print(actual)
    try:
        if isinstance(target,dict):
            d = set(target.keys())-set(required)
        for i in d:
            target.pop(i)
    
        return actual
    except:
        print("something wrong")


a= {
        'a':"a",
        'b': {
            'c':"c",
            'd':"d",
            'e':"e",
            'g': {
                'h':"h",
                'j':"j"
                
            },
    
            },
        'f':"f"
      }
a = [3,7,8,{'c':"c",
            'd':"d",
            'e':"e",}]

# print(del_key(a,a['b']['g'],{'j'}))
# print(del_key(a,a,{'f'}))
if isinstance(a,dict):
    print(del_key(a,a['b']['g'],{'j'}))
else:

    for i in a:
        if isinstance(i,dict):
            index=a.index(i)
            print(i)
            
            print(del_key(a[index],a[index],{'e'}))
            print(index)
        else:
            if isinstance(i,tuple or set or list):
                print("hellow")
