import pandas as pd

# Класи для роботи з даними
class Book:
    def __init__(self, id, name, writer, release_date):
        self.id = int(id)
        self.name = name
        self.writer = writer
        self.release_date = release_date

    def __str__(self):
        return f"Book: {self.name}, Writer: {self.writer}, Release date: {self.release_date}"

class Reader:
    def __init__(self, id, name, age):
        self.id = int(id)
        self.name = name
        self.age = int(age)

    def __str__(self):
        return f"Reader: {self.name}, Age: {self.age}"

class BookRent:
    def __init__(self, reader_id, book_id, start_date, days):
        self.reader_id = int(reader_id)
        self.book_id = int(book_id)
        self.start_date = start_date
        self.days = int(days)

def load_books(file_path):
    books = []
    books_df = pd.read_csv(file_path)
    for _, row in books_df.iterrows():
        books.append(Book(row["id"], row["name"], row["writer"], row["release_date"]))
    return books, books_df

def load_readers(file_path):
    readers = []
    readers_df = pd.read_csv(file_path)
    for _, row in readers_df.iterrows():
        readers.append(Reader(row["id"], row["name"], row["age"]))
    return readers, readers_df

def load_rents(file_path):
    rents = []
    rents_df = pd.read_csv(file_path)
    for _, row in rents_df.iterrows():
        rents.append(BookRent(row["reader_id"], row["book_id"], row["start_date"], row["days"]))
    return rents, rents_df

def analyze_data(books_df, readers_df, rents_df):
    # а) 
    book_rent_days = rents_df.groupby("book_id")["days"].sum().reset_index()
    book_rent_days = book_rent_days.merge(books_df, left_on="book_id", right_on="id")
    print("а) Загальна кількість днів оренди для кожної книги:")
    print(book_rent_days[["name", "writer", "days"]])

    # б) 
    reader_rents = rents_df.merge(books_df, left_on="book_id", right_on="id")
    reader_rents = reader_rents.merge(readers_df, left_on="reader_id", right_on="id", suffixes=("_book", "_reader"))
    grouped_rents = reader_rents.groupby(["reader_id", "name_reader", "name_book"])["days"].sum().reset_index()

    print("\nб) Інформація про оренди для кожного читача:")
    print(grouped_rents)

    # в)
    reader_total_days = rents_df.groupby("reader_id")["days"].sum().reset_index()
    reader_total_days = reader_total_days.merge(readers_df, left_on="reader_id", right_on="id")
    over_30_days = reader_total_days[reader_total_days["days"] > 30]

    print("\nв) Читачі, які орендували книги більше ніж на 30 днів:")
    print(over_30_days[["name", "days"]])

# Шлях до CSV файлів
books_file = "books.csv"
readers_file = "readers.csv"
rents_file = "book_rents.csv"

# Завантаження даних у класи та DataFrame
books, books_df = load_books(books_file)
readers, readers_df = load_readers(readers_file)
rents, rents_df = load_rents(rents_file)

# Аналіз даних
analyze_data(books_df, readers_df, rents_df)
