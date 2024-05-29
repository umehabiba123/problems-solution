def celsius_to_fahrenheit(celsius):
    return celsius*(9/5)+32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*(5/9)


number = int(input("Enter 0 for Celsius to fahrenheit and 1 for fahrenheit Celsius :"))
if number == 0:
    temprature_in_celsius = int(input("Enter temprature in Celsius : "))
    print("Temprature in fahrenheit is ",celsius_to_fahrenheit(temprature_in_celsius))
else:
    temprature_in_fahrenheit = int(input("Enter temprature in Fahrenheit : "))
    print("Temprature in Celsius is ",celsius_to_fahrenheit(temprature_in_fahrenheit))
