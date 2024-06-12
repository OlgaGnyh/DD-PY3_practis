def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    ...  # реализовать итеративный алгоритм нахождения факториала
    if n < 0:
        raise ValueError('Число не может быть отрицательным')
    if n == 0:
        factorial = 1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
    return factorial


print(factorial_iterative(5))
