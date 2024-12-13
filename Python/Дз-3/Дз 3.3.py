class Product:
    def __init__(self, id, name, category, price, amount):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.amount = amount

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Price: {self.price}, Amount: {self.amount})"

class Store:
    def __init__(self, initial_balance=0):
        self.products = []
        self.balance = initial_balance
        self.revenue = 0

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added.")
        self.balance -= product.price * product.amount

    def remove_product(self, product_id, quantity):
        for product in self.products:
            if product.id == product_id:
                if product.amount >= quantity:
                    product.amount -= quantity
                    self.balance += product.price * quantity
                    self.revenue += product.price * quantity
                    print(f"Removed {quantity} of {product.name}.")
                    if product.amount == 0:
                        self.products.remove(product)
                else:
                    print(f"Not enough quantity of {product.name}.")
                return
        print("Product not found.")

    def display_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product)

    def find_by_category(self, category):
        found = [p for p in self.products if p.category == category]
        if found:
            for p in found:
                print(p)
        else:
            print(f"No products found in category {category}.")

    def find_price_above(self, N):
        found = [p for p in self.products if p.price > N]
        if found:
            for p in found:
                print(p)
        else:
            print(f"No products found with price above {N}.")

    def find_price_below(self, N):
        found = [p for p in self.products if p.price < N]
        if found:
            for p in found:
                print(p)
        else:
            print(f"No products found with price below {N}.")

    def find_amount_above(self, N):
        found = [p for p in self.products if p.amount > N]
        if found:
            for p in found:
                print(p)
        else:
            print(f"No products found with amount above {N}.")

    def find_amount_below(self, N):
        found = [p for p in self.products if p.amount < N]
        if found:
            for p in found:
                print(p)
        else:
            print(f"No products found with amount below {N}.")

    def total_value(self):
        total = sum(p.price * p.amount for p in self.products)
        print(f"Total value of all products: {total}")

    def current_revenue(self):
        print(f"Current revenue: {self.revenue}")
        print(f"Current balance: {self.balance}")

def load_products_from_file(file_name, store):
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            for line in file:
                id, name, category, price, amount = line.strip().split(',')
                price = float(price)
                amount = int(amount)
                product = Product(id, name, category, price, amount)
                store.add_product(product)
        print(f"Products loaded from {file_name}.")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu(store):
    while True:
        print("\n--- Menu ---")
        print("1. Display all products")
        print("2. Find by category")
        print("3. Find products with price above N")
        print("4. Find products with price below N")
        print("5. Find products with amount above N")
        print("6. Find products with amount below N")
        print("7. Add new product")
        print("8. Add stock of a product")
        print("9. Remove stock of a product")
        print("10. Display total value of all products")
        print("11. Display revenue since the start")
        print("12. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            store.display_all_products()
        elif choice == '2':
            category = input("Enter category: ")
            store.find_by_category(category)
        elif choice == '3':
            N = float(input("Enter price N: "))
            store.find_price_above(N)
        elif choice == '4':
            N = float(input("Enter price N: "))
            store.find_price_below(N)
        elif choice == '5':
            N = int(input("Enter amount N: "))
            store.find_amount_above(N)
        elif choice == '6':
            N = int(input("Enter amount N: "))
            store.find_amount_below(N)
        elif choice == '7':
            id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            amount = int(input("Enter product amount: "))
            product = Product(id, name, category, price, amount)
            store.add_product(product)
        elif choice == '8':
            product_id = input("Enter product ID: ")
            amount = int(input("Enter amount to add: "))
            for product in store.products:
                if product.id == product_id:
                    product.amount += amount
                    store.balance -= product.price * amount
                    print(f"Added {amount} to {product.name}.")
                    break
            else:
                print("Product not found.")
        elif choice == '9':
            product_id = input("Enter product ID: ")
            amount = int(input("Enter amount to remove: "))
            store.remove_product(product_id, amount)
        elif choice == '10':
            store.total_value()
        elif choice == '11':
            store.current_revenue()
        elif choice == '12':
            print("Exiting program...")
            break
        else:
            print("Invalid input. Type 'help' to see menu again.")

if __name__ == "__main__":
    store = Store(initial_balance=1000)  # Initial balance example
    load_products_from_file("./products.txt", store)  
    main_menu(store)