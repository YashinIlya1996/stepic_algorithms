from random import randint


def partition3(a: list, l, r, ):
    x = a[l]
    jr = l
    jl = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            jl += 1
            jr += 1
            a[jl], a[i] = a[i], a[jl]
            if jr > jl:
                a[jr], a[i] = a[i], a[jr]

        elif a[i] == x and jr < r:
            jr += 1
            a[jr], a[i] = a[i], a[jr]
    a[l], a[jl] = a[jl], a[l]
    return jl, jr


def quick3_sort(a: list, l=None, r=None):
    if l is None and r is None:
        l = 0
        r = len(a) - 1
    if l >= r:
        return
    rand_pos = randint(l, r)
    a[l], a[rand_pos] = a[rand_pos], a[l]
    m1, m2 = partition3(a, l, r)
    quick3_sort(a, l, m1 - 1)
    quick3_sort(a, m2 + 1, r)