import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict
import csv


# Клас FurnitureComponent з валідацією
class FurnitureComponent:
    def __init__(self, id, name, material, price):
        self._id = id
        self._name = name
        self._material = material
        self._price = price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID повинен бути цілим числом і більшим за нуль.")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Назва компоненту повинна бути непорожнім рядком.")
        self._name = value.strip()

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Матеріал компоненту повинен бути непорожнім рядком.")
        self._material = value.strip()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Ціна повинна бути числом більшим за нуль.")
        self._price = value


class FurnitureCategory:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID категорії повинно бути цілим числом і більшим за нуль.")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Назва категорії повинна бути непорожнім рядком.")
        self._name = value.strip()


class Furniture:
    def __init__(self, order_number, category, name):
        if not isinstance(category, FurnitureCategory):
            raise TypeError("category must be an instance of FurnitureCategory")
        self._order_number = order_number
        self._category = category
        self._name = name

    @property
    def order_number(self):
        return self._order_number

    @order_number.setter
    def order_number(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Номер замовлення повинен бути цілим числом і більшим за нуль.")
        self._order_number = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, FurnitureCategory):
            raise TypeError("Категорія повинна бути об'єктом класу FurnitureCategory.")
        self._category = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Назва меблів повинна бути непорожнім рядком.")
        self._name = value.strip()

class Assembling:
    def __init__(self, assembling_date, order_number, component, status="In Process"):
        if not isinstance(component, FurnitureComponent):
            raise TypeError("component must be an instance of FurnitureComponent")
        self._assembling_date = assembling_date
        self._order_number = order_number
        self._component = component
        self._status = status

    @property
    def assembling_date(self):
        return self._assembling_date

    @assembling_date.setter
    def assembling_date(self, value):
        try:
            self._assembling_date = datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата збирання повинна бути в форматі 'РРРР-ММ-ДД'.")

    @property
    def order_number(self):
        return self._order_number

    @order_number.setter
    def order_number(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Номер замовлення повинен бути цілим числом і більшим за нуль.")
        self._order_number = value

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, value):
        if not isinstance(value, FurnitureComponent):
            raise TypeError("Компонент має бути екземпляром класу FurnitureComponent.")
        self._component = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ["In Process", "Completed", "Cancelled"]:
            raise ValueError("Статус може бути лише 'In Process', 'Completed' або 'Cancelled'.")
        self._status = value


