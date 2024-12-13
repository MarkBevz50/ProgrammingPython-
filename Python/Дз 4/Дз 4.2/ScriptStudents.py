import csv

# Функція для зчитування csv-файлу з оцінками студентів
def read_grades(file_name):
    students = []
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # зчитуємо заголовок (імена колонок)
        for row in reader:
            grades = [float(x) if x != 'n' else 0 for x in row[2:]]  # Оцінки з практичних занять, 'n' замінюємо на 0
            missed_classes = row[2:].count('n')  # Рахуємо кількість пропусків 'n'
            students.append({
                "name": row[0],  # Ім'я студента
                "bonus_points": float(row[1]) if row[1] != 'n' else 0,  # Бонусні бали
                "grades": grades,  # Оцінки
                "missed_classes": missed_classes  # Кількість пропусків
            })
    return students


# Функція для внесення оцінок за екзамен для кожного студента
def input_exam_grades(students):
    for student in students:
        while True:
            try:
                exam_grade = float(input(f"Введіть оцінку за екзамен для {student['name']}: "))
                if 0 <= exam_grade <= 50:
                    student['exam'] = exam_grade
                    break
                else:
                    print("Оцінка повинна бути в діапазоні від 0 до 50.")
            except ValueError:
                print("Невірне значення, введіть число.")

# Функція для підрахунку загальної оцінки за курс
def calculate_total_grades(students):
    for student in students:
        student['total'] = sum(student['grades']) + student.get('exam', 0) + student['bonus_points']
        if student['total'] > 100:
            student['total'] = 100

# Функція для збереження підсумкових оцінок в новий csv-файл
def save_total_grades(students, output_file):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Student', 'Total Score'])  # Заголовки
        for student in students:
            writer.writerow([student['name'], student['total']])

# Функція для формування рейтингу студентів
def save_student_ranking(students, ranking_file):
    # Сортуємо студентів за кількістю балів, а потім за кількістю пропусків
    students.sort(key=lambda x: (-x['total'], x['missed_classes']))  # Спершу по загальним балам, потім по пропускам 'n'

    with open(ranking_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Rank', 'Student', 'Bonus points', 'Total Score', 'Missed Classes'])
        for i, student in enumerate(students, 1):
            writer.writerow([i, student['name'], student['bonus_points'], student['total'], student['missed_classes']])


# Основна програма
if __name__ == "__main__":
    # Зчитуємо файл з оцінками студентів
    input_file = 'students.csv'  # Замінити на потрібний шлях до файлу
    students = read_grades(input_file)

    # Вносимо оцінки за екзамен
    input_exam_grades(students)

    # Підраховуємо підсумкові оцінки за курс
    calculate_total_grades(students)

    # Зберігаємо підсумкові оцінки в новий файл
    output_file = 'total_grades.csv'
    save_total_grades(students, output_file)

    # Формуємо рейтинг студентів і зберігаємо в окремий файл
    ranking_file = 'total_ranking.csv'
    save_student_ranking(students, ranking_file)

    print(f"Підсумкові оцінки збережено у файлі {output_file}.")
    print(f"Рейтинг студентів збережено у файлі {ranking_file}.")
