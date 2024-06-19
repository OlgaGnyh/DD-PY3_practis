from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    ...
    intersection = []
    for i in set(nums1):
        if i in set(nums2):
            intersection.append(i)
    return intersection


print(intersection([4,9,5], [9,4,9,8,4]))
