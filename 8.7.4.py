"""https://stepik.org/lesson/13262/step/4?unit=3447"""


def step_count_iter(a):
    n = len(a)
    d = [0 for _ in range(n + 1)]
    d[1] = a[0]
    for i in range(2, n + 1):
        d[i] = max(d[i - 1], d[i - 2]) + a[i - 1]
    return d[n]


input()
a = [int(el) for el in input().split()]
print(step_count_iter(a))
