import numpy as np
import ctypes
arr = np.array([42], dtype=np.int32)

print(f"Value arr: {arr[0]}")
arr2 = [2]
# Отримуємо адресу масиву
address = arr.ctypes.data
print(f"Adress: {address}")

# Використовуємо ctypes для зміни значення за вказаною адресою
ptr = ctypes.cast(address, ctypes.POINTER(ctypes.c_int))
ptr.contents.value = 100

print(f"Value of arr after changes: {arr[0]}")
