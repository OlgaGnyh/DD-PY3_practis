from typing import Union
from itertools import count
from math import factorial


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    ...  # TODO вычислить sin(x) с помощью разложения сумму бесконечного ряда
    def part_value(n):
         return ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)

    summa = 0
    for i in count():
        value = part_value(i)
        summa += value

        if abs(value) <= DELTA:
            return summa


print(sinx(3.14))
