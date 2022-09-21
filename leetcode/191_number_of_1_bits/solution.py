from collections import Counter


def hammingWeight(n: int) -> int:
    str_n = str(bin(n))
    str_list = [value for value in str_n]
    counter = Counter(str_list)
    return counter["1"]


# Solution using bit shifting
def hammingWeight2(n: int) -> int:
    res = 0
    while n:
        res += n % 2
        n = n >> 1  # this is how you shift the bit by 1
    return res


print(hammingWeight(0b00000000000000000000000000001011))
print(hammingWeight2(0b00000000000000000000000000001011))
