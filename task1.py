# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реал. операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
from typing import List, Any


class Matrix:
    def __init__(self, ls):
        self.ls = ls
        self.new_list = []

    def __add__(self, other):
        for i in zip(self.ls, other.ls):
            self.new_list.append([el1 + el2 for el1, el2 in zip(i[0], i[1])])
        return '\n'.join([' '.join([str(x) for x in i]) for i in self.ls])

    def __str__(self):
        return '\n'.join([' '.join([str(x) for x in i]) for i in self.ls])


my_list1 = Matrix([[1, 2, 3], [11, 3, 5], [5, 2, 1]])
my_list2 = Matrix([[4, 2, 9], [12, 33, 5], [34, 2, 12]])
print(my_list1)
print('-'*30)
print(my_list2)
print('-'*30)
print(my_list1 + my_list2)
