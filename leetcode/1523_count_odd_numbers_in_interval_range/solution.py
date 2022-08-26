# Brute force solution that actually fails on leetcode becuase of timeout
def countOdds(low: int, high: int) -> int:
    count = 0

    for i in range(low, high + 1):
        if i % 2:
            count +=1

    return count

def countOdds2(low: int, high: int) -> int:
    # // is int division while / is returns a float
    ans = (high - low) // 2

    if low % 2 or high % 2:
        ans += 1

    return ans

assert(countOdds(3,7) == 3)
assert(countOdds2(3,7) == 3)
