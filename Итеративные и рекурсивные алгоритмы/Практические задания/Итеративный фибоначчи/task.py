def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    ...  # TODO написать итеративный алгоритм чисел Фибоначчи
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1

    for i in range(n-1):
        c = a + b
        a, b = b, c
    return c


print([fib_iterative(i) for i in range(20)])
