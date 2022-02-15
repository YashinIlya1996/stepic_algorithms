"""https://stepik.org/lesson/13259/step/5?unit=3444"""

from pprint import pprint as print


def knapsack_without_repetitions(W: int, w: list, c: list):
    if (not (w or c)) or W == 0:
        return 0
    n = len(w)
    w = [0] + w
    c = [0] + c
    D = [[].copy() for _ in range(n + 1)]
    for w_cur in range(W + 1):
        for i in range(n + 1):
            D[i].append(0)

    for i in range(1, n + 1):
        for w_cur in range(1, W + 1):
            if w[i] <= w_cur:
                D[i][w_cur] = max(D[i - 1][w_cur], D[i - 1][w_cur - w[i]] + c[i])
            else:
                D[i][w_cur] = D[i - 1][w_cur]
    return D[n][W]


def test():
    print(knapsack_without_repetitions(10, [6, 3, 4, 2], [30, 14, 16, 9]))


def main():
    W, n = map(int, input().split())
    w = [int(wi) for wi in input().split()]
    print(knapsack_without_repetitions(W, w, w))


if __name__ == '__main__':
    main()
