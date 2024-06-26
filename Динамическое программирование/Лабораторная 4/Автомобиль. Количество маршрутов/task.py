from typing import List
import pprint


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования
    route_count_table = [[0] * m for i in range(n)]
    for ind in range(m):
        route_count_table[0][ind] = 1

    for ind in range(n):
        route_count_table[ind][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            route_count_table[i][j] = route_count_table[i-1][j] + route_count_table[i][j-1] + route_count_table[i-1][j-1]

    return route_count_table


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
    # pprint.pprint(car_paths(4, 5), width=25)
