from mergesort import mergesort2
from quicksort import quicksort1

nums = [5, 7, 8, 3, 4, 5, 6, 8, 9,
        3, 3, 4, 5, 7, 4, 5, 6, 4,
        2, 6, 8, 9, 0, 3, 4]


class Sort:
    def __init__(self, lst=None, default=False):
        self.lst = lst or nums
        self.default = default

    def mergesort(self):
        return mergesort2(self.lst)

    def quicksort(self):
        return quicksort1(self.lst)

    def __str__(self):
        return str(self.lst)


s = Sort(nums)

print(s.quicksort())
print(s.mergesort())
print(s)
repr(s)
