import re
# pattern = re.compile(r'https://www?\.\w+\.\w+')
#
# matches = pattern.findall(text)
#
# url = []
# for match in matches:
#     url.append(match)
#
# text = 'Позвоните мне по номеру 555-123-4567 или 555-987-6543'
#
# pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
# matches = pattern.findall(text)
#
# text = 'Цвет неба - синий.'
#
# replaced_text = re.sub(r'синий', 'blue', text)
# print(replaced_text)
#
from collections import Counter, defaultdict, deque, namedtuple

# text = 'The price of the product is $1001.50'
# numbers = re.findall(r'\d+\.\d+', text, re.IGNORECASE)
# print(numbers)
#
# text = 'The prices are $100.50, €200.75, and ¥300.99'
# result = re.findall(r'[$€¥]\d+\.\d+', text)
# print(result)
#
# pattern = re.compile(r'\d+')
#
# text = 'There are 2 apples and 5 bananas'
# matches = pattern.finditer(text)
#
# pattern = re.compile(r'\d{4}')
#
# text = '20247'
# match = pattern.fullmatch(text)
#
# pattern = re.compile(r'\s+')
#
# text = 'Split this sentence into words'
# split_text = pattern.split(text)
#
# pattern = re.compile(r'\d+')
#
# text = 'I have 2 apples and 5 bananas'
# new_text, num_subs = pattern.subn("number", text)
#
# pattern = re.compile(r'\d')
#
# text = '123abc456'
# match = pattern.search(text, pos=3, endpos=8)
#
#
# # Регулярные выражения для различных форматов дат
# patterns = [
#     re.compile(r'(\d{2})/(\d{2})/(\d{4})'),  # Формат DD/MM/YYYY
#     re.compile(r'(\d{2})-(\d{2})-(\d{4})'),  # Формат MM-DD-YYYY
#     re.compile(r'(\d{4})\.(\d{2})\.(\d{2})') # Формат YYYY.MM.DD
# ]
#
# def normalize_date(date_str):
#     for pattern in patterns:
#         match = pattern.search(date_str)
#         if match:
#             print(match)
#             if pattern.pattern == r'(\d{2})/(\d{2})/(\d{4})':  # DD/MM/YYYY to YYYY-MM-DD
#                 return f'{match.group(3)}-{match.group(2)}-{match.group(1)}'
#             elif pattern.pattern == r'(\d{2})-(\d{2})-(\d{4})':  # MM-DD-YYYY to YYYY-MM-DD
#                 return f'{match.group(3)}-{match.group(1)}-{match.group(2)}'
#             elif pattern.pattern == r'(\d{4})\.(\d{2})\.(\d{2})':  # YYYY.MM.DD to YYYY-MM-DD
#                 return f'{match.group(1)}-{match.group(2)}-{match.group(3)}'
#     return None
#
#
# def extract_and_normalize_dates(strings):
#     normalized_dates = []
#     for string in strings:
#         normalized_date = normalize_date(string)
#         if normalized_date:
#             normalized_dates.append(normalized_date)
#     return normalized_dates
#
#
# dates = [
#     "Сегодня 23/04/2021",
#     "Встреча назначена на 12-05-2020",
#     "Событие произошло 2019.06.17",
#     "Дата: 15/08/2022, запомните её!",
#     "Запланировано на 07-31-2023"
# ]
#
# normalized_dates = extract_and_normalize_dates(dates)
# print(normalized_dates)

# text = 'aaa abc a ab'
# matches = re.findall(r'a*', text)
# matches = re.findall(r'a+', text)
# matches = re.findall(r'a?', text)
# matches = re.findall(r'a{2}', text)
# matches = re.findall(r'a{2,3}', text)

