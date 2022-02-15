"""https://stepik.org/lesson/13246/step/4?unit=3431"""


def binary_find(b, A):
    l = 0
    r = len(A) - 1
    while l <= r:
        i = l + (r - l) // 2
        if A[i] == b:
            return i + 1
        elif A[i] > b:
            r = i - 1
        else:
            l = i + 1
    return -1


n, *A = map(int, input().split())
k, *b = map(int, input().split())
for i in range(k):
    b[i] = binary_find(b[i], A)
print(' '.join(str(n) for n in b))