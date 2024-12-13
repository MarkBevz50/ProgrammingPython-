number1 = "1000"
number2 = "1000"

def binary(mybinary):
    decimal = 0
    for i in range(len(mybinary)):
        decimal += int(mybinary[i]) * (2 ** (len(mybinary) - 1 - i))
    return decimal
def dec_to_bin(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary if binary else "0"
def add_two_binary(bin1, bin2):
    first_num = binary(bin1)
    second_num = binary(bin2)
    return dec_to_bin(first_num + second_num)

Sum = add_two_binary(number1, number2)
print("The sum is: ",Sum, '(',binary(Sum),')')

def mult_two_binary(bin1, bin2):
    first_num = binary(bin1)
    second_num = binary(bin2)
    return dec_to_bin(first_num * second_num)

Prod = mult_two_binary(number1, number2)
print("The product is: ",Prod,'(',binary(Prod),')')

def sub_two_binary(bin1, bin2):
    first_num = binary(bin1)
    second_num = binary(bin2)
    return dec_to_bin(first_num - second_num)

Diff = sub_two_binary(number2, number1 )
print("The difference is: ",Diff,'(',binary(Diff),')')