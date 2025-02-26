# class Employee:
#     pass
#
#
# emp_1 = Employee()
# emp_2 = Employee()
#
# emp_1.name = "Ivan"
# emp_1.surname = "Ivanov"
# emp_1.email = "Ivanov@gmail.com"
# emp_1.pay = 50_000
#
# emp_2.name = "Petr"
# emp_2.surname = "Petrov"
# emp_2.email = "Petrov@gmail.com"
# emp_2.pay = 60_000
#
# print(emp_1.name)
# print(emp_1.surname)
#
# print(emp_2.name)
# print(emp_2.surname)
#
# class Employee:
#     """Класс для представления сотрудника"""
#     name: str
#     surname: str
#     email: str
#     pay: int
#
#     number_of_employees = 0
#
#     def __init__(self, name, surname, pay):
#         """Метод для инициализации экземпляра класса."""
#         """Задаём значения атрибутов экземпляра."""
#         self.name = name
#         self.surname = surname
#         self.pay = pay
#         self.email = f'{name}.{surname}@corp.com'
#
#         Employee.number_of_employees += 1
#
#     def fullname(self):
#         """Метод, который возвращает полное имя сотрудника."""
#         return f"{self.surname} {self.name}"
#
# emp_1 = Employee("Ivan", "Ivanov", 50_000)
# emp_2 = Employee("Petr", "Petrov", 60_000)
#
#
# print(emp_1.name)
# print(emp_1.surname)
# print(emp_1.pay)
# print(emp_1.email)
#
# print(emp_1.fullname())
# print(emp_2.fullname())
#
# print(Employee.number_of_employees)
#
#
# class Employee:
#     """Класс сотрудника, который обладает общими свойстваи и методами"""
#
#     name: str  # Указание атрибутов, которые будут доступны для объекта
#     surname: str
#
#     def work(self):
#         print("Do some work")
#
#     def go_to_vacation(self):
#         print("Go to vacation")
#
#
# class Developer(Employee):
#     """Дочерний класс от класса работника, который принимает и переопределяет некоторые свойства"""
#
#     language: str
#     level: str
#
#     def work(self):
#         print("Write code")
#
#     def read_documentation(self):
#         print("Read documentation")
#
#
# dev_1 = Developer()
# print(dev_1.work())
#
# class JavaDeveloper:
#     """Класс для представления Java-разработчиков."""
#
#     def __init__(self, name):
#         """Метод, который инициализирует экземпляры класса."""
#         self.name = name
#
#     def info(self):
#         """Метод для печати информации о Java-разработчике."""
#         print(f'I am {self.name} - Java developer.')
#
#     def code(self):
#         """Метод для программирования на языке Java."""
#         print("class HelloWorld { public static void main(String[] args)...")
#
#
# class PythonDeveloper:
#     """Класс для представления Python-разработчиков."""
#
#     def __init__(self, name):
#         """Метод, который инициализирует экземпляры класса."""
#         self.name = name
#
#     def info(self):
#         """Метод для печати информации о Python-разработчике."""
#         print(f'I am {self.name} - Python developer.')
#
#     def code(self):
#         """Метод для программирования на языке Python."""
#         print("print('Hello, World!')")
#
#
# # Создаем экземпляры разных классов
# dev1 = JavaDeveloper('Ivan')
# dev2 = PythonDeveloper('Petr')
#
# # Но работаем с ними единым образом
# for developer in (dev1, dev2):
#     developer.info()  # Вызов метода info()
#     developer.code()  # Вызов метода code()
#     print()


class Employee:
    """Класс для представления сотрудника"""

    name: str
    surname: str
    email: str
    pay: int

    def __init__(self, name, surname, pay):
        """Метод для инициализации экземпляра класса."""
        """Задаём значения атрибутов экземпляра."""
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = f"{name}.{surname}@corp.com"
        self.is_work = False
        self.is_vacation = False

    def work(self):
        self.is_work = True
        self.is_vacation = False
        print("Do some work.")

    def go_to_vacation(self):
        self.is_vacation = True
        self.is_work = False
        print("Go to vacation.")


if __name__ == "__main__":
    emp_1 = Employee("Ivan", "Ivanov", 50_000)

    print(emp_1.name)
    print(emp_1.surname)
    print(emp_1.pay)
    print(emp_1.email)
