import os
import random

def create_test_folder(path, num_files=10, max_file_size=1024):
    if not os.path.exists(path):
        os.makedirs(path)

    for i in range(num_files):
        file_path = os.path.join(path, f"file_{i}.txt")
        size = random.randint(1, max_file_size * 2)
        with open(file_path, "wb") as f:
            f.write(os.urandom(size))

    print(f"Створено {num_files} файлів у папці {path}")

def delete_large_files(path, max_size):
    """Видаляє завеликі afqkb"""
    if not os.path.exists(path):
        print("Нема такого каталога.")
        return

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) > max_size:
                    os.remove(file_path)
                    print(f"Файл {file_path} видалено.")
            

def main():
    while True:
        print("1. Створити папку з файлами для тестування програми")
        print("2. Виконати завдання")
        print("3. Вийти")
        
        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            path = input("Введіть шлях до папки (за замовчуванням ./test_folder): ") or "./test_folder"
            num_files = int(input("Введіть кількість файлів (за замовчуванням 10): ") or 10)
            max_file_size = int(input("Введіть максимальний розмір файлу у байтах (за замовчуванням 1024): ") or 1024)
            create_test_folder(path, num_files, max_file_size)

        elif choice == "2":
            path = input("Введіть шлях до папки: ")
            if not os.path.exists(path):
                print("Вказана папка не існує. Спробуйте ще раз.")
                continue
            max_size = int(input("Введіть максимальний розмір файлу у байтах: "))
            delete_large_files(path, max_size)

        elif choice == "3":
            print("Вихід із програми.")
            break

        else:
            print("не правельний вибір. Спробуй ще раз.")

if __name__ == "__main__":
    main()
