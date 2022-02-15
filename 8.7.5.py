"""https://stepik.org/lesson/13262/step/5"""

from functools import lru_cache
import sys

sys.setrecursionlimit(10000)


@lru_cache(maxsize=None)
def calc(x: int):
    if x == 1:
        return 0
    elif x in (2, 3):
        return 1
    else:
        if x % 3 == 0 and x % 2 == 0:
            return min(calc(x // 3), calc(x // 2), calc(x - 1)) + 1
        elif x % 3 == 0:
            return min(calc(x // 3), calc(x - 1)) + 1
        elif x % 2 == 0:
            return min(calc(x // 2), calc(x - 1)) + 1
        else:
            return calc(x - 1) + 1


def calc_iter(x):
    d = {1: 0, 2: 1, 3: 1}
    for i in range(4, x + 1):
        if i % 3 == 0 and i % 2 == 0:
            d[i] = min(d[i // 3], d[i // 2], d[i - 1]) + 1
        elif i % 3 == 0:
            d[i] = min(d[i // 3], d[i - 1]) + 1
        elif i % 2 == 0:
            d[i] = min(d[i // 2], d[i - 1]) + 1
        else:
            d[i] = d[i - 1] + 1
    return (d[x], d)


def return_answer(x: int, d: dict):
    answer = [x]
    while x > 1:
        if x % 3 == 0 and x % 2 == 0:
            if d[x // 3] == d[x] - 1:
                x = x // 3
            elif d[x // 2] == d[x] - 1:
                x = x // 2
            else:
                x = x - 1
        elif x % 3 == 0:
            if d[x // 3] == d[x] - 1:
                x = x // 3
            else:
                x = x - 1
        elif x % 2 == 0:
            if d[x // 2] == d[x] - 1:
                x = x // 2
            else:
                x = x - 1
        else:
            x -= 1
        answer.append(x)
    return list(reversed(answer))


n = int(input())
count, d = calc_iter(n)
print(count)
print(*return_answer(n, d))
