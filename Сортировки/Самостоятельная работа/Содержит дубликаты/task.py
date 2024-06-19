from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    ...
    counter = 0
    majority_element = None
    while counter <= 1:
        for i in nums:
            if counter == 0:
                majority_element = i
                counter += 1
            elif i == majority_element:
                counter += 1
        if counter > 1:
            return True
        else:
            return False

print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