# Запис даних у CSV
def write_csv(filename, fieldnames, data):
    """Функція запису даних у CSV файл."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
# Завантаження даних
components_data = [
    {"id": 1, "name": "Screw", "material": "Metal", "price": 0.5},
    {"id": 2, "name": "Wood Panel", "material": "Wood", "price": 10.0},
    {"id": 3, "name": "Glass", "material": "Glass", "price": 25.0},
    {"id": 4, "name": "Hinge", "material": "Metal", "price": 2.5},
    {"id": 5, "name": "Plastic Cap", "material": "Plastic", "price": 1.0},
    {"id": 6, "name": "Leg", "material": "Wood", "price": 15.0},
    {"id": 7, "name": "Fabric", "material": "Fabric", "price": 12.0},
    {"id": 8, "name": "Seat Cushion", "material": "Foam", "price": 8.0},
    {"id": 9, "name": "Metal Frame", "material": "Metal", "price": 20.0},
    {"id": 10, "name": "Drawer", "material": "Wood", "price": 30.0},
    {"id": 11, "name": "Glass Top", "material": "Glass", "price": 40.0},
    {"id": 12, "name": "Armrest", "material": "Wood", "price": 7.0},
    {"id": 13, "name": "Table Leg", "material": "Metal", "price": 18.0},
    {"id": 14, "name": "Backrest", "material": "Fabric", "price": 9.0},
    {"id": 15, "name": "Cushion Cover", "material": "Cotton", "price": 5.0},
    {"id": 16, "name": "Nail", "material": "Steel", "price": 0.25},
    {"id": 17, "name": "Wire", "material": "Cooper", "price": 2.0},
]

categories_data = [
    {"id": 1, "name": "Chairs"},
    {"id": 2, "name": "Tables"},
    {"id": 3, "name": "Sofas"},
    {"id": 4, "name": "Storage Units"},
    {"id": 5, "name": "Beds"},
]

orders_data = [
    {"order_number": 101, "category_id": 1, "name": "Office Chair"},
    {"order_number": 102, "category_id": 2, "name": "Dining Table"},
    {"order_number": 103, "category_id": 3, "name": "Leather Sofa"},
    {"order_number": 104, "category_id": 4, "name": "Wooden Cabinet"},
    {"order_number": 105, "category_id": 5, "name": "King Size Bed"},
    {"order_number": 106, "category_id": 2, "name": "Coffee Table"},
    {"order_number": 107, "category_id": 1, "name": "Ergonomic Chair"},
    {"order_number": 108, "category_id": 3, "name": "Corner Sofa"},
]

assembling_data = [
    {"assembling_date": "2024-11-20", "order_number": 101, "id_component": 1, "status": "Completed"},
    {"assembling_date": "2024-11-20", "order_number": 101, "id_component": 2, "status": "Completed"},
    {"assembling_date": "2024-11-20", "order_number": 101, "id_component": 3, "status": "Completed"},
    {"assembling_date": "2024-11-21", "order_number": 102, "id_component": 4, "status": "Completed"},
    {"assembling_date": "2024-11-21", "order_number": 102, "id_component": 5, "status": "In Process"},
    {"assembling_date": "2024-11-22", "order_number": 103, "id_component": 6, "status": "Completed"},
    {"assembling_date": "2024-11-22", "order_number": 103, "id_component": 7, "status": "Completed"},
    {"assembling_date": "2024-11-23", "order_number": 104, "id_component": 8, "status": "In Process"},
    {"assembling_date": "2024-11-23", "order_number": 104, "id_component": 9, "status": "In Process"},
    {"assembling_date": "2024-11-24", "order_number": 105, "id_component": 10, "status": "Completed"},
    {"assembling_date": "2024-11-25", "order_number": 106, "id_component": 11, "status": "Completed"},
    {"assembling_date": "2024-11-26", "order_number": 107, "id_component": 12, "status": "In Process"},
    {"assembling_date": "2024-11-26", "order_number": 107, "id_component": 13, "status": "Completed"},
    {"assembling_date": "2024-11-27", "order_number": 108, "id_component": 14, "status": "Completed"},
    {"assembling_date": "2024-11-27", "order_number": 108, "id_component": 15, "status": "Completed"},
    {"assembling_date": "2024-11-28", "order_number": 103, "id_component": 9, "status": "Completed"},
    {"assembling_date": "2024-11-28", "order_number": 105, "id_component": 7, "status": "In Process"},
]
# Запис даних у CSV
write_csv('components.csv', ["id", "name", "material", "price"], components_data)
write_csv('categories.csv', ["id", "name"], categories_data)
write_csv('orders.csv', ["order_number", "category_id", "name"], orders_data)
write_csv('assembling.csv', ["assembling_date", "order_number", "id_component", "status"], assembling_data)

# Завантаження даних з CSV
components_df = pd.read_csv("components.csv")
categories_df = pd.read_csv("categories.csv")
orders_df = pd.read_csv("orders.csv")
assembling_df = pd.read_csv("assembling.csv")

# Створення об'єктів
components = [FurnitureComponent(**row) for _, row in components_df.iterrows()]
categories = [FurnitureCategory(**row) for _, row in categories_df.iterrows()]
orders = [
    Furniture(
        row["order_number"],
        next(cat for cat in categories if cat.id == row["category_id"]),
        row["name"]
    ) for _, row in orders_df.iterrows()
]
assemblings = [
    Assembling(
        row["assembling_date"],
        row["order_number"],
        next(comp for comp in components if comp.id == row["id_component"]),
        row["status"]
    ) for _, row in assembling_df.iterrows()
]


# Завдання 1
def task_1():
    """Таблиця кількості встановлених компонентів та сумарної вартості."""
    comp_data = defaultdict(lambda: {"count": 0, "total_cost": 0.0})
    for assembling in assemblings:
        comp = assembling.component
        comp_data[comp.name]["count"] += 1
        comp_data[comp.name]["total_cost"] += comp.price

    summary = pd.DataFrame.from_dict(comp_data, orient='index').reset_index().rename(columns={"index": "name"})
    print(summary)
    return summary


# Завдання 2
def task_2(summary):
    """Діаграма кількості встановлених компонентів."""
    plt.figure(figsize=(10, 6))
    plt.bar(summary['name'], summary['count'], color='skyblue')
    plt.title("Кількість встановлених компонентів")
    plt.xlabel("Назва компоненту")
    plt.ylabel("Кількість")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def task_3(start_date, end_date):
    """Сумарна вартість компонентів для кожного дня за вказаний період."""

    # Перетворюємо строки в datetime
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Словник для зберігання сумарної вартості компонентів для кожного дня
    daily_costs = defaultdict(float)

    # Проходимо по всіх збірках та додаємо вартість компонентів за відповідні дати
    for assembling in assemblings:
        assembling_date = datetime.strptime(assembling.assembling_date, "%Y-%m-%d") if isinstance(assembling.assembling_date, str) else assembling.assembling_date
        if start_date <= assembling_date <= end_date:
            comp = assembling.component
            daily_costs[assembling_date.date()] += comp.price

    # Перетворюємо результат у DataFrame
    daily_costs_df = pd.DataFrame(list(daily_costs.items()), columns=["assembling_date", "total_cost"])

    # Сортуємо по датах
    daily_costs_df = daily_costs_df.sort_values("assembling_date")

    print(daily_costs_df)
    return daily_costs_df




# Завдання 4
def task_4(daily_costs_df):
    """Графік сумарної вартості компонентів для кожного дня."""

    # Переконуємося, що дата має правильний формат
    daily_costs_df['assembling_date'] = pd.to_datetime(daily_costs_df['assembling_date']).dt.strftime('%Y-%m-%d')

    # Створюємо графік
    plt.figure(figsize=(10, 6))
    plt.plot(daily_costs_df['assembling_date'], daily_costs_df['total_cost'], marker='o', color='green')
    plt.title("Сумарна вартість компонентів за кожний день")
    plt.xlabel("Дата")
    plt.ylabel("Сумарна вартість")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def task_5():
    """Перелік компонентів, які не були встановлені у жодному замовленні."""
    # Збираємо ID компонентів, які були встановлені
    installed_ids = {assembling.component.id for assembling in assemblings}
    
    # Збираємо компоненти, яких немає в списку встановлених
    not_installed = [comp for comp in components if comp.id not in installed_ids]
    
    # Виводимо компоненти, які не були встановлені
    print("Компоненти, які не були встановлені:")
    for comp in not_installed:
        print(f"ID: {comp.id}, Назва: {comp.name}, Матеріал: {comp.material}, Ціна: {comp.price}")



# Завдання 6
def task_6():
    """Загальна кількість готових та неготових замовлень."""
    completed = [assembling for assembling in assemblings if assembling.status == "Completed"]
    in_process = [assembling for assembling in assemblings if assembling.status == "In Process"]
    print(f"Готових замовлень: {len(completed)}")
    print(f"Неготових замовлень: {len(in_process)}")
    return completed, in_process


# Завдання 7
def task_7(completed, in_process):
    """Діаграма готових та неготових замовлень."""
    status = ['Готові', 'Неготові']
    counts = [len(completed), len(in_process)]
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=status, autopct='%1.1f%%', startangle=90)
    plt.title("Готові та Неготові замовлення")
    plt.axis('equal')  # Гарантує круглу діаграму
    plt.show()


# Завдання 8
def task_8():
    """Таблиця вартості готових замовлень, відсортованих за вартістю."""
    completed_orders = [assembling for assembling in assemblings if assembling.status == "Completed"]
    order_costs = defaultdict(float)

    for assembling in completed_orders:
        order_costs[assembling.order_number] += assembling.component.price

    sorted_orders = sorted(order_costs.items(), key=lambda x: x[1], reverse=True)
    sorted_costs = pd.DataFrame(sorted_orders, columns=["Order Number", "Total Cost"])
    print(sorted_costs)
    return sorted_costs


# Завдання 9
def task_9(sorted_costs):
    """Діаграма вартості топ 5 готових замовлень."""
    top_5_orders = sorted_costs.head(5)
    plt.figure(figsize=(10, 6))
    plt.bar(top_5_orders['Order Number'], top_5_orders['Total Cost'], color='orange')
    plt.title("Топ 5 готових замовлень за вартістю")
    plt.xlabel("Номер замовлення")
    plt.ylabel("Вартість")
    plt.tight_layout()
    plt.show()


# Завдання 10
def task_10():
    """Кількість компонентів кожного типу для кожної категорії."""
    category_component_count = defaultdict(lambda: defaultdict(int))
    for assembling in assemblings:
        category_component_count[assembling.component.material][assembling.component.name] += 1

    category_component_count_df = pd.DataFrame(
        [(cat, comp, count) for cat, comps in category_component_count.items()
         for comp, count in comps.items()],
        columns=["Category", "Component", "Count"]
    )
    print(category_component_count_df)
    return category_component_count_df


# Завдання 11
def task_11(category_component_count):
    """Експорт таблиці у CSV та Excel."""
    category_component_count.to_csv("category_component_count.csv", index=False)
    category_component_count.to_excel("category_component_count.xlsx", index=False)
    print("Таблиця експортувана в CSV та Excel")


# Меню
def menu():
    category_component_count = None

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Таблиця кількості встановлених компонентів та сумарної вартості")
        print("2. Діаграма для кількості встановлених компонентів")
        print("3. Сумарна вартість компонентів для кожного дня за певний період")
        print("4. Графік сумарної вартості компонентів для кожного дня за певний період")
        print("5. Перелік компонентів, які не були встановлені у жодному замовленні")
        print("6. Загальна кількість готових та неготових замовлень")
        print("7. Діаграма готових та неготових замовлень")
        print("8. Таблиця вартості готових замовлень, відсортованих за вартістю")
        print("9. Діаграма вартості топ 5 готових замовлень")
        print("10. Кількість компонентів кожного типу для кожної категорії")
        print("11. Експорт таблиці у CSV та Excel")
        print("0. Вихід")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            summary = task_1()
        elif choice == "2":
            task_2(summary)
        elif choice == "3":
            start_date = str(input("Enter start date\n"))
            end_date = str(input("Enter end date"))
            daily_costs = task_3(start_date, end_date)
        elif choice == "4":
            task_4(daily_costs)
        elif choice == "5":
            task_5()
        elif choice == "6":
            completed, in_process = task_6()
        elif choice == "7":
            task_7(completed, in_process)
        elif choice == "8":
            sorted_costs = task_8()
        elif choice == "9":
            task_9(sorted_costs)
        elif choice == "10":
            category_component_count = task_10()
        elif choice == "11":
            if category_component_count is not None:
                task_11(category_component_count)
            else:
                print("Для експорту потрібно спочатку виконати завдання 10.")
        elif choice == "0":
            print("Завершення роботи.")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

menu()
