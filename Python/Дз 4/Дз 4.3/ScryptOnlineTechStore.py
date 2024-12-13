from datetime import datetime, timedelta
import random

# Класи для таблиць
class User:
    def __init__(self, id, first_name, last_name, email, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

class Product:
    def __init__(self, id, category_id, model, year, price, color, purchase_price):
        self.id = id
        self.category_id = category_id
        self.model = model
        self.year = year
        self.price = price  # Ціна продажу
        self.color = color
        self.purchase_price = purchase_price  # Закупочна ціна


class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Order:
    def __init__(self, id, created_date, total_price, status, user_id, address):
        self.id = id
        self.created_date = created_date
        self.total_price = total_price
        self.status = status
        self.user_id = user_id
        self.address = address

class OrderDetails:
    def __init__(self, id, order_id, product_id, quantity, price):
        self.id = id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

# База даних
users = []
products = []
categories = []
orders = []
order_details = []

# Функції для меню
def add_product():
    id = len(products) + 1
    category_id = int(input("Введіть ID категорії продукту: "))
    model = input("Введіть модель продукту: ")
    year = int(input("Введіть рік випуску продукту: "))
    price = float(input("Введіть ціну продукту: "))
    color = input("Введіть колір продукту: ")
    product = Product(id, category_id, model, year, price, color)
    products.append(product)
    print("Продукт додано успішно.")

def add_order():
    id = len(orders) + 1
    user_id = int(input("Введіть ID користувача: "))
    address = input("Введіть адресу для доставки: ")
    created_date = datetime.now()
    total_price = 0
    order = Order(id, created_date, total_price, 'New', user_id, address)
    orders.append(order)

    while True:
        product_id = int(input("Введіть ID продукту (0 для завершення): "))
        if product_id == 0:
            break
        quantity = int(input("Введіть кількість продукту: "))
        product = next((p for p in products if p.id == product_id), None)
        if product:
            price = product.price * quantity
            total_price += price
            order_detail = OrderDetails(len(order_details) + 1, order.id, product_id, quantity, price)
            order_details.append(order_detail)

    order.total_price = total_price
    print("Замовлення створено успішно.")

def update_order_status():
    order_id = int(input("Введіть ID замовлення: "))
    new_status = input("Введіть новий статус (New, Paid, Delivered): ")
    order = next((o for o in orders if o.id == order_id), None)
    if order:
        order.status = new_status
        print("Статус замовлення оновлено.")

def print_products_by_category():
    category_id = int(input("Введіть ID категорії: "))
    filtered_products = [p for p in products if p.category_id == category_id]
    if filtered_products:
        for product in filtered_products:
            print(f"Model: {product.model}, Price: {product.price}, Year: {product.year}")
    else:
        print("Немає продуктів в цій категорії.")

def find_regular_customers():
    # Пошук клієнтів з 3 або більше оплаченими замовленнями
    paid_orders = {user_id: 0 for user_id in set(order.user_id for order in orders)}
    
    # Збільшення кількості оплачених замовлень для кожного клієнта
    for order in orders:
        if order.status == 'Paid':
            paid_orders[order.user_id] += 1
    
    # Вибір клієнтів, які мають 3 або більше оплачених замовлень
    regular_customers = [(user_id, count) for user_id, count in paid_orders.items() if count >= 3]
    
    if regular_customers:
        for customer_id, count in regular_customers:
            user = next((u for u in users if u.id == customer_id), None)
            if user:
                # Виводимо ім'я клієнта і кількість його оплачених замовлень
                print(f"Постійний клієнт: {user.first_name} {user.last_name} — Кількість оплачених замовлень: {count}")
    else:
        print("Немає постійних клієнтів.")


def calculate_income(start_date, end_date):
    net_income = 0  # Змінна для чистого прибутку

    for order in orders:
        if start_date <= order.created_date <= end_date and (order.status == 'Paid' or order.status == 'Delivered'):
            # Знайти всі деталі замовлення для цього замовлення
            for detail in order_details:
                if detail.order_id == order.id:
                    # Знайти продукт за ID
                    product = next((p for p in products if p.id == detail.product_id), None)
                    if product:
                        # Обчислити чистий прибуток для кожного продукту
                        profit_per_unit = product.price - product.purchase_price  # Чистий прибуток з одиниці товару
                        net_income += profit_per_unit * detail.quantity  # Чистий прибуток за кількість одиниць товару

    print(f"Чистий дохід за період з {start_date} по {end_date}: {net_income}")


def find_top_5_products():
    product_sales = {product.id: 0 for product in products}
    for detail in order_details:
        product_sales[detail.product_id] += detail.quantity
    
    top_5_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:5]
    for product_id, quantity in top_5_products:
        product = next((p for p in products if p.id == product_id), None)
        print(f"Продукт: {product.model}, Продано одиниць: {quantity}")

