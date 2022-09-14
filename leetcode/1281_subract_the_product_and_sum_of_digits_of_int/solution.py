import math


def subtractProductAndASum(n: int) -> int:
    split_n = [int(value) for value in list(str(n))]
    sum_of_n = sum(split_n)
    product_of_n = math.prod(split_n)  # Prod method was added into Math in 3.8

    return product_of_n - sum_of_n


assert subtractProductAndASum(234) == 15


def subtractProductAndASum2(n: int) -> int:
    sum_of_n = 0
    product_of_n = 1

    for value in [int(value) for value in list(str(n))]:
        sum_of_n += value
        product_of_n *= value

    return product_of_n - sum_of_n


assert subtractProductAndASum2(234) == 15
