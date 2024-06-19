from typing import List


def partition(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    ...  # TODO реализовать алгоритм быстрой сортировки

    if len(container) <= 1:
        return container

    def _sort(container, low, high):
        if low < high:
            pivot_ind = partition(container, low, high)
            _sort(container, low, pivot_ind - 1)
            _sort(container, pivot_ind + 1, high)
        return container
    return _sort(container, 0, len(container) - 1)


print(sort([98, 45, 1, 5, 6, 8, 7, 54]))
