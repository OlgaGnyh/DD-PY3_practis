from typing import List


def generate(num_rows: int) -> List[List[int]]:
    ...
    result = [[1] * i for i in range(1, num_rows+1)]
    for i in range(2, len(result)):
        for j in range(1, len(result[i]) - 1):
            result[i][j] = result[i-1][j-1] + result[i-1][j]

    return result


print(generate(6))
