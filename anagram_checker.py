def anagram(string1,string2):
    if len(string1)!=len(string2):
        return False
    else:
        string1=string1.lower()
        string1=string2.lower()
                     # Convert strings to lists of characters
        list1=list(string1)     
        list2=list(string2)
                     # Sort the lists
        list1.sort()
        list2.sort()
                     #  check both strings are same
        if string1 == string2:
            
            return True
    
        
    
string1 = input("Enter the first word: ")
string2 = input("Enter the second word: ")
if anagram(string1,string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")