def find_busy_days():
    days_of_week = [0] * 7  # Дні тижня (0 - понеділок, 6 - неділя)
    for order in orders:
        days_of_week[order.created_date.weekday()] += 1

    # Обчислимо середню кількість замовлень
    total_orders = sum(days_of_week)
    avg_orders = total_orders / len(days_of_week)

    # Виводимо кількість замовлень по днях
    for i, count in enumerate(days_of_week):
        print(f"{['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'Пятниця', 'Субота', 'Неділя'][i]}: {count} замовлень")

    # Виводимо дні, коли кількість замовлень перевищує середнє на m або більше
    print("\nДні, коли найчастіше робляться покупки:")
    for i, count in enumerate(days_of_week):
        if count > avg_orders :
            print(f"{['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'Пятниця', 'Субота', 'Неділя'][i]}: {count} замовлень (найбільш зайняті дні)")


def find_category_with_highest_average_price():
    # Створюємо словник для зберігання цін за категоріями
    category_prices = {category.id: [] for category in categories}
    
    # Заповнюємо словник списками цін продуктів для кожної категорії
    for product in products:
        category_prices[product.category_id].append(product.price)
    
    # Обчислюємо середню ціну для кожної категорії
    category_avg_prices = {
        category_id: (sum(prices) / len(prices)) for category_id, prices in category_prices.items() if prices
    }
    
    # Знаходимо категорію з найвищою середньою ціною
    if category_avg_prices:
        max_category_id = max(category_avg_prices, key=category_avg_prices.get)
        max_category = next((c for c in categories if c.id == max_category_id), None)
        
        # Виводимо категорію з найвищою середньою ціною
        print(f"Категорія з найвищою середньою ціною: {max_category.name} ({category_avg_prices[max_category_id]:.2f})")
    else:
        print("Немає категорій з продуктами для обчислення.")

def find_users_without_orders():
    users_with_orders = {order.user_id for order in orders}
    users_without_orders = [user for user in users if user.id not in users_with_orders]
    
    if users_without_orders:
        for user in users_without_orders:
            print(f"Користувач без замовлень: {user.first_name} {user.last_name}")
    else:
        print("Усі користувачі зробили замовлення.")

def find_users_above_average_orders():
    # Обчислення середньої вартості всіх замовлень
    average_order_total = sum(order.total_price for order in orders) / len(orders)
    
    print(f"Середня вартість всіх замовлень: {average_order_total:.2f} $")
    
    # Збір користувачів із замовленнями вище середнього і виведення їх загальної суми
    users_above_average = {order.user_id: 0 for order in orders if order.total_price > average_order_total}
    
    for order in orders:
        if order.user_id in users_above_average:
            users_above_average[order.user_id] += order.total_price
    
    if users_above_average:
        for user_id, total in users_above_average.items():
            user = next((u for u in users if u.id == user_id), None)
            print(f"Користувач {user.first_name} {user.last_name} замовив на суму: {total:.2f} $, що більше за середню.")
    else:
        print("Немає користувачів із замовленнями більше за середню вартість.")