# text = 'abcabc ab abcabcabc'
# matches = re.findall(r'(abc)+', text)
#
# text = 'ab cd abcd'
# matches = re.findall(r'(ab|cd)', text)
# Регулярное выражение для поиска дат и времени
# pattern = re.compile(r'(\d{2}[-/.]\d{2}[-/.]\d{4})\s+в\s+(\d{2}:\d{2})')
#
# # Пример строки с датами и временем
# text = "Встреча запланирована на 23-04-2021 в 14:30 и 12/05/2020 в 09:00. Следующее событие 15-08-2022 в 18:45."
#
# # Функция для извлечения дат и времени
# def extract_dates_and_times(text):
#     # Используем findall для поиска всех совпадений
#     matches = pattern.findall(text)
#     return matches
#
# # Извлекаем и выводим даты и время
# result = extract_dates_and_times(text)
# print(result)
# Список строк с адресами электронной почты
# emails ="""
# CoreyMSchafer@gmail.com
# corey.schafer@university.edu
# dfgsdfhsfghh
# corey-321-schafer@my-work.net
# """
#
#
# # Регулярное выражение для поиска адресов электронной почты
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
#
# # Поиск всех совпадений в списке строк
# matches = pattern.finditer(emails)
#
# # Вывод всех совпадений
# for match in matches:
#     print(match.group())
#
# emails = ['user1@gmail.com', 'user2@yahoo.com', 'user3@yandex.ru', 'user4@hotmail.com', 'user5@gmail.com']
#
# gmail_emails = []
# for email in emails:
#     if re.search(r'\b\w+@gmail\.com\b', email):
#         gmail_emails.append(email)
#
# text = '''
# Visit my website at https://www.example.com
# or you can check out https://www.someotherexample.com
# '''

