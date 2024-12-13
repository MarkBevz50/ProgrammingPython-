import random
# class dekanat:
#     def __init__(self, dekan, zastupnik1, zastupnik2, sekretar):
#         self.dekan = dekan
#         self.zastupnik1 = zastupnik1
#         self.zastupnik2 = zastupnik2
#         self.sekretar = sekretar
#     def expel(self, students, student):
#             for stud in students:
#                 if stud.name == student.name and stud.surname == student.surname:
#                     expelled = stud
#                     students.remove(stud) 
#                     break
#                 else:
#                     continue
#             if expelled:
#                 print(f"Expelled:{expelled}")
#             else:
#                 print(f"ther is no {student}")
        
# class student:
#     def __init__(self, name="", surname=""):
#         self._name = None
#         self._surname = None
#         self.name = name
#         self.surname = surname
#     def __str__(self):
#         return f"student {self.name} {self.surname}"
#     @property
#     def name(self):
#         return self._name
#     @property
#     def surname(self):
#         return self._surname
#     @surname.setter
#     def surname(self, surname):
#         if surname == "":
#             raise NameError("Surname couldnt be empty string")
#         elif isinstance(surname, (int,float)):
#             raise TypeError("Name could not be a number!")
#         else:
#             self._surname = surname

#     @name.setter
#     def name(self, name):
#         if name == "":
#             raise NameError("Name couldnt be empty string")
#         elif isinstance(name, (int,float)):
#             raise TypeError("Name could not be a number!")
#         else:
#             self._name = name



# D = dekanat("Diyak", "Horlatch", "Seliverstov", "Marichka")
# I = student("Ihor", "Kucherov")
# M = student("Markiyan", "Bevz")
# P = student("Popovchak", "Andrii")
# L = student("Lopatinskiy", "Oleksa")
# studd = [I,M,P,L]
# D.expel(studd, I)

# class human:
#     def __init__(self, name="", surname="", age=0):
#         self._name = None
#         self._surname = None
#         self._age = None
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def __str__ (self):
#         return f"name: {self.name}, surname: {self.surname}, age: {self.age}"
#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self, name):
#         if name == "":
#             raise NameError("Name cant be an empty string")
#         elif isinstance(name, (int, float)):
#             raise TypeError("Name cant be a number!")
#         else:
#             self._name = name
#     @property
#     def surname(self):
#         return self._surname
#     @surname.setter
#     def surname(self, surname):
#         if surname == "":
#             raise NameError("Surame cant be an empty string")
#         elif isinstance(surname, (int, float)):
#             raise TypeError("Surame cant be a number!")
#         else:
#             self._surname = surname
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self, age):
#         if age <=0:
#             raise ValueError("Age cant be zero or less")
#         elif isinstance(age, str):
#             raise TypeError("Age cant be a string!")
#         else:
#             self._age = age


# class teacher(human):
#     def __init__(self,name, surname, age, salary):
#         super().__init__(name, surname, age)
#         self._salary = None
#         self.salary = salary
#     def __str__(self):
#        return super().__str__() + f", salary: {self.salary}"
#     @property
#     def salary(self):
#         return self._salary
#     @salary.setter
#     def salary(self, salary):
#         if salary <=0:
#             raise ValueError("Salary cant be zero or less")
#         elif isinstance(salary, str):
#             raise TypeError("Salary cant be a string!")
#         else:
#             self._salary = salary
#     def __add__(self, salary_incr):
#         self.salary = self.salary + salary_incr
# S = teacher("Mark", "Bevz", 18, 200000)
# S + 12000
# print(S)


# def div3(num):
#   summ = 0
#   numm = str(num)
#   for l in numm:
#     summ+=int(l)
#   return summ
    
# while 1:
#   A = input("Enter a number:")
#   res = div3(A)
#   print (f"Sum of digits of your number is: {res}")
#   if res%3 == 0:
#     break
#   else:
#     continue

# class Dice:
#     def __init__(self, number_of_points=0):
#         self.number_of_points = random.randint(1, 6)
#     def __str__ (self):
#         return f"number of points: {self.number_of_points}"
# class DiceCollection:
#     def __init__(self, collection_of_dices):
#         self.collection_of_dices = collection_of_dices
#     def print_all_dice(self):
#         for num in self.collection_of_dices:
#             for numnum in num:
#                 print(numnum)
#     def shuffle_dice(self):
#         length = len(self.collection_of_dices)
#         random_index = random.randint(0,length-1)
#         for num in range(length):
#             self.collection_of_dices[num],self.collection_of_dices[random_index] = self.collection_of_dices[random_index],self.collection_of_dices[num]
#     def get_dice_by_index(self, number):
#         certain_dice = self.collection_of_dices[number-1]
#         for num in certain_dice:
#             print(num)
#     def draw_one_dice(self):
#         length = len(self.collection_of_dices)
#         rand_index = random.randint(0, length-1)
#         self.collection_of_dices[rand_index]
#         return self.collection_of_dices[rand_index]
#     def draw_multiple_dice(self, n):
#         length = len(self.collection_of_dices)
#         dices = []
#         for i in range(0, n):
#             rand_index = random.randint(0, length-1)
#             dice=self.collection_of_dices[rand_index]
#             dices.append(dice)
#         return dices
#     def add_new_dice(self):
#         NewDice =[]
#         NewDice.append(Dice())
#         self.collection_of_dices.append(NewDice)
#         return NewDice[0]
#     def total_points(self):
#         summ = 0
#         for num in self.collection_of_dices:
#             for numnum in num:
#                 summ += numnum.number_of_points
#         return summ
    
