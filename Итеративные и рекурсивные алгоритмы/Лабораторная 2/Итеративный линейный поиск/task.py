"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    ...  # реализовать итеративный линейный поиск
    if arr == []:
        raise ValueError('Список пуст')
    minimum = arr[-1]
    for ind, value in enumerate(arr[::-1]):
        if value <= minimum:
            minimum = value
            minimum_index = len(arr) - 1 - ind

    return minimum_index


print(min_search([1]))
print(min_search([56, 48, 6, 6, 641, 98, 47]))
