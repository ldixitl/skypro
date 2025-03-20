class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.pay + other.pay

        raise TypeError


class Developer(Employee):

    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class ExampleClass:
    pass


emp_1 = Employee("Ivan", "Ivanov", 50_000)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
exm1 = ExampleClass()

dev_1 = Developer("Petr", "Petrov", 50_000, "Python")
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.first)
# print(dev_1.last)
# print(dev_1.pay)
# print(dev_1.prog_lang)

res = emp_1 + dev_1
print(res)

for emp_obj in (emp_1, dev_1, exm1):
    if issubclass(type(emp_obj), Employee):
        emp_obj.apply_raise()
    else:
        print("Skip object has no raise method")

# class Employee:
#     def work(self):
#         print('Do some work')
#
# class Developer(Employee):
#     def work(self):
#         super().work()
#         print('Write code')
#
# class JavaDeveloper(Developer):
#     def work(self):
#         super().work()
#         print('Write tests for code')
#
# emp = JavaDeveloper()
# emp.work()

