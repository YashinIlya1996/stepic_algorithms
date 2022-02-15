def merge(a: list, b: list):
    c = []
    while a and b:
        if a[0] <= b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    if a:
        c.extend(a)
    else:
        c.extend(b)
    return c


def merge_sort(a: list):
    if len(a) == 1:
        return a
    else:
        m = len(a) // 2
        return merge(merge_sort(a[:m]), merge_sort(a[m:]))

