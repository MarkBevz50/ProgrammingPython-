def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Приклад
n = 1
result = fibonacci_iterative(n)
print(f"{n}-те число Фібоначчі:", result)
def ideal(num=1):
    i = 1
    a = []
    while i ** 2 <= num:
        if num % i == 0:
            a.append(i)
            if i != num // i:
                a.append(num // i)
        i += 1
    a.sort()
    
    if sum(a) == num:
        return True
    return False 
    print(a)

ideal(6)
#Написати рограиу для переведення з двійкової, шістнадцяткової та вісімкової у десяткову
def binary(mybinary):
    decimal = 0
    for i in range(len(mybinary)):
        decimal += int(mybinary[i]) * (2 ** (len(mybinary) - 1 - i))
    return decimal

print(binary("1101"))  
def octal(myoctal):
    decimal = 0
    for i in range(len(myoctal)):
        decimal += int(myoctal[i]) * (8 ** (len(myoctal) - 1 - i))
    return decimal

print(octal("17"))  
def hexadecim(myhex):
    decimal = 0
    hexDigits = "0123456789ABCDEF"
    myhex = myhex.upper()
    
    for i in range(len(myhex)):
        decimal += hexDigits.index(myhex[i]) * (16 ** (len(myhex) - 1 - i))
    
    return decimal

print(hexadecim("1a")) 
def binary_to_octal(mybin):
    decimal = 0
    for i in range(len(mybin)):
        decimal += int(mybin[i]) * (2 ** (len(mybin) - 1 - i))

    if decimal == 0:
        return "0"
    
    octal_number = ""
    while decimal > 0:
        remainder = decimal % 8
        octal_number = str(remainder) + octal_number
        decimal //= 8
    
    return octal_number
binary_number = "101011"  
octal_number = binary_to_octal(binary_number)
print(f"Вісімкове число: {octal_number}")
   