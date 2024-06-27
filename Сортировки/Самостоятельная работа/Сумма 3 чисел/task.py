from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    ...

    # result = []
    # for i in range(len(nums)-2):
    #     for j in range(1, len(nums)-1):
    #         for k in range(2, len(nums)):
    #             if nums[i] + nums[j] + nums[k] == 0 and i != j and i != k and j != k:
    #                 result.append([nums[i], nums[j], nums[k]])
    #     return result


    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1
    return result


print(three_sum([-1,0,1,2,-1,-4]))
