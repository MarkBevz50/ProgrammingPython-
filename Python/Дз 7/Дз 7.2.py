import csv
import pandas as pd

class Reading:
    def __init__(self, previous:int, current:int):
        if current<previous:
            raise ValueError("Поточний показник лічильника не можу бути менший за попередній")
        self.previous = previous
        self.current = current

    @property
    def consumption(self):
        return self.current - self.previous

class ElectricCounter:
    def __init__(self, apartment:int,month:int, day_reading:Reading, night_reading:Reading):
        self.apartment = apartment
        self.month = month
        self.day_reading = day_reading
        self.night_reading = night_reading

    @property
    def month(self):
        return self._month
    @month.setter
    def month(self, value):
        self._month = value

    @property
    def day_consumption(self):
        return self.day_reading.consumption

    @property
    def night_consumption(self):
        return self.night_reading.consumption

    @property
    def total_consumption(self):
        return self.day_consumption + self.night_consumption
    
def load_data(file_paths):
    # Читаємо дані з кількох CSV-файлів
        dataframes = []
        for file_path in file_paths:
            df = pd.read_csv(file_path)
            dataframes.append(df)

        # Об’єднуємо всі дані в одну таблицю
        full_data = pd.concat(dataframes, ignore_index=True)

        # Перевірка, що поточний показник не менший за попередній
        for index, row in full_data.iterrows():
            if row['current_day'] < row['previous_day'] or row['current_night'] < row['previous_night']:
                raise ValueError(f"Invalid readings in apartment {row['apartment']} for month {row['month']}")
    
        return full_data


def monthly_usage(data, month):
    month_data = data[data['month'] == month].copy()
    month_data['day_usage'] = month_data['current_day'] - month_data['previous_day']
    month_data['night_usage'] = month_data['current_night'] - month_data['previous_night']
    month_data['total_usage'] = month_data['day_usage'] + month_data['night_usage']
    
    print(f"Usage data for month {month}:")
    print(month_data[['apartment', 'day_usage', 'night_usage', 'total_usage']].to_string(index=False))


def total_building_usage(data):
    data['day_usage'] = data['current_day'] - data['previous_day']
    data['night_usage'] = data['current_night'] - data['previous_night']
    total_day = data['day_usage'].sum()
    total_night = data['night_usage'].sum()
    total_all = total_day + total_night
    
    print("Total electricity usage in the building:")
    print(f"Day usage: {total_day} kWh, Night usage: {total_night} kWh, Total usage: {total_all} kWh")


def quarterly_cost(data, day_rate, night_rate):
    data['day_usage'] = data['current_day'] - data['previous_day']
    data['night_usage'] = data['current_night'] - data['previous_night']
    data['quarter'] = ((data['month'] - 1) // 3) + 1
    
    for quarter in data['quarter'].unique():
        quarter_data = data[data['quarter'] == quarter]
        cost_day = (quarter_data['day_usage'] * day_rate).sum()
        cost_night = (quarter_data['night_usage'] * night_rate).sum()
        cost_total = cost_day + cost_night
        print(f"Quarter {quarter} costs:")
        print(f"Day cost: {cost_day} грн, Night cost: {cost_night} грн, Total cost: {cost_total} грн")


def max_monthly_usage(data):
    data['day_usage'] = data['current_day'] - data['previous_day']
    data['night_usage'] = data['current_night'] - data['previous_night']
    data['total_usage'] = data['day_usage'] + data['night_usage']
    
    # Застосовуємо групування з вилученням зайвих колонок
    max_usage = data.loc[data.groupby('apartment')['total_usage'].idxmax()].reset_index(drop=True)
    
    print("Maximum monthly consumption for each apartment:")
    print(max_usage[['apartment', 'month', 'day_usage', 'night_usage', 'total_usage']].to_string(index=False))



file_paths = ["flat1.csv", "flat2.csv"]
day_rate = 4.7  # Ціна за 1 кВт/год вдень
night_rate = 3.5  # Ціна за 1 кВт/год вночі

# Завантаження даних
data = load_data(file_paths)

# Перевірка правильності введеного значення місяця
while True:
    try:
        month = int(input("Enter the number of the month (range 1-12): "))
        if 1 <= month <= 12:
            break
        else:
            print("Uncorrect data! Month number must be between 1 and 12.")
    except ValueError:
        print("Please enter a valid integer.")

# а) Виведення таблички використання для конкретного місяця
monthly_usage(data, month)

# б) Загальна кількість спожитої електрики за весь час
total_building_usage(data)

# в) Вартість спожитої електрики у будинку за різні квартали
quarterly_cost(data, day_rate, night_rate)

# г) Найбільше місячне споживання для кожної квартири
max_monthly_usage(data)
