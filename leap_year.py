def leap_year(year):
    if(year%4==0):
        print(year," is a leap year.")
    else:
        print(year," is not a leap year.")
        return 0
leap_year(2022)