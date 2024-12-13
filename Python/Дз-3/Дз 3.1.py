def AlgSum(arr):
    sum = 0
    for i in range(len(arr)):
        if i >= 2 and (arr[i-1] == 10 or arr[i-2] == 10):
            sum += arr[i] * 2
        else:
            sum += arr[i]
    return sum

def Sum(array1, array2):
    sum1 = AlgSum(array1)
    sum2 = AlgSum(array2)
    
    if sum1 == sum2:
        return ("The sums of the arrays are equal", sum1)
    elif sum1 < sum2:
        return (sum2, array2)
    elif sum1 > sum2:
        return (sum1, array1)

a = [1, 2, 10, 3, 4, 5]
b = [1, 2, 10, 3, 4, 5]
с = [1, 2, 3, 10, 4, 2, 12]
d = [8, 10, 10]
e = [8, 10, 4, 5, 3]
print(Sum(d, e))
