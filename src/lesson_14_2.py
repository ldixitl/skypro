# def printing(func):
#     def inner(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Func {func} called with result: {result}")
#         return result
#
#     return inner
#
#
#
# @printing
# def add_one(x):
#     return x + 1
#
#
# # new_f = printing(add_one)
#
# y = add_one(10)
#
# # y = new_f(10)
#
# print(y)
# import random
#
# def my_decorator(func):
#     def inner(*args, **kwargs):
#         result = func(*args, **kwargs)
#
#         result_int = int(result)
#         return result_int
#
#     return inner
#
#
# @my_decorator
# def get_rand_numbers():
#     return random.randint(1, 100) / random.randint(1, 100)
#
# print(get_rand_numbers())
# import datetime
#
#
# class Employee:
#
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + "@email.com"
#         self.pay = pay
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#
#     @classmethod
#     def set_raise_amt(cls, new_raise_amt):
#         cls.raise_amt = new_raise_amt
#
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True
#
#
# emp_1 = Employee('Jon', 'Snow', 50000)
# emp_2 = Employee('Ivan', 'Ivanov', 60000)
#
# print(Employee.raise_amt)
#
# Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
#
# emp_str_1 = 'Jon-Snow-70000'
# emp_str_2 = 'Ivan-Ivanov-30000'
# emp_str_3 = 'Elena-Nikitina-90000'
#
# first, last, pay = emp_str_1.split('-')
# #new_emp_1 = Employee(first, last, pay)
#
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)
#
#
# my_date = datetime.date(2023, 1, 31)
# print(Employee.is_workday(my_date))
#
# class Employee:
#
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.__first = first
#         self.__last = last
#         self._email = first + '.' + last + "@email.com"
#         self.pay = pay
#
#     def fullname(self):
#         return f"{self.__first} {self.__last}"
#
# emp_1 = Employee("Ivan", "Ivanov", 50_000)
#
# print(emp_1.fullname())
# print(emp_1._email)
# emp_1._email = "test@mail.ru"
# print(emp_1._email)
# print(emp_1.pay)
#
# print(dir(emp_1))
# print(emp_1._Employee__first, emp_1._Employee__last)

# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'
#
# emp_1 = Employee('Jon', 'Snow')
# emp_1.first = 'Tim'
#
# print(emp_1.email)
#
# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     # Геттер для email
#     @property
#     def email(self):
#         """Возвращает email сотрудника. К атрибуту можно обращаться без ()."""
#         return f'{self.first}.{self.last}@email.com'
#
#     # Геттер для fullname
#     @property
#     def fullname(self):
#         """Возвращает полное имя сотрудника. К атрибуту можно обращаться без ()."""
#         return f'{self.first} {self.last}'
#
#     # Чтобы иметь возможность присваивать атрибуту fullname-значения,
#     # надо определить его сеттер. Это работает только для атрибутов с @property
#     @fullname.setter
#     def fullname(self, name):
#         """Метод срабатывает при операции присваивания."""
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
#
#     @fullname.deleter
#     def fullname(self):
#         print('Delete Name!')
#         self.first = None
#         self.last = None
#
# emp_1 = Employee('Test', 'Test')
# emp_1.fullname = 'Jon Snow'
# print(emp_1.first)
# del emp_1.fullname
# print(emp_1.fullname)
