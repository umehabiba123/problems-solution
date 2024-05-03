def binary_to_decimal(binary):
    """
    Convert a binary number to its decimal equivalent.

    :param binary: Binary number as a string.
    :return: Decimal equivalent of the binary number.
    """
    decimal = 0
    power = 0
    for i in binary:
        if i=="1":
            decimal = decimal+(2**power)
            power+=1
        else:
            power+=1
    return decimal


while True:
    binary_number = input("Enter a binary number: ")
    print("Decimal equivalent:", binary_to_decimal(binary_number))
    a = int(input("if you want to exit enter 0 else enter 1 "))

    if a==0:
        break

