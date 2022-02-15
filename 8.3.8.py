"""https://stepik.org/lesson/13258/step/8?unit=3443"""

from pprint import pprint as print


def diff(ai, bj):
    return 1 if ai != bj else 0


def edit_dist(a, b):
    if a == b:
        return 0
    n, m = len(a) + 1, len(b) + 1
    d = [[].copy() for _ in range(m)]
    for i in range(n):
        d[0].append(i)
    for i in range(1, m):
        d[i].append(i)

    # заполнение матрицы расстояний d
    for i in range(1, m):
        for j in range(1, n):
            deleting = d[i - 1][j] + 1
            insert = d[i][j - 1] + 1
            substitution = d[i - 1][j - 1] + diff(a[j - 1], b[i - 1])
            d[i].append(min(deleting, insert, substitution))
    return d[m - 1][n - 1]


def main():
    a = input()
    b = input()
    print(edit_dist(a, b))


def test():
    print(edit_dist('qwert', 'kjhgfdsa'))
    print(edit_dist('ab', 'ab'))


if __name__ == '__main__':
    main()
