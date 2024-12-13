from functools import wraps
from typing import get_type_hints
import time
import random

# Завдання a: Декоратор @type_check
# Перевіряє, чи типи аргументів функції відповідають заміткам
def type_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        hints = get_type_hints(func)
        all_args = kwargs.copy()
        all_args.update(zip(func.__code__.co_varnames, args))

        for arg_name, arg_type in hints.items():
            if arg_name in all_args and not isinstance(all_args[arg_name], arg_type):
                raise TypeError(f"Argument '{arg_name}' must be of type {arg_type.__name__}")

        return func(*args, **kwargs)
    return wrapper

@type_check
def concatenate(a: str, b: str) -> str:
    return a + b

# Виклик злощасні функції для перевірки @type_check
print("Завдання a: Декоратор @type_check")
print(concatenate("hello", "world"))  # Працює
#concatenate("hello", 123)  # Викине TypeError


# Завдання b: Декоратор @inject
# Автоматично створює об’єкт вказаного класу і підставляє його замість параметра
class DatabaseService:
    def fetch_data(self):
        return "Data from database"

def inject(**dependencies):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg_name, cls in dependencies.items():
                if arg_name not in kwargs:
                    kwargs[arg_name] = cls()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@inject(service=DatabaseService)
def get_data(service):
    return service.fetch_data()

# Виклик функції для перевірки @inject
print("\nЗавдання b: Декоратор @inject")
print(get_data())  # Виведе "Data from database"


# Завдання c: Декоратор @trace_recursion
# Рахує кількість рекурсивних викликів функції
def trace_recursion(func):
    func.recursion_count = 0  # Змінна для підрахунку поточних рекурсивних викликів
    func.total_calls = 0  # Змінна для зберігання загальної кількості рекурсій

    @wraps(func)
    def wrapper(*args, **kwargs):
        func.recursion_count += 1
        func.total_calls += 1
        result = func(*args, **kwargs)
        func.recursion_count -= 1

        if func.recursion_count == 0:  # Повернення з найглибшої рекурсії
            print(f"Total recursive calls: {func.total_calls}")
            func.total_calls = 0  # Скидаємо після завершення всіх рекурсивних викликів

        return result
    return wrapper

@trace_recursion
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

# Виклик функції для перевірки @trace_recursion
print("\nЗавдання c: Декоратор @trace_recursion")
print(f"Factorial of 6 is {factorial(6)}")  # Виведе значення факторіалу і правильну кількість рекурсійних викликів


# Завдання d: Декоратор @rate_limiter
# Обмежує кількість викликів функції за певний період
def rate_limiter(max_calls, time_window):
    def decorator(func):
        calls = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            current_time = time.time()
            calls = [call for call in calls if current_time - call < time_window]

            if len(calls) < max_calls:
                calls.append(current_time)
                return func(*args, **kwargs)
            else:
                print("Rate limit exceeded, please wait.")

        return wrapper
    return decorator

@rate_limiter(max_calls=5, time_window=60)
def api_call():
    print("API called")

# Виклики функції для перевірки @rate_limiter
print("\nЗавдання d: Декоратор @rate_limiter")
for _ in range(7):
    api_call()
    time.sleep(10)


# Завдання e: Мій декоратор @timer
# Вимірює та виводить час виконання функції
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def sort_large_array():
    # Створення великого масиву з 1,000,000 випадкових чисел
    large_array = [random.randint(0, 10000000) for _ in range(10000000)]
    # Сортування масиву
    large_array.sort()
    return "Sorting completed"

# Виклик функції для перевірки часу сортування
print(sort_large_array())