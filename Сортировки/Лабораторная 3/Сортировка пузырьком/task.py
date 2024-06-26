from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки пузырьком
    if len(container) <= 1:
        return container
    flag = 0
    n = len(container)
    while flag < len(container) - 1:
        flag = len(container) - 1
        for i in range(n-1):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
                flag -= 1
        n -= 1

    return container


print(sort([98, 45, 1, 5, 6, 8, 7, 54]))
