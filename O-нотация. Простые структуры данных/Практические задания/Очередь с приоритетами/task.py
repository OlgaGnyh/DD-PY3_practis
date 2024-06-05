"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        ...  # TODO использовать deque для реализации очереди с приоритетами
        self.que: dict[ int, deque] = {priority: deque() for priority in range(self.HIGH_PRIORITY, self.LOW_PRIORITY+1)}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        ...  # TODO реализовать метод enqueue
        self.que[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        ...  # TODO реализовать метод dequeue
        for que in self.que.values():
            if que:
                return que.popleft()
        raise IndexError

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        ...  # TODO реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError(f"Индекс должен быть целым числом")

        que = self.que[priority]
        if not 0 <= ind < len(que):
            raise IndexError("Индекс все границ очереди")
        return que[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        ...  # TODO реализовать метод clear
        for que in self.que.values():
            que.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        ...  # TODO реализовать метод __len__
        len_ = 0
        for que in self.que.values():
            len_ += len(que)
        return len_

