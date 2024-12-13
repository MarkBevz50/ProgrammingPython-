# Клас Автомобіль
import csv

class Car:
    def __init__(self, car_number, brand, year):
        self.car_number = car_number  # Номер автомобіля
        self.brand = brand  # Марка автомобіля
        self.year = year  # Рік випуску

class Operation:
    def __init__(self, operation_number, name, price):
        self.operation_number = operation_number  # Номер операції
        self.name = name  # Назва операції
        self.price = price  # Вартість операції

class OperationWithPartReplacement(Operation):
    def __init__(self, operation_number, name, price, part_price):
        super().__init__(operation_number, name, price)
        self.part_price = part_price  # Вартість деталі

class Receipt:
    def __init__(self, car, operation, part_count=0):
        self.car = car  # Автомобіль
        self.operation = operation  # Операція
        self.part_count = part_count  # Кількість замінених деталей (за замовчуванням 0)

    def total_cost(self):
        if isinstance(self.operation, OperationWithPartReplacement):
            return self.operation.price + self.operation.part_price * self.part_count
        else:
            return self.operation.price

class AutoService:
    def __init__(self):
        self.receipts = []
        self.cars = {}

    def load_cars(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаємо заголовок
            for row in reader:
                car_number, brand, year = row
                self.cars[car_number] = Car(car_number, brand, int(year))

    def load_operations(self, filename, with_parts=False):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаємо заголовок
            for row in reader:
                car_number, operation_number, name, price, *rest = row
                price = float(price)
                if with_parts:
                    part_price = float(rest[0])
                    part_count = int(rest[1])
                    operation = OperationWithPartReplacement(operation_number, name, price, part_price)
                    self.receipts.append(Receipt(self.cars[car_number], operation, part_count))
                else:
                    operation = Operation(operation_number, name, price)
                    self.receipts.append(Receipt(self.cars[car_number], operation))

    def add_receipt(self, receipt):
        self.receipts.append(receipt)

    def total_payment(self):
        return sum(receipt.total_cost() for receipt in self.receipts)

    def payment_per_operation(self):
        operation_totals = {}
        for receipt in self.receipts:
            operation = receipt.operation.name
            if operation not in operation_totals:
                operation_totals[operation] = 0
            operation_totals[operation] += receipt.total_cost()
        return operation_totals

    def car_count_per_operation(self, operation_name):
        car_brands = {}
        for receipt in self.receipts:
            if receipt.operation.name == operation_name:
                brand = receipt.car.brand
                if brand not in car_brands:
                    car_brands[brand] = 0
                car_brands[brand] += 1
        return car_brands

    def car_count_for_all_operations(self):
        operation_car_count = {}
        for receipt in self.receipts:
            operation_name = receipt.operation.name
            if operation_name not in operation_car_count:
                operation_car_count[operation_name] = {}
            brand = receipt.car.brand
            if brand not in operation_car_count[operation_name]:
                operation_car_count[operation_name][brand] = 0
            operation_car_count[operation_name][brand] += 1
        return operation_car_count
    
auto_service = AutoService()

# Завантажуємо автомобілі
auto_service.load_cars('cars.csv')

# Завантажуємо операції без заміни деталей
auto_service.load_operations('operations_without_parts.csv', with_parts=False)

# Завантажуємо операції із заміною деталей
auto_service.load_operations('operations_with_parts.csv', with_parts=True)

# Виведення результатів

# 1. Сумарна оплата за всі операції
print(f"Сумарна оплата за всі операції: {auto_service.total_payment()} грн")

# 2. Сумарні оплати по кожній операції
print("Сумарні оплати по кожній операції:")
for operation, total in auto_service.payment_per_operation().items():
    print(f"{operation}: {total} грн")

# 3. Кількість автомобілів для кожної операції по марках
print("Кількість автомобілів для кожної операції по марках:")
for operation, brands in auto_service.car_count_for_all_operations().items():
    print(f"Операція: {operation}")
    for brand, count in brands.items():
        print(f"  {brand}: {count} автомобілі(в)")