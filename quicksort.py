import random
import functools
import time


def timewrap(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        s = time.time()
        f = func(*args, **kwargs)
        print(time.time() - s)
        return f
    return wrapper


def quicksort1(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort1(s_nums) + e_nums + quicksort1(m_nums)


def quick_sort2(nums, fst, lst):
    if fst >= lst: return

    i, j = fst, lst
    pivot = nums[(lst + fst) // 2]
    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quick_sort2(nums, fst, j)
    quick_sort2(nums, i, lst)
    return nums


def quick_sort3(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quick_sort3(l_nums) + e_nums + quick_sort3(b_nums)


def main():
    nums = [5, 7, 8, 3, 4, 5, 6, 8, 9,
            3, 3, 4, 5, 7, 4, 5, 6, 4, 2, 6, 8, 9, 0, 3, 4]
    q1 = quicksort1(nums)
    q2 = quick_sort2(nums, 0, len(nums)-1)
    q3 = quick_sort3(nums)
    return f"{q1}\n{q2}\n{q3}"
