def count_sort(a: list, nmax=10):
    b = [a.count(i) for i in range(0, nmax + 1)]
    for i in range(2, len(b)):
        b[i] += b[i - 1]
    _a = [0 for _ in range(len(a))]
    for el in reversed(a):
        _a[b[el] - 1] = el
        b[el] -= 1
    return _a


