"""https://stepik.org/lesson/13248/step/5"""


from collections import deque

def generate_input():
    import random
    with open('6.4.5_input.txt', 'w') as file:
        s = ''
        for i in range(random.randint(0, 1e5)):
            file.write(str(random.randint(1, 1e9)) + ' ')

def merge(a: list, b: list):
    c = []
    count = 0
    while a and b:
        if a[0] <= b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
            count += len(a)
    if a:
        c.extend(a)
    else:
        c.extend(b)
    return c, count


input()
# generate_input()
# sys.stdin = open('6.4._5_input.txt')
a = []
a = deque([[x] for x in map(int, input().split())])
answer = 0
while len(a) > 1:
    temp = []
    while a:
        if len(a) > 1:
            c, count = merge(a.popleft(), a.popleft())
        else:
            c, count = merge(a.popleft(), [])
        answer += count
        temp.append(c)
    a = deque(temp)
print(answer)
