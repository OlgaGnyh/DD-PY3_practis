from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать алгоритм бинарного поиска
    if right_border is None:
        right_border = len(seq) - 1

    if left_border > right_border:
        raise ValueError('элемента нет в массиве')

    mid_index = left_border + (right_border - left_border)// 2
    mid_value = seq[mid_index]
    if value == mid_value:
        while True:
            if not 0 <= mid_index - 1 <= len(seq) or seq[mid_index-1] != value:
                break
            else:
                mid_index -= 1
        # while not 0 <= mid_index - 1 <= len(seq) or seq[mid_index-1] != value:
        #     mid_index -= 1
        return mid_index
    elif mid_value < value:
        left_border = mid_index + 1
    else:
        right_border = mid_index - 1
    return binary_search(value, seq, left_border, right_border)


print(binary_search(6, [1, 5, 4,6,6,6,6,6,6, 6, 8, 21, 37, 41, 48, 49, 50, 60, 89, 102, 109, 650]))
