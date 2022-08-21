from typing import List


# Brute force solution O(N^2)
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

# O(n) solution
def twoSum2(nums: List[int], target: int) -> List[int]:
    nums_dict = {}

    for position, number in enumerate(nums):
        diff = target - number
        if diff in nums_dict:
            return [nums_dict[diff], position]
        nums_dict[number] = position


# This solution is much faster than the last one 7635ms vs 121ms because it only
# requires a single loop through the values. The way this works is because the
# difference between the target and the number will be the other number. So you
# calculate the difference between the target and number then check if the
# difference is already in the dict. If not store the number as a key and the
# value as its index.


assert twoSum2([1, 2, 34, 5], 6) == [0, 3]
