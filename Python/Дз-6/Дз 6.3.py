import csv
from datetime import datetime

# Завантаження даних із CSV-файлів
def load_computers(computers_file):
    computers = {}
    with open(computers_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            computer_id = int(row[0])
            brand = row[1]
            price = float(row[2])
            computers[computer_id] = {"brand": brand, "price": price}
    return computers

def load_operating_systems(os_file):
    os_data = {}
    with open(os_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            os_id = int(row[0])
            os_name = row[1]
            price = float(row[2])
            os_data[os_id] = {"os_name": os_name, "price": price}
    return os_data

def load_sales(sales_files):
    sales = []
    for file_name in sales_files:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                date = datetime.strptime(row[0], '%Y-%m-%d').date()
                computer_id = int(row[1])
                os_id = int(row[2])
                quantity = int(row[3])
                sales.append({
                    "date": date,
                    "computer_id": computer_id,
                    "os_id": os_id,
                    "quantity": quantity
                })
    return sales

# 1. Сумарна вартість проданої комп'ютерної техніки
def calculate_total_sales_value(computers, os_data, sales):
    total_value = 0
    for sale in sales:
        computer = computers[sale["computer_id"]]
        os = os_data[sale["os_id"]]
        sale_value = (computer["price"] + os["price"]) * sale["quantity"]
        total_value += sale_value
    return total_value

# 2. Вартість проданої комп'ютерної техніки для кожної марки
def calculate_sales_by_brand(computers, os_data, sales):
    sales_by_brand = {}
    for sale in sales:
        brand = computers[sale["computer_id"]]["brand"]
        os = os_data[sale["os_id"]]
        sale_value = (computers[sale["computer_id"]]["price"] + os["price"]) * sale["quantity"]
        if brand not in sales_by_brand:
            sales_by_brand[brand] = 0
        sales_by_brand[brand] += sale_value
    return sales_by_brand

# 3. Вартість проданої техніки для конкретної марки, окремо за ОС
def calculate_sales_by_os_for_brand(computers, os_data, sales, brand_input):
    sales_by_os = {}
    for sale in sales:
        computer = computers[sale["computer_id"]]
        if computer["brand"] == brand_input:
            os_name = os_data[sale["os_id"]]["os_name"]
            sale_value = (computer["price"] + os_data[sale["os_id"]]["price"]) * sale["quantity"]
            if os_name not in sales_by_os:
                sales_by_os[os_name] = 0
            sales_by_os[os_name] += sale_value
    return sales_by_os

# Приклад використання функцій
computers_file = 'computers.csv'
os_file = 'os.csv'
sales_files = ['sales1.csv', 'sales2.csv']

computers = load_computers(computers_file)
os_data = load_operating_systems(os_file)
sales = load_sales(sales_files)

# 1. Сумарна вартість продажів
total_sales_value = calculate_total_sales_value(computers, os_data, sales)
print("Сумарна вартість проданої техніки:", total_sales_value, "$")

# 2. Вартість продажів для кожної марки
sales_by_brand = calculate_sales_by_brand(computers, os_data, sales)
print("Вартість продажів для кожної марки:")
for brand, value in sales_by_brand.items():
    print(f"{brand}: {value} $")

# 3. Вартість продажів для конкретної марки за ОС
brand_input = input("Введіть марку: ")
sales_by_os_for_brand = calculate_sales_by_os_for_brand(computers, os_data, sales, brand_input)
print(f"Вартість продажів для марки {brand_input} за ОС:")
for os_name, value in sales_by_os_for_brand.items():
    print(f"{os_name}: {value} $")
