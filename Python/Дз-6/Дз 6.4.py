from decimal import Decimal
from enum import Enum
from typing import List, Dict

class EventType(Enum):
    CORRUPTION = "Corruption"
    DISASTER = "Disaster"
    ECONOMIC_GROWTH = "EconomicGrowth"
    OLYMPIC_GAMES = "OlympicGames"

class Resource:
    def __init__(self, price: Decimal, origin: str):
        self.price = price
        self.origin = origin
        self.price_history = [(price, "Initial Price")]

    def update_price(self, percent_change: float, event_type: EventType):
        self.price += self.price * Decimal(percent_change / 100)
        self.price_history.append((self.price, event_type.name))

    def get_price_history(self):
        return self.price_history

class Gold(Resource):
    pass

class Oil(Resource):
    pass

class Coal(Resource):
    pass

class Country:
    def __init__(self, name: str):
        self.name = name
        self.resources: List[Resource] = []
        self.event_history: List[str] = []

    def subscribe(self, resource: Resource):
        self.resources.append(resource)

    def generate_event(self, event_type: EventType):
        self.event_history.append(event_type.name)
        for resource in self.resources:
            if event_type in {EventType.ECONOMIC_GROWTH, EventType.OLYMPIC_GAMES}:
                resource.update_price(10, event_type)
            elif event_type in {EventType.CORRUPTION, EventType.DISASTER}:
                resource.update_price(-10, event_type)

    def get_event_history(self):
        return self.event_history

# Створення країн
country_a = Country("CountryA")
country_b = Country("CountryB")
country_c = Country("CountryC")

# Створення ресурсів
gold_a = Gold(Decimal("1000"), "CountryA")
gold_b = Gold(Decimal("800"), "CountryB")
gold_c = Gold(Decimal("1300"), "CountryC")
oil_b = Oil(Decimal("600"), "CountryB")
coal_c = Coal(Decimal("500"), "CountryC")

# Підписка на новини
country_a.subscribe(gold_a)
country_b.subscribe(gold_b)
country_b.subscribe(oil_b)
country_c.subscribe(coal_c)
country_c.subscribe(gold_c)

# Всі ресурси у системі
resources = [gold_a, gold_b,gold_c, oil_b, coal_c]

# Функції меню
def show_all_resources():
    for resource in resources:
        resource_type = type(resource).__name__
        print(f"Resource from {resource.origin} ({resource_type}): Price {resource.price.quantize(Decimal('0.01'))}")



def generate_event_for_country(country, event_type):
    country.generate_event(event_type)
    adjust_prices_for_other_countries(country, event_type)

def adjust_prices_for_other_countries(target_country, event_type):
    for country in [country_a, country_b, country_c]:
        if country != target_country:
            for resource in country.resources:
                if event_type in {EventType.ECONOMIC_GROWTH, EventType.OLYMPIC_GAMES}:
                    resource.update_price(-5, event_type)
                elif event_type in {EventType.CORRUPTION, EventType.DISASTER}:
                    resource.update_price(5, event_type)

def find_country_with_cheapest_resource(resource_type):
    cheapest_resource = min((r for r in resources if isinstance(r, resource_type)), key=lambda x: x.price)
    print(f"The cheapest {resource_type.__name__} is in {cheapest_resource.origin} with price {cheapest_resource.price}")

def find_country_with_most_expensive_resource(resource_type):
    expensive_resource = max((r for r in resources if isinstance(r, resource_type)), key=lambda x: x.price)
    print(f"The most expensive {resource_type.__name__} is in {expensive_resource.origin} with price {expensive_resource.price}")

def show_price_history_for_country_resources(country_name):
    country_resources = [resource for resource in resources if resource.origin == country_name]
    if not country_resources:
        print(f"У країні {country_name} немає ресурсів.")
        return

    for resource in country_resources:
        print(f"Price history for {country_name} {type(resource).__name__}:")
        for price, event in resource.get_price_history():
            print(f"Price: {price.quantize(Decimal('0.01'))}, Event: {event}")
        print()  # Додатковий рядок для розділення історій ресурсів


def show_event_history_for_country(country):
    print(f"Event history for {country.name}:")
    for event in country.get_event_history():
        print(event)

# Консольне меню
while True:
    print("\nМеню:")
    print("1. Вивести усі ресурси наявні в системі")
    print("2. Згенерувати подію для певної країни")
    print("3. Вивести країну з найдешевшим ресурсом")
    print("4. Вивести країну з найдорожчим ресурсом")
    print("5. Вивести історію змін ціни для ресурсу")
    print("6. Вивести події, що стались в країні")
    print("0. Вийти")
    
    choice = input("Оберіть опцію: ")
    if choice == "1":
        show_all_resources()
    elif choice == "2":
        country_name = input("Введіть країну (CountryA, CountryB, CountryC): ")
        event_type = input("Введіть тип події (Corruption, Disaster, Economic_Growth, Olympic_Games): ")
        country = {"CountryA": country_a, "CountryB": country_b, "CountryC": country_c}.get(country_name)
        try:
            event = EventType[event_type.replace(" ", "_").upper()]
            if country:
                generate_event_for_country(country, event)
            else:
                print("Некоректна країна.")
        except KeyError:
            print("Некоректний тип події.")

    elif choice == "3":
        resource_type = input("Введіть тип ресурсу (Gold, Oil, Coal): ")
        resource_class = {"Gold": Gold, "Oil": Oil, "Coal": Coal}.get(resource_type)
        if resource_class:
            find_country_with_cheapest_resource(resource_class)
        else:
            print("Некоректний тип ресурсу.")
    elif choice == "4":
        resource_type = input("Введіть тип ресурсу (Gold, Oil, Coal): ")
        resource_class = {"Gold": Gold, "Oil": Oil, "Coal": Coal}.get(resource_type)
        if resource_class:
            find_country_with_most_expensive_resource(resource_class)
        else:
            print("Некоректний тип ресурсу.")
    elif choice == "5":
        country_name = input("Введіть країну ресурсу (CountryA, CountryB, CountryC): ")
        show_price_history_for_country_resources(country_name)
    elif choice == "6":
        country_name = input("Введіть країну (CountryA, CountryB, CountryC): ")
        country = {"CountryA": country_a, "CountryB": country_b, "CountryC": country_c}.get(country_name)
        if country:
            show_event_history_for_country(country)
        else:
            print("Некоректна країна.")
    elif choice == "0":
        break
    else:
        print("Некоректна опція.")
