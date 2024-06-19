from typing import List


def maximum_gap(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0

    nums.sort()
    maximum_gap = 0
    for i in range(1, len(nums)):
        maximum_gap = max(maximum_gap, nums[i] - nums[i - 1])
    return maximum_gap