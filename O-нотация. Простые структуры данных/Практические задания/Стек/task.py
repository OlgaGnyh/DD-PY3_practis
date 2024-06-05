from typing import Any


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, elem: Any) -> None:
        """
        Добавление элемента в вершину стека

        :param elem: Элемент, который должен быть добавлен
        """
         # TODO реализовать операцию push
        self._stack.append(elem)

    def pop(self) -> Any:
        """
        Извлечение элемента из вершины стека.

        :raise: IndexError - Ошибка, если стек пуст

        :return: Извлеченный с вершины стека элемент.
        """
        # TODO реализовать операцию pop
        if not self._stack:
            raise IndexError

        return self._stack.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в стеке, без его извлечения.

        :param ind: индекс элемента (отсчет с вершины, 0 - вершина, последний добавленный элемент, 1 - предпоследний элемент, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ стека

        :return: Значение просмотренного элемента
        """
         # TODO реализовать операцию peek
        if not isinstance(ind, int):
            raise TypeError
        elif ind not in [i for i in range(len(self._stack))]:
            raise IndexError
        return self._stack[-ind-1]

    def clear(self) -> None:
        """ Очистка стека. """
         # TODO реализовать операцию clear
        self._stack.clear()

    def __len__(self) -> int:
        """ Количество элементов в стеке. """
         # TODO реализовать операцию __len__
        return len(self._stack)

    def __str__(self) -> str:
        return f"{self._stack}"


a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
print(a)
print(a.pop())
print(a)