#
# # Создаем список
# my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
# # Создаем объект Counter на основе списка
# counted = Counter(my_list)
# # Выводим результаты подсчета
# print(counted)
#
# # Создаем строку
# my_string = 'abbcccddddeeeee'
# # Создаем объект Counter на основе строки
# counted = Counter(my_string)
# # Выводим результаты подсчета
# print(counted)
#
# # Использование метода most_common()
# print(counted.most_common(2))
# # Использование метода elements()
# print(list(counted.elements()))
# # Использование метода subtract()
# counted.subtract('abbccc')
# print(counted)
# words = [
#     'apple',
#     'apple',
#     'apple',
#     'banana',
#     'banana',
#     'grape',
#     'grape',
#     'grape',
#     'grape',
#     'orange'
# ]
#
# def get_top_words(list_words, top_n=3):
#     counter_words = Counter(list_words)
#     return counter_words.most_common(top_n)
#
# Создаем defaultdict, который возвращает 0 для отсутствующих ключей
# my_dict = defaultdict(int)
# # Добавляем значение
# my_dict['one'] = 1
# # Выводим существующее значение
# print(my_dict['one'])
# # Выводим значение для отсутствующего ключа
# print(my_dict['two'])
# # Определяем функцию для значений по умолчанию
# def default_value():
#     return 'неизвестно'
#
# # Создаем defaultdict с функцией по умолчанию
# my_dict = defaultdict(default_value)
# # Выводим значение для отсутствующего ключа
# print(my_dict['two'])
#
# grades = [('Alice', 85), ('Bob', 90), ('Alice', 95), ('Bob', 85), ('Alice', 88)]
#
# def grades_group(grades_list):
#     names_dict = defaultdict(list)
#     for name, grade in grades_list:
#         names_dict[name].append(grade)
#     return names_dict
#
# print(grades_group(grades))
#
# Создание deque
# my_deque = deque([1, 2, 3])
# # Добавление элемента в начало очереди
# my_deque.appendleft(0)
# # Добавление элемента в конец очереди
# my_deque.append(4)
# # Удаление элемента из начала очереди
# my_deque.popleft()
# # Удаление элемента из конца очереди
# my_deque.pop()
# # Вывод очереди
# print(my_deque)
#
# Создаем deque
# my_deque = deque([1, 2, 3])
# # Добавляем элементы в конец и начало
# my_deque.append(4)
# my_deque.appendleft(0)
# # Удаляем элементы из конца и начала
# print(my_deque.pop())
# print(my_deque.popleft())
# # Добавляем несколько элементов в конец
# my_deque.extend([5, 6, 7])
# # Добавляем несколько элементов в начало
# my_deque.extendleft([-2, -1])
# print(my_deque)
# # Поворачиваем элементы на 2 позиции вправо
# my_deque.rotate(2)
#
# print(my_deque)
#
# def add_customer(my_queue, customer):
#     my_queue.append(customer)
#     print(f'Текущее состояние очереди: {my_queue}')
#
#
# def add_vip_customer(my_queue, customer):
#     my_queue.appendleft(customer)
#     print(f'Текущее состояние очереди: {my_queue}')
#
#
# def surve_customer(my_queue):
#     if my_queue:
#         print(f"Обслуживаем клиента: {my_queue.popleft()}")
#     else:
#         print("Очередь пуста")
#     print(f'Текущее состояние очереди: {my_queue}')
#
#
# if __name__ == '__main__':
#     queue = deque()
#     add_customer(queue, 'Alice')
#     add_customer(queue, 'Max')
#     add_customer(queue, 'Steve')
#     surve_customer(queue)
#     add_vip_customer(queue, 'Charlie')
#     surve_customer(queue)
#     surve_customer(queue)
#     surve_customer(queue)
#
Point = namedtuple('Point', ['x', 'y'])
# fruits = ['apple', 'banana', 'cherry']
# print(random.choice(fruits))
# print(random.choice(fruits))
# print(Counter(fruits))
# print(random.choice('abcdef'))
# random.shuffle(fruits)
# print(fruits)
#
# def throw_dice():
#     return random.randint(1, 6), random.randint(1, 6)
#
#
# def play_game():
#     player_1_dice_1, player_1_dice_2 = throw_dice()
#     sum_player_1 = player_1_dice_1 + player_1_dice_2
#     print(f'Игрок 1 выбросил кости {player_1_dice_1, player_1_dice_2} на сумму {sum_player_1}')
#
#     player_2_dice_1, player_2_dice_2 = throw_dice()
#     sum_player_2 = player_2_dice_1 + player_2_dice_2
#     print(f'Игрок 2 выбросил кости {player_2_dice_1, player_2_dice_2} на сумму {sum_player_2}')
#
#     if sum_player_1 > sum_player_2:
#         print('Игрок 1 выиграл')
#     elif sum_player_2 > sum_player_1:
#         print('Игрок 2 выиграл')
#     else:
#         print('Ничья!')
#
#
# if __name__ == "__main__":
#     play_game()
#
import json
# p = Point(1, 2)
# print(p.x, p.y)
# Создание объекта Point
# p = Point(1, 2)
# # Замена значения поля
# p2 = p._replace(x=10)
# print(p2)
# # Преобразование в словарь
# print(p._asdict())
# print(p2._asdict())
# # Список полей
# print(p._fields)
# print(p2._fields)
# # Создание из итерируемого объекта
# p3 = Point._make([3, 4])
# print(p3)
#
#
# def add_student(students_dict, name, subject, grade):
#     if name in students_dict:
#         students_dict[name].grades[subject] = grade
#     else:
#         students_dict[name] = Student(name, {subject: grade})
#
#
# def add_grade(students_dict, name, subject, grade):
#     if name in students_dict:
#         students_dict[name].grades[subject] = grade
#     else:
#         print(f'Студент с именем {name} не существует')
#
#
# def print_average_grades(students_dict):
#     for student in students_dict.values():
#         avg = sum(student.grades.values()) / len(student.grades.values())
#         print(f'Средняя оценка для {student.name} равна {avg:.2f}')
#
#
# if __name__ == '__main__':
#     # Создание пустого словаря для хранения оценок студентов
#     students = dict()
#
#     Student = namedtuple('Student', ['name', 'grades'])
#
#     # Добавление оценок для студентов
#     add_student(students, "Alice", "математика", 85)
#     add_student(students, "Alice", "физика", 98)
#     add_student(students, "Bob", "математика", 78)
#     add_student(students, "Bob", "химия", 88)
#     add_grade(students, "Alice", "химия", 95)
#     add_grade(students, "John", "химия", 95)
#     add_grade(students, "Alice", "математика", 32)
#     print(students)
#
#     # # Вывод среднего балла для каждого студента
#     print_average_grades(students)
import random

# print(random.random())
# print(random.randint(1, 87))


def count_emails(input_file: str, output_file: str):
    with open(input_file) as access_file:
        data_from_file = access_file.read()

    pattern = r'\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b'
    email_list = re.findall(pattern, data_from_file)

    domains = Counter(item.split('@')[1] for item in email_list)

    result = {'total_count': len(email_list), 'domains': {}}

    for domain, count in domains.items():
        domain_emails = [email for email in email_list if email.split('@')[1] == domain]

        result['domains'][domain] = {'count': count, 'emails': domain_emails}

    with open(output_file, 'w') as of:
        json.dump(result, of, indent=4)


if __name__ == '__main__':
    count_emails('../logs/access.log', '../data/result.json')
