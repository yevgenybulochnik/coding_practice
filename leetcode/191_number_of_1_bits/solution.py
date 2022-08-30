from collections import Counter


def hammingWeight(n: int) -> int:
    str_n = str(bin(n))
    str_list = [value for value in str_n]
    counter = Counter(str_list)
    return counter["1"]


print(hammingWeight(0b00000000000000000000000000001011))
