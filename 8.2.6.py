"""https://stepik.org/lesson/13257/step/6?unit=3442"""

from sys import stdin


def gis_nlogn(A):
    n = len(A)
    inf = max([abs(el) for el in A]) + 1
    L = [inf] + [-inf] * (n + 1)
    memory = {}
    for i in range(n):
        left = 0
        right = n + 1
        while left + 1 < right:
            middle = (left + right) // 2
            if L[middle] >= A[i]:
                left = middle
            else:
                right = middle
        L[right] = A[i]
        memory.setdefault(right, {})
        if A[i] not in memory[right].keys():
            memory[right].setdefault(A[i], 0)
            memory[right][A[i]] = i
    k = n + 1
    while L[k] == -inf:
        k -= 1
    _answer = [list(memory[k].items())[0]]
    temp = 0
    for i in range(k-1, 0, -1):
        for el in memory[i].items():
            if el[0] >= _answer[temp][0] and el[1] < _answer[temp][1]:
                temp += 1
                _answer.append(el)
                break
    print(k)
    for el in reversed(_answer):
        print(el[1] + 1, end=' ')


n = int(stdin.readline())
A = [i for i in map(int, stdin.readline().split())]
gis_nlogn(A)
