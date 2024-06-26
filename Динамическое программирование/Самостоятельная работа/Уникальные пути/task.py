def unique_paths(m: int, n: int) -> int:
    ...
    route_count_table = [[0] * m for i in range(n)]
    for ind in range(m):
        route_count_table[0][ind] = 1

    for ind in range(n):
        route_count_table[ind][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            route_count_table[i][j] = route_count_table[i - 1][j] + route_count_table[i][j - 1]
    return route_count_table[-1][-1]


print(unique_paths(3, 7))
