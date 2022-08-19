from typing import List


# Brute force solution 0(N^2)
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_len = len(nums)

    for i in range(nums_len):
        index_plus_one = i + 1
        for j in range(index_plus_one, nums_len):
            if nums[i] + nums[j] == target:
                return [i, j]

# This works becuase moving forward in the list means you have already checked
# the sum of previous numbers. 1 + 2 is check when iterating the index of 0, 2 +
# 1 doesnt need to occur when iterating 1th index as it already happened in the
# previous loop
assert twoSum([1, 2, 34, 5], 6) == [0, 3]
