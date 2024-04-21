# convert temprature in fahrenheit
celsius=input("Enter temprature in celsius ")

celsius=int(celsius)
fahrenheit=celsius*(9/5)+32
print("Temprature in fahrenheit is ",fahrenheit)

# print your name that assign to a variable
a = "Habiba Chaudhry"
print(a)

# print the name five time in new line
print ("My name")
for i in range(5):
    print(a,"\n")

x=7
print(a*x ,'\n')


#  if else statement
if(fahrenheit>90):
    print('it\'s too hot')
elif(fahrenheit>70):
    print("it\'s cool ..")
else:
    print("it\'s just fine")

# guess number program
number=10
guess =input("Enter a number between 1 & 20 =")
guess =int(guess)
if(guess==number):
    print("Congrats! you guess correct number")
elif(guess<number):
    print('No, Try a little higher')
else:
    print('No, Try a little lower')


    




