# try:
#     print(a)
# except NameError:
#     print("Обращение к несуществующей переменной.")
#
# try:
#     1 / 0
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
#
# try:
#     open("file")
# except FileNotFoundError:
#     print("Файл не найден")

# try:
#     a, b = input().split()
#     a, b = int(a), int(b)
#     result = a / b
#     print(result)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#
# class Exp:
#
#     def func1(self):
#         self.func2()
#         print('Штатное завершение func1()')
#
#     def func2(self):
#         self.func3()
#         print('Штатное завершение func2()')
#
#     def func3(self):
#         print(100 / 1)
#         print('Штатное завершение func3()')
#
#
# ob = Exp()
# ob.func1()
#
# print("Выход.")
#
# class MyClass:
#
#     def func1(self):
#         try:
#             1 / 0
#         except ZeroDivisionError:
#             print("На ноль делить нельзя")
#         print("Работает метод func1")
#
#
#     def func2(self):
#         self.func1()
#         print("Работает метод func2")
#
#     def func3(self):
#         self.func2()
#         print("Работает метод func3")
#
#
# if __name__ == '__main__':
#     my_obj = MyClass()
#     my_obj.func3()
#
# class ShellException(Exception):
#
#     def __init__(self, *args, **kwargs):
#         self.message = args[0] if args else "Ошибка обработки скрипта."
#
#     def __str__(self):
#         return self.message
#
#
# class ShellEmptyException(ShellException):
#
#     def __init__(self, *args, **kwargs):
#         self.message = args[0] if args else "Скрипт пустой."
#
#
# class ShellShebangException(ShellException):
#
#     def __init__(self, *args, **kwargs):
#         self.message = args[0] if args else "Отсутствует шебанг."
#
#
# class ShellScript:
#     def __init__(self, content):
#         if not content:
#             raise ShellEmptyException
#         elif content[0:2] != "#!":
#             raise ShellShebangException
#         self.eval()
#
#     def eval(self):
#         pass
#
#
# if __name__ == "__main__":
#     bash_content = '#!/bin/bash'
#     try:
#         shell_script = ShellScript(bash_content)
#     except ShellEmptyException as e:
#         print(e)
#         print("Передайте не пустой файл скрипта.")
#     except ShellShebangException as e:
#         print(e)
#         print("Валидация на шебанг не пройдена.")


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        elif isinstance(other, (int, float)):
            return self.pay + other
        raise TypeError


if __name__ == "__main__":
    emp_1 = Employee("Ivan", "Ivanov", 50_000)
    emp_2 = Employee("Petr", "Petrov", 120_000)

    print(emp_1 + emp_2)
    print(emp_1 + 10000)
    print(emp_1 + "4234")