# def print_dices(arr_of_obj):
#         for num in arr_of_obj:
#             print(num)        

# P = Dice()
# C = Dice()
# L = Dice()
# S = Dice()
# COD = [[P,S],[C],[L],[S]]
# if __name__ == '__main__':
#     game_dice = DiceCollection(COD)
#     game_dice.print_all_dice()
#     print("Меню")
#     while True:
#         k = int(input("Оберіть функцію\n"
#                       "1 - перемішати кістки\n"
#                       "2 - знайти кістку за номером\n"
#                       "3 - витягнути ОДНУ кістку\n"
#                       "4 - витягнути кілька кісток\n"
#                       "5 - додати нову кістку\n"
#                       "6 - підрахувати суму очок\n"
#                       "7 - вивести всі кістки\n"))
#         if k == 1:
#             game_dice.shuffle_dice()
#             print("Кістки перемішано!")
#         elif k == 2:
#             index = int(input("Введіть номер кістки: "))
#             print(game_dice.get_dice_by_index(index))
#         elif k == 3:
#             print_dices(game_dice.draw_one_dice())
#         elif k == 4:
#             n = int(input("Скільки кісток витягти? "))
#             dice = game_dice.draw_multiple_dice(n)
#             for d in dice:
#                 print_dices(d)
#         elif k == 5:
#             new_dice = game_dice.add_new_dice()
#             print(f"Додано нову кістку: {new_dice}")
#         elif k == 6:
#             print(f"Сума очок на всіх кістках: {game_dice.total_points()}")
#         elif k == 7:
#             game_dice.print_all_dice()
#         else:
#             print("Goodbye")
#             break

class product:
    def __init__(self, name, category, price ):
        self._price = price
        self.name = name
        self.category = category
        self.price = price
    def __str__(self):
        return f"Name of product: {self.name}, Category: {self.category}, Price: {self.price}"
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("Price cant`t be negative or zero")
        elif isinstance(price,str):
            raise ValueError("Praise can`t be string")
        else:
            self._price = price
    def __lt__(self, other):
        return self._price < other._price
class Shop:
    def __init__(self, collection_of_products=[]):
        self.collection_of_products = collection_of_products
    def print_all_products(self):
        for num in self.collection_of_products:
            print(num)
    def add_product(self, name,category, price):
        self.collection_of_products.append(product(name,category, price))
    def print_products_by_category(self,category):
        for num in self.collection_of_products:
            if num.category == category:
                print(num)
            else:
                continue
    def remove_product(self, name):
        for num in self.collection_of_products:
            if num.name == name:
                self.collection_of_products.remove(num)
            else:
                continue
    def sort_products_by_price(self):
        self.collection_of_products.sort(reverse = True)
    def print_products_by_name(self,name):
        for num in self.collection_of_products:
            if num.name == name:
                print(num)
            else:
                continue
    def print_unique_categories(self):
        sett = set()
        for num in self.collection_of_products:
            sett.add(num.category)
        print(sett)
            

if __name__ == "__main__": 
    shop = Shop() 
    shop.add_product("Шоколад", "Солодощі", 25) 
    shop.add_product("Чай", "Напої", 30) 
    shop.add_product("Кава", "Напої", 40) 
    shop.add_product("Печиво", "Солодощі", 20) 
 
    print("Меню:") 
    while True: 
        print("\n1 - Додати товар") 
        print("2 - Видалити товар") 
        print("3 - Вивести товари по категорії") 
        print("4 - Сортувати товари за ціною") 
        print("5 - Пошук товару по назві") 
        print("6 - Вивести унікальні категорії") 
        print("7 - Вийти") 
 
        choice = int(input("Оберіть функцію: ")) 
         
        if choice == 1: 
            name = input("Назва товару: ") 
            category = input("Категорія товару: ") 
            price = float(input("Ціна товару: ")) 
            shop.add_product(name, category, price) 
         
        elif choice == 2: 
            name = input("Назва товару для видалення: ") 
            shop.remove_product(name) 
         
        elif choice == 3: 
            category = input("Введіть категорію для фільтрації: ") 
            shop.print_products_by_category(category) 
         
        elif choice == 4: 
            shop.sort_products_by_price() 
            shop.print_all_products() 
         
        elif choice == 5: 
            name = input("Введіть назву товару для пошуку: ") 
            shop.print_products_by_name(name) 
         
        elif choice == 6: 
            shop.print_unique_categories() 
         
        elif choice == 7: 
            print("До побачення!") 
            break 