from typing import List

# Fails because it takes too long to run, pretty much have to use some sort of
# linear search instead of splitting the array. The Pivot can really be
# anywhere in the array.


def pivotIndex(nums: List[int]) -> int:
    left_sum = 0
    right_sum = 0

    for i, _ in enumerate(nums):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i + 1:])

        if left_sum == right_sum:
            return i

        # This doesnt work becuase the array can have negative numbers
        # if left_sum > right_sum:
        #     return -1

    return -1


assert pivotIndex([1, 7, 3, 6, 5, 6]) == 3


def pivotIndex2(nums: List[int]) -> int:
    S = sum(nums)
    left_sum = 0

    for i, n in enumerate(nums):
        if left_sum == (S - left_sum - n):
            return i
        left_sum += n
    return -1


assert pivotIndex2([1, 7, 3, 6, 5, 6]) == 3
