k, l = map(int, input().split())
key_dict = {}
for _ in range(k):
    letter, code = input().split(': ')
    key_dict[letter] = code
s = input()
answer = ""
while s:
    for key, value in key_dict.items():
        if s.startswith(value):
            answer += key
            s = s[len(value):]
            break
print(answer)
