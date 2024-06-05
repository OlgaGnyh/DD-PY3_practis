"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        first element: элемент с индексом 0
        """
        ...  # TODO инициализировать список
        self.que = []

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        ...  # TODO реализовать метод enqueue
        self.que.append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        ...  # TODO реализовать метод dequeue
        if not self.que:
            raise IndexError
        return self.que.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        ...  # TODO реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError
        elif ind not in [i for i in range(len(self.que))]:
            raise IndexError
        return self.que[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        ...  # TODO реализовать метод clear
        self.que.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        ...  # TODO реализовать метод __len__
        return len(self.que)
