# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'
#
#     @property
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def __repr__(self):
#         return f"{self.__class__.__name__} ('{self.first}', '{self.last}', '{self.pay}')"
#
#     def __str__(self):
#         return f"{self.last} {self.first} ({self.pay})"
#
#     def __add__(self, other):
#         return self.pay + other.pay
#
#     def __len__(self):
#         return len(f"{self.first} {self.last}")
#
#
# emp_1 = Employee("Ivan", "Ivanov", 50_000)
# emp_2 = Employee("Test", "Testov", 60_000)
# print(emp_1)
# print(emp_2)
# total = emp_1 + emp_2
# print(total)
# print(len(emp_1))
#
# class StripChars:
#
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, *args, **kwargs):
#         return args[0].strip(self.chars)
#
#
# st1 = StripChars("?")
# res = st1('?Example?')
# print(res)
#
# st2 = StripChars("!")
# res = st2("!SomeExample!")
# print(res)
#
# class EvenRange:
#     def __init__(self, stop):
#         self.stop = stop
#
#     def __iter__(self):
#         self.current_value = -2
#         return self
#
#     def __next__(self):
#         if self.current_value + 2 < self.stop:
#             self.current_value += 2
#             return self.current_value
#         else:
#             raise StopIteration
#
# r = EvenRange(9)
#
# for i in r:
#     print(i)
#
# class MyOpen:
#     def __init__(self, filename, mode="r"):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.fp = open(self.filename, self.mode)
#         return self.fp
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.fp.close()
#
#
# with MyOpen("test.txt") as fp:
#     print(fp.read())


class MyContext:
    def __enter__(self):
        return self  # При входе в контекст возвращает сам объект.

    def __exit__(self, type, value, traceback):
        if type:  # Если возникло исключение (type не None)
            print("An error occurred")  # Выводит сообщение об ошибке.
        return True  # Подавляет исключение, предотвращая его распространение.


with MyContext():
    x = 1 / 0  # Деление на ноль вызовет исключение
print("Код продолжает выполняться")
