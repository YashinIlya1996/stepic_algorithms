from random import randint


def partition(a: list, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j


def quick_sort(a: list, l=None, r=None):
    if l is None and r is None:
        l = 0
        r = len(a) - 1
    while l < r:
        rand_pos = randint(l, r)
        a[l], a[rand_pos] = a[rand_pos], a[l]
        m = partition(a, l, r)
        if (m - l) >= (r - m):
            quick_sort(a, m + 1, r)
            r = m - 1
        else:
            quick_sort(a, l, m - 1)
            l = m + 1
