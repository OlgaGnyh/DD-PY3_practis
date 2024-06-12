from typing import List
from collections import deque

def two_sum(nums: List[int], target: int) -> List[int]:
    ...
    # for ind1, value1 in enumerate(nums):
    #     for ind2, value2 in enumerate(nums):
    #         if value1 + value2 == target and ind1 != ind2:
    #             return [ind1, ind2]

    dq = deque(sorted([(val, idx) for idx, val in enumerate(nums)]))

    while True:
        summa = dq[0][0] + dq[-1][0]

        if summa > target:
            dq.pop()
        elif summa < target:
            dq.popleft()
        else:
            break
    return [dq[0][1], dq[-1][1]]


print(two_sum([3, 6, 2, 9, 1], 10))
