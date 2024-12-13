import csv
from datetime import datetime

# Завантаження даних із CSV-файлів
def load_stations(stations_file):
    stations = {}
    with open(stations_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустити заголовок
        for row in reader:
            station_id, location = row[0], row[1]
            stations[station_id] = location
    return stations

def load_fuel_prices(fuel_prices_file):
    fuel_prices = {}
    with open(fuel_prices_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустити заголовок
        for row in reader:
            if len(row) < 2:  # Перевірка на наявність необхідної кількості елементів
                continue  # Пропустити рядок, якщо він порожній або неповний
            fuel_type, price_per_liter = row[0], float(row[1])
            fuel_prices[fuel_type] = price_per_liter
    return fuel_prices


def load_services(service_files):
    services = []
    for file_name in service_files:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                station_id = row[0]
                service_date = datetime.strptime(row[1], '%Y-%m-%d').date()
                fuel_type = row[2]
                fuel_quantity = float(row[3])
                services.append({
                    "station_id": station_id,
                    "service_date": service_date,
                    "fuel_type": fuel_type,
                    "fuel_quantity": fuel_quantity
                })
    return services

# 1. Обчислення виручки для кожної заправки
def calculate_total_revenue_by_station(stations, fuel_prices, services):
    revenue_by_station = {}
    for service in services:
        station_id = service['station_id']
        location = stations[station_id]
        fuel_type = service['fuel_type']
        fuel_quantity = service['fuel_quantity']
        price_per_liter = fuel_prices[fuel_type]
        revenue = fuel_quantity * price_per_liter
        if station_id not in revenue_by_station:
            revenue_by_station[station_id] = {"location": location, "revenue": 0}
        revenue_by_station[station_id]["revenue"] += revenue
    return revenue_by_station

# 2. Виручка за видом пального для введеного міста та дати
def calculate_revenue_by_fuel_type(stations, fuel_prices, services, city, date):
    date = datetime.strptime(date, '%Y-%m-%d').date()
    revenue_by_fuel = {}
    for service in services:
        station_id = service['station_id']
        if stations[station_id] == city and service['service_date'] == date:
            fuel_type = service['fuel_type']
            fuel_quantity = service['fuel_quantity']
            price_per_liter = fuel_prices[fuel_type]
            revenue = fuel_quantity * price_per_liter
            if fuel_type not in revenue_by_fuel:
                revenue_by_fuel[fuel_type] = 0
            revenue_by_fuel[fuel_type] += revenue
    return revenue_by_fuel

# 3. Сума на рахунок для дронів
def calculate_drones_fund(services):
    drone_fuel_types = ['PULLS_95', 'PULLS_Diesel']
    drone_fund = 0
    for service in services:
        if service['fuel_type'] in drone_fuel_types:
            drone_fund += service['fuel_quantity']  # Додаємо по 1 грн за кожен літр
    return drone_fund

# Приклад використання функцій
stations_file = 'stations.csv'
fuel_prices_file = 'fuel_prices.csv'
service_files = ['service1.csv', 'service2.csv']

stations = load_stations(stations_file)
fuel_prices = load_fuel_prices(fuel_prices_file)
services = load_services(service_files)

# 1. Виручка для кожної заправки
total_revenue_by_station = calculate_total_revenue_by_station(stations, fuel_prices, services)
print("Виручка для кожної заправки:")
for station_id, data in total_revenue_by_station.items():
    print(f"Заправка {station_id} ({data['location']}): {data['revenue']} грн")

# 2. Введення міста та дати для обчислення виручки за видом пального
city = input("Введіть місто/селище: ")
date = input("Введіть дату (у форматі РРРР-ММ-ДД): ")
revenue_by_fuel_type = calculate_revenue_by_fuel_type(stations, fuel_prices, services, city, date)
print(f"Виручка за кожен вид пального для {city} на {date}:")
for fuel_type, revenue in revenue_by_fuel_type.items():
    print(f"{fuel_type}: {revenue} грн")

# 3. Сума на закупівлю дронів
total_drone_fund = calculate_drones_fund(services)
print("Сума на рахунок для дронів ШАРК:", total_drone_fund, "грн")
