"""https://stepik.org/lesson/13257/step/5?unit=3442"""


import sys
input = sys.stdin.readline
n = int(input())
a = [i for i in map(int, input().split())]
d = [1 for _ in range(len(a))]
for i in range(len(a)):
    for j in range(i):
        if a[i] % a[j] == 0 and d[j] + 1 > d[i]:
            d[i] += 1
k = max(d)
print(k)
