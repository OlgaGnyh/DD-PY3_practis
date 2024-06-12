from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # реализовать итеративный алгоритм бинарного поиска
    left_border = 0
    right_border = len(seq) - 1
    while left_border <= right_border:
        midlle_index = (left_border + right_border) // 2
        midlle_value = seq[midlle_index]
        if midlle_value == value:
            while True:
                if not 0 <= midlle_index - 1 <= len(seq) or seq[midlle_index - 1] != value:
                    break
                else:
                    midlle_index -= 1
            return midlle_index
        elif midlle_value < value:
            left_border = midlle_index + 1
        else:
            right_border = midlle_index - 1

    raise ValueError('элемента нет в массиве')


print(binary_search(6, [1, 5, 4, 6, 6, 6, 6, 6, 8, 21, 37, 41, 48, 49, 50, 60, 89, 102, 109, 650]))
print(binary_search(3, [1, 3]))
