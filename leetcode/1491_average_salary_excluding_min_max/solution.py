from typing import List


def average(salary: List[int]) -> float:
    return sum(
        [value for value in salary if value != max(salary) and value != min(salary)]
    ) / (len(salary) - 2)


print(average([4000, 3000, 1000, 2000]))
