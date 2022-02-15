"""https://stepik.org/lesson/13229/step/5?unit=3415"""

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    else:
        return gcd(b % a, a)


a, b = map(int, input().split())
print(gcd(a, b))
