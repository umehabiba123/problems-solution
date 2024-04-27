def string_palindrome(string):
    a=len(string)-1
    reverse = ""
#  loop to take reverse value
    while a>=0:
        reverse = reverse + string[a]
        a=a-1
# compare to check palindrome or not
    if string==reverse:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")
string_palindrome("abba")
