from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    ...

    result = []
    for i in range(len(nums)-2):
        for j in range(1, len(nums)-1):
            for k in range(2, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and i != j and i != k and j != k:
                    result.append([nums[i], nums[j], nums[k]])
        return result


print(three_sum([-1,0,1,2,-1,-4]))
