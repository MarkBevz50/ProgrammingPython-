
'''У вікі є формула для P_n+1, я її просто привів до вигляду P_n'''
def Legander_Poly(n,x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * Legander_Poly(n - 1, x) - (n - 1) * Legander_Poly(n - 2, x)) / n 

    # Тест програми
n = int(input("Введіть степінь полінома Лежандра (n): "))
x = float(input("Введіть значення x: "))
result = Legander_Poly(n, x)
print(f"P_{n}({x}) = {result}") 