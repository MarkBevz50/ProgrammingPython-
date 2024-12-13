# Тип квитанції
class Receipt:
    def __init__(self, NameSurname, price):
        self.NameSurname = NameSurname  # Ім'я та прізвище платника
        self.price = price  # Вартість послуги

# Тип товарної накладної
class Invoice:
    def __init__(self, product_name, delivery_adress, delivery_count, post_office_number, receiver_name):
        self.product_name = product_name  # Назва товару
        self.delivery_count = delivery_count  # Кількість доставок
        self.post_office_number = post_office_number  # Номер поштового відділення
        self.receiver_name = receiver_name  # Ім'я та прізвище отримувача
        self.delivery_adress = delivery_adress  # Адреса доставки

# Тип поштового відділення
class PostOffice:
    def __init__(self, receipt, invoice):
        self.receipt = receipt  # Квитанція про оплату
        self.invoice = invoice  # Товарна накладна

# Тип поштового відправлення з доставкою
class DeliveryWithFee(PostOffice):
    def __init__(self, receipt, invoice, delivery_fee_percent):
        super().__init__(receipt, invoice)  # Викликаємо конструктор батьківського класу
        self.delivery_fee_percent = delivery_fee_percent  # Націнка за доставку

    def total_price_with_fee(self):
        return self.receipt.price + (self.receipt.price * self.delivery_fee_percent / 100)

# Список відправлень
deliveries = []

# Функція для додавання нових відправлень
def add_delivery(receipt, invoice, fee):
    delivery = DeliveryWithFee(receipt, invoice, fee)
    deliveries.append(delivery)

def total_sum():
    return sum(d.total_price_with_fee() for d in deliveries)

# 2. Перелік відправлень, впорядкований за адресою доставки (лексикографічно)
def sorted_deliveries():
    return sorted(deliveries, key=lambda d: d.invoice.delivery_adress)

# 3. Сумарна вартість для кожного пункту призначення та поштового відділення
def total_price_per_destination_and_post_office():
    destination_totals = {}
    for d in deliveries:
        destination = d.invoice.delivery_adress
        post_office = d.invoice.post_office_number
        if destination not in destination_totals:
            destination_totals[destination] = {'post_offices': {}, 'total': 0}
        if post_office not in destination_totals[destination]['post_offices']:
            destination_totals[destination]['post_offices'][post_office] = 0
        # Додаємо вартість для конкретного відділення
        destination_totals[destination]['post_offices'][post_office] += d.total_price_with_fee()
        # Додаємо вартість до загальної суми для міста
        destination_totals[destination]['total'] += d.total_price_with_fee()

    # Сортування за пунктом призначення (лексикографічно)
    sorted_destinations = dict(sorted(destination_totals.items()))
    return sorted_destinations

# 4. Сумарна вартість відправлень для кожного пункту призначення
def total_price_per_receiver():
    receiver_totals = {}
    for d in deliveries:
        receiver = d.invoice.receiver_name
        if receiver not in receiver_totals:
            receiver_totals[receiver] = 0
        receiver_totals[receiver] += d.total_price_with_fee()

    return receiver_totals

# Приклад даних
receipt1 = Receipt("Андрій Глова", 100)
invoice1 = Invoice("Бентлі", "Львів", 2, 123, "Роман Селіверстов")
add_delivery(receipt1, invoice1, 10)

receipt2 = Receipt("Маркіян Бевз", 200)
invoice2 = Invoice("Порш 911", "Львів", 1, 124, "Андрій Глова")
add_delivery(receipt2, invoice2, 5)

receipt3 = Receipt("Оксана Ярошко", 300)
invoice3 = Invoice("Феррарі", "Львів", 1, 125, "Сергій Ярошко")
add_delivery(receipt3, invoice3, 7)

receipt4 = Receipt("Денис Білий", 250)
invoice4 = Invoice("Тесла", "Дніпро", 3, 126, "Денис Білий")
add_delivery(receipt4, invoice4, 12)

receipt5 = Receipt("Ірина Рожкова", 150)
invoice5 = Invoice("Ауді", "Одеса", 2, 127, "Ольга Доля")
add_delivery(receipt5, invoice5, 8)

receipt6 = Receipt("Тарас Дяченко", 180)
invoice6 = Invoice("Лексус", "Львів", 1, 128, "Святослав Літинський")
add_delivery(receipt6, invoice6, 6)

receipt7 = Receipt("Юлія Ткаченко", 220)
invoice7 = Invoice("Мерседес", "Вінниця", 1, 129, "Орест Музичук")
add_delivery(receipt7, invoice7, 9)

receipt8 = Receipt("Олександр Пилипенко", 400)
invoice8 = Invoice("Роллс-Ройс", "Черкаси", 1, 130, "Іван Дияк")
add_delivery(receipt8, invoice8, 15)

receipt9 = Receipt("Василь Коваленко", 320)
invoice9 = Invoice("БМВ", "Чернівці", 2, 131, "Василь Коваленко")
add_delivery(receipt9, invoice9, 11)

receipt10 = Receipt("Михайло Потоцький", 350)
invoice10 = Invoice("Мазераті", "Херсон", 1, 132, "Роман Дольний")
add_delivery(receipt10, invoice10, 10)

receipt11 = Receipt("Катерина Островська", 290)
invoice11 = Invoice("Джип", "Луцьк", 3, 133, "Петро Моставчук")
add_delivery(receipt11, invoice11, 7)

receipt12 = Receipt("Петро Дорошенко", 270)
invoice12 = Invoice("Рендж Ровер", "Тернопіль", 1, 134, "Іван Сагайдачний")
add_delivery(receipt12, invoice12, 9)

# 1. Отримати загальну суму
print("Загальна сума:", total_sum())

# 2. Вивести список відправлень, відсортований за адресою доставки
print("\nВідправлення за адресами:")
for d in sorted_deliveries():
    print(f"отримувач: {d.invoice.receiver_name}, адреса: {d.invoice.delivery_adress}, ціна з доставкою: {d.total_price_with_fee():.2f} грн")

# 3. Сумарна вартість для кожного пункту призначення і відділення
print("\nСумарна вартість для кожного пункту призначення і поштового відділення:")
destination_totals = total_price_per_destination_and_post_office()
for destination, data in destination_totals.items():
    print(f"Пункт призначення: {destination}")
    # Виводимо суму для кожного відділення
    for post_office, total in data['post_offices'].items():
        print(f"  Відділення {post_office}: {total:.2f} грн")
    # Виводимо загальну суму для міста
    print(f"  Загальна сума для {destination}: {data['total']:.2f} грн\n")

# 4. Сумарна вартість для кожного отримувача
#print("\nСумарна вартість для кожного отримувача:")
#for receiver, total in total_price_per_receiver().items():
   #print(f"{receiver} - {total:.2f} грн")