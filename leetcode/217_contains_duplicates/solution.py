from collections import Counter
from typing import List


def containsDuplicates(nums: List[int]) -> bool:
    count = Counter(nums)
    values = count.values()

    if max(values) > 1:
        return True
    else:
        return False


assert containsDuplicates([1, 2, 3, 1]) == True
assert containsDuplicates([1, 2, 3, 4]) == False

# Different example from the discussion which is much shorter and doesnt use counters
def containsDuplicates2(nums: List[int]) -> bool:
    return False if len(nums) == len(set(nums)) else True


assert containsDuplicates2([1, 2, 3, 1]) == True
assert containsDuplicates2([1, 2, 3, 4]) == False
