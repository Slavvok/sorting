from collections import deque


nums = [5, 7, 8, 3, 4, 5, 6, 8, 9,
        3, 3, 4, 5, 7, 4, 5, 6, 4,
        2, 6, 8, 9, 0, 3, 4]


def getminrun(n):
    r = 0
    n = len(n)
    while( n>=64 ):
        r |= n & 1
        n >>= 1
    return n + r


print(getminrun(nums*100))
