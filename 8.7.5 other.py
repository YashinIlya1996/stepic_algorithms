def found(number):
    que, answer = [1], [number]
    previous = {1: 0}
    while number not in previous:
        x = que.pop(0)
        for elem in {x + 1, 2 * x, 3 * x}:
            if elem not in previous and elem <= number:
                previous[elem] = x
                que.append(elem)

    while answer[-1] != 1:
        answer.append(previous[answer[-1]])
    return answer


ans = found(int(input()))
print(len(ans) - 1)
print(*reversed(ans))