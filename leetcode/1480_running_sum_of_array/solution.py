from typing import List


def runningSum(nums: List[int]) -> List[int]:
    running_sums = []
    nums_lin = len(nums)
    for i in range(nums_lin):
        running_sums.append(sum(nums[0: i + 1]))
    return running_sums


assert runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
