from typing import List


def missing_number(nums: List[int]) -> int:
    ...
    n = len(nums)
    missing_number = None
    for i in range(n + 1):
        if i not in nums:
           missing_number = i
    return missing_number

print(missing_number([9,6,4,2,3,5,7,0,1]))
