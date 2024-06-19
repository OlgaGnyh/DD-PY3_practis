from typing import List


def majority_element(nums: List[int]) -> int:
    ...
    counter = 0
    majority_element = None
    for i in nums:
        if counter == 0:
            majority_element = i
            counter += 1
        elif i == majority_element:
            counter += 1
        else:
            counter -= 1
    return majority_element


print(majority_element([1,2,2,1,1,2,2]))
