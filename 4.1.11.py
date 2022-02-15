"""https://stepik.org/lesson/13238/step/11?unit=3424"""

n = int(input())
sum, arr = 0, []
for i in range(1, n + 1):
    if sum + i <= n:
        sum += i
        arr.append(i)
    else:
        arr[-1] += n - sum
        break
print(len(arr))
# print(' '.join(str(num) for num in arr))
print(*arr)