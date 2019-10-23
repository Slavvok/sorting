def mergesort1(lst):
    if len(lst) <= 1:
        return lst

    left = []
    right = []
    for i in range(len(lst)):
        if i < len(lst)/2:
            left.append(lst[i])
        else:
            right.append(lst[i])
    left = mergesort2(left)
    right = mergesort2(right)

    return merge(left, right)


def mergesort2(lst):
    """More pythonic version"""
    length = len(lst)
    if length <= 1:
        return lst

    middle = int(length/2)
    left = lst[:middle]
    right = lst[-(length-middle):]

    left = mergesort2(left)
    right = mergesort2(right)

    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        l = left[0]
        r = right[0]
        if l <= r:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result

