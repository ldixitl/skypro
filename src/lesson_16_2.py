import timeit
from abc import ABC, abstractmethod

#
#
# class Employee(ABC):
#
#     @abstractmethod
#     def work(self):
#         pass
#
#
# class Develop(Employee):
#
#     def work(self):
#         print("Write some code")
#
#     def code(self):
#         pass
#
#
# class Accountant(Employee):
#
#     def work(self):
#         print("Counting")
#
#
# dev = Develop()
# acc = Accountant()
#
# dev.work()
# acc.work()
#
# class Employee:
#
#     def __init__(self):
#         self.pay = self.id * 10000
#
#
# class MixinLog:
#     ID = 1
#
#     def __init__(self):
#         self.id = self.ID
#         MixinLog.ID += 1
#         self.order_log()
#         super().__init__()
#
#     def order_log(self):
#         print(f'{self.id}-й сотрудник.')
#
#
# class Develop(MixinLog, Employee):
#
#     def __init__(self):
#         super().__init__()
#
#     def work(self):
#         print("Write some code.")
#
#     def code(self):
#         pass
#
#
# dev_1 = Develop()
# dev_2 = Develop()
#
# print(dev_2.pay)
#
# print(Develop.__mro__)
#
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_set_del(self):
#         self.x += 1
#         self.y = 100
#         del self.y
#
#
# class PointSlots:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_set_del(self):
#         self.x += 1
#         self.y = 100
#         del self.y
#
#
# point_slots = PointSlots(1, 2)
#
# point = Point(1, 2)
#
# time_slots = timeit.timeit(point_slots.get_set_del)
# time = timeit.timeit(point.get_set_del)
#
# print(time_slots)
# print(time)
