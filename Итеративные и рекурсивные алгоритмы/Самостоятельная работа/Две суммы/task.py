from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    ...
    for ind1, value1 in enumerate(nums):
        for ind2, value2 in enumerate(nums):
            if value1 + value2 == target and ind1 != ind2:
                return [ind1, ind2]
