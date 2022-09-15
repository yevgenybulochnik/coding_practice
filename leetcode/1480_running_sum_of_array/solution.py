from typing import List
from itertools import accumulate


def runningSum(nums: List[int]) -> List[int]:
    running_sums = []
    nums_lin = len(nums)
    for i in range(nums_lin):
        running_sums.append(sum(nums[0: i + 1]))
    return running_sums


assert runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]


def runningSum2(nums: List[int]) -> List[int]:
    return list(accumulate(nums))


assert runningSum2([1, 2, 3, 4]) == [1, 3, 6, 10]
