def vowel_counter(string):
    count = 0
    for i in string:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="o":
            count += 1
            
    return f"There are {count} vowel word in {string} "
print(vowel_counter("alif allah or insan"))