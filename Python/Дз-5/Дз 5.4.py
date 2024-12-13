import csv

class Apartment:
    def __init__(self, apartment_id, building_number, apartment_number):
        self.apartment_id = apartment_id
        self.building_number = building_number
        self.apartment_number = apartment_number


class WaterBill:
    def __init__(self, apartment_id, month, water_usage):
        self.apartment_id = apartment_id
        self.month = month
        self.water_usage = water_usage  # in m³


class HotWaterBill(WaterBill):
    def __init__(self, apartment_id, month, water_usage, energy_usage):
        super().__init__(apartment_id, month, water_usage)
        self.energy_usage = energy_usage  # in Gcal


class Tariff:
    COLD_WATER_PRICE = 20  # грн за m³
    HOT_WATER_PRICE = 40  # грн за m³
    ENERGY_PRICE = 55  # грн за Гкал


class WaterSupplyManager:
    def __init__(self):
        self.apartments = {}
        self.water_bills = []
        self.hot_water_bills = []

    def add_apartment(self, apartment):
        self.apartments[apartment.apartment_id] = apartment

    def add_water_bill(self, water_bill):
        self.water_bills.append(water_bill)

    def add_hot_water_bill(self, hot_water_bill):
        self.hot_water_bills.append(hot_water_bill)

    def load_apartments(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаємо заголовок
            for row in reader:
                apartment_id, building_number, apartment_number = row
                self.add_apartment(Apartment(int(apartment_id), int(building_number), int(apartment_number)))

    def load_water_bills(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаємо заголовок
            for row in reader:
                apartment_id, month, water_usage = row
                self.add_water_bill(WaterBill(int(apartment_id), month, float(water_usage)))

    def load_hot_water_bills(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаємо заголовок
            for row in reader:
                apartment_id, month, water_usage, energy_usage = row
                self.add_hot_water_bill(HotWaterBill(int(apartment_id), month, float(water_usage), float(energy_usage)))

    def total_payment_per_building(self):
        building_totals = {}
        for bill in self.water_bills + self.hot_water_bills:
            apartment = self.apartments[bill.apartment_id]
            building = apartment.building_number
            if building not in building_totals:
                building_totals[building] = 0

            # Calculate payment for cold or hot water
            if isinstance(bill, HotWaterBill):
                building_totals[building] += bill.water_usage * Tariff.HOT_WATER_PRICE
                building_totals[building] += bill.energy_usage * Tariff.ENERGY_PRICE
            else:
                building_totals[building] += bill.water_usage * Tariff.COLD_WATER_PRICE

        return building_totals

    def monthly_payment_per_building(self):
        monthly_payments = {}
        for bill in self.water_bills + self.hot_water_bills:
            apartment = self.apartments[bill.apartment_id]
            building = apartment.building_number
            if building not in monthly_payments:
                monthly_payments[building] = {}

            if bill.month not in monthly_payments[building]:
                monthly_payments[building][bill.month] = {"cold_water": 0, "hot_water": 0}

            if isinstance(bill, HotWaterBill):
                monthly_payments[building][bill.month]["hot_water"] += bill.water_usage * Tariff.HOT_WATER_PRICE
                monthly_payments[building][bill.month]["hot_water"] += bill.energy_usage * Tariff.ENERGY_PRICE
            else:
                monthly_payments[building][bill.month]["cold_water"] += bill.water_usage * Tariff.COLD_WATER_PRICE

        return monthly_payments

    def payment_for_month(self, month):
        month_payments = {}
        for bill in self.water_bills + self.hot_water_bills:
            if bill.month == month:
                apartment = self.apartments[bill.apartment_id]
                building = apartment.building_number
                if building not in month_payments:
                    month_payments[building] = {}

                apartment_key = f"{apartment.building_number}/{apartment.apartment_number}"
                if apartment_key not in month_payments[building]:
                    month_payments[building][apartment_key] = {"cold_water": 0, "hot_water": 0}

                if isinstance(bill, HotWaterBill):
                    month_payments[building][apartment_key]["hot_water"] += bill.water_usage * Tariff.HOT_WATER_PRICE
                    month_payments[building][apartment_key]["hot_water"] += bill.energy_usage * Tariff.ENERGY_PRICE
                else:
                    month_payments[building][apartment_key]["cold_water"] += bill.water_usage * Tariff.COLD_WATER_PRICE

        return month_payments


# Приклад використання:
manager = WaterSupplyManager()

# Завантажуємо дані з CSV-файлів
manager.load_apartments('apartments.csv')
manager.load_water_bills('cold_water_bills.csv')
manager.load_hot_water_bills('hot_water_bills.csv')

# 1. Вивести сумарну вартість води по будинкам
total_per_building = manager.total_payment_per_building()
print("Сумарна вартість води по будинкам:")
for building, total in total_per_building.items():
    print(f"Будинок {building}: {total} грн")

# 2. Вивести щомісячну оплату по будинкам
monthly_payments = manager.monthly_payment_per_building()
print("\nЩомісячна оплата за холодну та гарячу воду по будинкам:")
for building, months in monthly_payments.items():
    print(f"Будинок {building}:")
    for month, payments in months.items():
        print(f"  {month}: холодна вода - {payments['cold_water']} грн, гаряча вода - {payments['hot_water']} грн")

# 3. Вивести оплату для конкретного місяця
month_input = input("\nВведіть місяць: ")
month_payments = manager.payment_for_month(month_input)
print(f"\nОплата за {month_input}:")
for building, apartments in month_payments.items():
    print(f"Будинок {building}:")
    for apartment, payments in apartments.items():
        print(f"  Квартира {apartment}: холодна вода - {payments['cold_water']} грн, гаряча вода - {payments['hot_water']} грн")
