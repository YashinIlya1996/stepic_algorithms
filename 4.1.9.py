"""https://stepik.org/lesson/13238/step/9?unit=3424"""

segments = []
dots = []
n = int(input())
for _ in range(n):
    segments.append(tuple(map(int, input().split())))
segments.sort(key=lambda segment: segment[1])
dots.append(segments[0][1])
del segments[0]
for segment in segments:
    if segment[0] > dots[-1]:
        dots.append(segment[1])
print(len(dots))
print(' '.join(str(dot) for dot in dots))