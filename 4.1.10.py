"""https://stepik.org/lesson/13238/step/10?unit=3424"""

n, W = map(int, input().split())
stuffs = []
for _ in range(n):
    stuffs.append((tuple(map(int, input().split()))))
stuffs.sort(key=lambda x: x[0] / x[1], reverse=True)
C = 0.0
for stuff in stuffs:
    if W > stuff[1]:
        W -= stuff[1]
        C += stuff[0]
    else:
        C += stuff[0] / stuff[1] * W
        break
print(f'{C:.10f}')