# Консольне меню
def menu():
    while True:
        print("\nМеню:")
        print("1. Додати продукт")
        print("2. Додати замовлення")
        print("3. Оновити статус замовлення")
        print("4. Вивести продукти за категорією")
        print("5. Знайти постійних клієнтів")
        print("6. Знайти дохід за період")
        print("7. Топ 5 продуктів")
        print("8. Дні з найчастішими покупками")
        print("9. Категорія з найвищою середньою ціною")
        print("10. Користувачі без замовлень")
        print("11. Користувачі з замовленнями більше за середню суму")
        print("0. Вихід")
        
        choice = input("Виберіть дію: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            add_order()
        elif choice == '3':
            update_order_status()
        elif choice == '4':
            print_products_by_category()
        elif choice == '5':
            find_regular_customers()
        elif choice == '6':
            start_date = datetime.strptime(input("Введіть початкову дату (YYYY-MM-DD): "), "%Y-%m-%d")
            end_date = datetime.strptime(input("Введіть кінцеву дату (YYYY-MM-DD): "), "%Y-%m-%d")
            calculate_income(start_date, end_date)
        elif choice == '7':
            find_top_5_products()
        elif choice == '8':
            find_busy_days()
        elif choice == '9':
            find_category_with_highest_average_price()
        elif choice == '10':
            find_users_without_orders()
        elif choice == '11':
            find_users_above_average_orders()
        elif choice == '0':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


# Категорії
categories = [
    Category(1, "Ноутбуки"),
    Category(2, "Телефони"),
    Category(3, "Телевізори"),
    Category(4, "Планшети"),
    Category(5, "Аксесуари")
]

# Користувачі
users = [
    User(1, "Олександр", "Коваленко", "alex@domain.com", "+380123456789"),
    User(2, "Ірина", "Шевченко", "iryna@domain.com", "+380987654321"),
    User(3, "Максим", "Петренко", "maksym@domain.com", "+380555667788"),
    User(4, "Ольга", "Дмитренко", "olga@domain.com", "+380999888777"),
    User(5, "Віктор", "Колодій", "viktor@domain.com", "+380333444555"),
    User(6, "Тетяна", "Соловей", "tatiana@domain.com", "+380654321987"),  # Новий користувач
    User(7, "Дмитро", "Завгородній", "dmytro@domain.com", "+380321654987")  # Новий користувач
]

# Продукти
products = [
    # Ноутбуки
    Product(1, 1, "MacBook Pro", 2023, 2500, "Silver", 2000),
    Product(2, 1, "Dell XPS 13", 2022, 1800, "Black", 1500),
    Product(3, 1, "Lenovo ThinkPad X1 Carbon", 2023, 2000, "Gray", 1700),

    # Телефони
    Product(4, 2, "iPhone 14", 2022, 1200, "Black", 900),
    Product(5, 2, "Samsung Galaxy S23", 2023, 1100, "White", 800),
    Product(6, 2, "Google Pixel 8", 2023, 900, "Green", 700),

    # Телевізори
    Product(7, 3, "Samsung QLED 65\"", 2023, 2000, "Gray", 1500),
    Product(8, 3, "LG OLED 55\"", 2022, 1800, "Black", 1400),
    Product(9, 3, "Sony Bravia 4K 60\"", 2023, 1600, "Silver", 1300),

    # Планшети
    Product(10, 4, "iPad Pro 11\"", 2023, 1500, "Silver", 1200),  # Новий продукт
    Product(11, 4, "Samsung Galaxy Tab S8", 2023, 900, "Black", 700),  # Новий продукт

    # Аксесуари
    Product(12, 5, "Apple AirPods Pro", 2023, 300, "White", 200),  # Новий продукт
    Product(13, 5, "Samsung Galaxy Buds", 2023, 250, "Black", 150)  # Новий продукт
]

# Замовлення
orders = [
    Order(1, datetime(2024, 1, 15), 3700, "Paid", 1, "Київ, вул. Лесі Українки, 10"),
    Order(2, datetime(2024, 2, 10), 1800, "Delivered", 2, "Львів, вул. Шевченка, 25"),
    Order(3, datetime(2024, 3, 5), 2900, "New", 3, "Одеса, вул. Дерибасівська, 7"),
    Order(4, datetime(2024, 1, 20), 1200, "Paid", 4, "Харків, вул. Сумська, 12"),
    Order(5, datetime(2024, 2, 28), 2500, "Delivered", 5, "Дніпро, вул. Центральна, 5"),

    # Повторні замовлення
    Order(6, datetime(2024, 1, 27), 5000, "Paid", 1, "Київ, вул. Лесі Українки, 10"),  # Олександр Коваленко
    Order(6, datetime(2024, 1, 25), 5000, "Paid", 1, "Київ, вул. Лесі Українки, 10"),  # Олександр Коваленко
    Order(7, datetime(2024, 2, 15), 1200, "Paid", 4, "Київ, вул. Лесі Українки, 10"),  # Олександр Коваленко
    Order(8, datetime(2024, 3, 10), 2200, "Delivered", 10, "Львів, вул. Шевченка, 25"),  # Ірина Шевченко
    Order(9, datetime(2024, 2, 5), 1600, "Paid", 8, "Одеса, вул. Дерибасівська, 7"),  # Максим Петренко
    Order(10, datetime(2024, 3, 12), 1500, "Delivered", 6, "Дніпро, вул. Центральна, 5"),  # Віктор Іванов
    Order(11, datetime(2024, 4, 1), 1900, "Paid", 10, "Київ, вул. Лесі Українки, 10"),  # Тетяна Соловей
    Order(12, datetime(2024, 4, 5), 800, "Delivered", 11, "Львів, вул. Шевченка, 25"),  # Дмитро Завгородній
]

# Деталі замовлень
order_details = [
    # Олександр Коваленко купив MacBook Pro і iPhone 14
    OrderDetails(1, 1, 1, 1, 2500),  # MacBook Pro
    OrderDetails(2, 1, 4, 1, 1200),  # iPhone 14

    # Ірина Шевченко купила LG OLED 55"
    OrderDetails(3, 2, 8, 1, 1800),  # LG OLED 55"

    # Максим Петренко купив Dell XPS 13 і Google Pixel 7
    OrderDetails(4, 3, 2, 1, 1800),  # Dell XPS 13
    OrderDetails(5, 3, 6, 1, 900),   # Google Pixel 7

    # Ольга Сидорова купила iPhone 14
    OrderDetails(6, 4, 4, 1, 1200),  # iPhone 14

    # Віктор Іванов купив MacBook Pro
    OrderDetails(7, 5, 1, 1, 2500),  # MacBook Pro

    # Повторні замовлення
    # Олександр Коваленко повторно купив MacBook Pro
    OrderDetails(8, 6, 1, 1, 2500),  # MacBook Pro
    OrderDetails(9, 7, 4, 1, 1200),  # iPhone 14 (повторно)

    # Ірина Шевченко купила Asus ZenBook 14
    OrderDetails(10, 8, 10, 1, 2200),  # Asus ZenBook 14

    # Максим Петренко купив Samsung QLED 65"
    OrderDetails(11, 9, 7, 1, 2000),  # Samsung QLED 65"

    # Віктор Іванов купив Google Pixel 8
    OrderDetails(12, 10, 6, 1, 900),  # Google Pixel 8

    # Тетяна Соловей купила iPad Pro
    OrderDetails(13, 11, 10, 1, 1500),  # iPad Pro

    # Дмитро Завгородній купив Samsung Galaxy Buds
    OrderDetails(14, 12, 13, 1, 250)  # Samsung Galaxy Buds
]



menu()
