import csv

TARIFFS = {
    1: 50,
    2: 60,
    3: 70,
    4: 85,
}

FUEL_COST_PER_LITER = 55  # Вартість палива за літр


# Клас для комунальної служби
class UtilityService:
    def __init__(self, service_id, name):
        self.service_id = service_id
        self.name = name


# Клас для працівника
class Worker:
    def __init__(self, worker_id, surname, tariff_grade):
        self.worker_id = worker_id
        self.surname = surname
        self.tariff_grade = tariff_grade


# Базовий клас для наряду
class WorkOrder:
    def __init__(self, date, service_id, worker_id, hours_worked):
        self.date = date
        self.service_id = service_id
        self.worker_id = worker_id
        self.hours_worked = hours_worked

    def calculate_payment(self, worker):
        return self.hours_worked * TARIFFS[worker.tariff_grade]


# Клас для наряду зі спецтехнікою
class WorkOrderWithMachinery(WorkOrder):
    def __init__(self, date, service_id, worker_id, hours_worked, fuel_used):
        super().__init__(date, service_id, worker_id, hours_worked)
        self.fuel_used = fuel_used

    def calculate_payment(self, worker):
        base_payment = super().calculate_payment(worker)
        fuel_cost = self.fuel_used * FUEL_COST_PER_LITER
        return base_payment + fuel_cost


# Клас для управління нарядами
class SnowRemovalSystem:
    def __init__(self):
        self.services = {}
        self.workers = {}
        self.work_orders = []

    def add_service(self, service):
        self.services[service.service_id] = service

    def add_worker(self, worker):
        self.workers[worker.worker_id] = worker

    def add_work_order(self, work_order):
        self.work_orders.append(work_order)

    def load_services(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаємо заголовок
            for row in reader:
                service_id, name = row
                self.add_service(UtilityService(int(service_id), name))

    def load_workers(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаємо заголовок
            for row in reader:
                worker_id, surname, tariff_grade = row
                self.add_worker(Worker(int(worker_id), surname, int(tariff_grade)))

    def load_work_orders(self, filename, with_machinery=False):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаємо заголовок
            for row in reader:
                if with_machinery:
                    date, service_id, worker_id, hours_worked, fuel_used = row
                    self.add_work_order(WorkOrderWithMachinery(
                        date, int(service_id), int(worker_id), int(hours_worked), float(fuel_used)))
                else:
                    date, service_id, worker_id, hours_worked = row
                    self.add_work_order(WorkOrder(
                        date, int(service_id), int(worker_id), int(hours_worked)))

    # 1. Сумарна оплата всіх працівників за всі дні
    def total_payment(self):
        total = 0
        for order in self.work_orders:
            worker = self.workers[order.worker_id]
            total += order.calculate_payment(worker)
        return total


        # 2. Сумарні оплати працівників кожного дня
    def daily_payments(self, with_machinery=False):
        daily_sums = {}
        for order in self.work_orders:
            if with_machinery:
                if isinstance(order, WorkOrderWithMachinery):  # З технікою
                    worker = self.workers[order.worker_id]
                    if order.date not in daily_sums:
                        daily_sums[order.date] = 0
                    daily_sums[order.date] += order.calculate_payment(worker)
            else:
                if not isinstance(order, WorkOrderWithMachinery):  # Без техніки
                    worker = self.workers[order.worker_id]
                    if order.date not in daily_sums:
                        daily_sums[order.date] = 0
                    daily_sums[order.date] += order.calculate_payment(worker)
        return daily_sums


    # 3. Сума нарахованої платні для конкретного працівника
    def payment_for_worker(self, surname):
        total = 0
        for order in self.work_orders:
            worker = self.workers[order.worker_id]
            if worker.surname == surname:
                total += order.calculate_payment(worker)
        return total



# Створюємо систему прибирання снігу та завантажуємо дані
snow_removal = SnowRemovalSystem()

# Завантажуємо дані з файлів
snow_removal.load_services('services.csv')
snow_removal.load_workers('workers.csv')
snow_removal.load_work_orders('work_orders.csv', with_machinery=False)
snow_removal.load_work_orders('work_orders_with_machinery.csv', with_machinery=True)

# Виведення результатів

# 1. Отримати сумарну оплату всіх працівників
print(f"Сумарна оплата: {snow_removal.total_payment()} грн")

# 2. Сумарна оплата кожного дня (без спецтехніки)
print("Сумарні оплати кожного дня (без спецтехніки):")
for date, total in snow_removal.daily_payments(with_machinery=False).items():
    print(f"{date}: {total} грн")

# 2. Сумарна оплата кожного дня (зі спецтехнікою)
print("Сумарні оплати кожного дня (зі спецтехнікою):")
for date, total in snow_removal.daily_payments(with_machinery=True).items():
    print(f"{date}: {total} грн")

# 3. Оплата для працівника із певним прізвищем 
surname = input("Введіть прізвище робітника: ")
print(f"Оплата для {surname} : {snow_removal.payment_for_worker(surname)} грн")
