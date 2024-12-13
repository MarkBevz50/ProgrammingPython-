def add_strings(num1, num2):
    # Handle signs
    if num1[0] == '-' and num2[0] != '-':
        return subtract_strings(num2, num1[1:])
    elif num1[0] != '-' and num2[0] == '-':
        return subtract_strings(num1, num2[1:])
    elif num1[0] == '-' and num2[0] == '-':
        return '-' + add_strings(num1[1:], num2[1:])
    
    # Make both strings the same length
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    carry = 0
    result = []
    
    # Start adding from the last digit
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))
    
    # If there's a remaining carry
    if carry:
        result.append(str(carry))
    
    return ''.join(result[::-1])

def subtract_strings(num1, num2):
    # Determine if the result will be negative
    if num1[0] == '-' and num2[0] != '-':
        return '-' + add_strings(num1[1:], num2)
    elif num1[0] != '-' and num2[0] == '-':
        return add_strings(num1, num2[1:])
    elif num1[0] == '-' and num2[0] == '-':
        return subtract_strings(num2[1:], num1[1:])
    
    # Ensure num1 >= num2 for simplicity
    if compare_strings(num1, num2) == -1:
        return '-' + subtract_strings(num2, num1)
    
    # Make both strings the same length
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    result = []
    borrow = 0
    
    # Start subtracting from the last digit
    for i in range(max_len - 1, -1, -1):
        diff = int(num1[i]) - int(num2[i]) - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(diff))
    
    # Remove leading zeros
    while result and result[-1] == '0':
        result.pop()
    
    return ''.join(result[::-1]) or '0'

def multiply_strings(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    
    # Handle signs
    sign = ''
    if num1[0] == '-' and num2[0] != '-':
        sign = '-'
        num1 = num1[1:]
    elif num1[0] != '-' and num2[0] == '-':
        sign = '-'
        num2 = num2[1:]
    elif num1[0] == '-' and num2[0] == '-':
        num1 = num1[1:]
        num2 = num2[1:]
    
    # Reverse both strings
    num1, num2 = num1[::-1], num2[::-1]
    
    # Initialize result array
    result = [0] * (len(num1) + len(num2))
    
    # Multiply each digit
    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += int(num1[i]) * int(num2[j])
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    # Remove leading zeros and reverse
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    return sign + ''.join(map(str, result[::-1]))

def divide_strings(dividend, divisor):
    if divisor == '0':
        return "Undefined"  # Division by zero
    
    # Handle signs
    sign = ''
    if dividend[0] == '-' and divisor[0] != '-':
        sign = '-'
        dividend = dividend[1:]
    elif dividend[0] != '-' and divisor[0] == '-':
        sign = '-'
        divisor = divisor[1:]
    elif dividend[0] == '-' and divisor[0] == '-':
        dividend = dividend[1:]
        divisor = divisor[1:]
    
    # Initialize quotient and remainder
    quotient = ''
    remainder = '0'
    
    for digit in dividend:
        remainder = add_strings(multiply_strings(remainder, '10'), digit)
        count = 0
        while compare_strings(remainder, divisor) >= 0:
            remainder = subtract_strings(remainder, divisor)
            count += 1
        quotient += str(count)
    
    # Remove leading zeros from quotient
    quotient = quotient.lstrip('0') or '0'
    
    return sign + quotient

def compare_strings(num1, num2):
    # Remove leading zeros
    num1 = num1.lstrip('0')
    num2 = num2.lstrip('0')
    
    # Compare lengths
    if len(num1) > len(num2):
        return 1
    elif len(num1) < len(num2):
        return -1
    
    # Compare digit by digit
    for i in range(len(num1)):
        if num1[i] > num2[i]:
            return 1
        elif num1[i] < num2[i]:
            return -1
    
    return 0  # Both numbers are equal

num1 = "100"
num2 = "11"
print(divide_strings(num1, num2))
