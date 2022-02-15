import sys
from time_func import time_func
from generate_input import generate_input
from merge_sort import merge_sort
from quick_sort import quick_sort
from quick3_sort import quick3_sort
from random import randint, choice


generate_input(length=2 * 10 ** 4)
sys.stdin = open('input.txt', 'rt')
tested_list1 = list(map(int, input().split()))
tested_list2 = tested_list1.copy()
sys.stdin.close()
# time_func(merge_sort)(tested_list)
time_func(quick_sort)(tested_list1)
assert tested_list1 == sorted(tested_list1)
time_func(quick3_sort)(tested_list2)
assert tested_list2 == sorted(tested_list2)

print('проверка quick_sort на few_unique')
data = []
for i in range(10):
    data.append(randint(0, 10 ** 9))
with open('input.txt', 'w') as file:
    for i in range(2 * 10 ** 4):
        file.write(str(choice(data)) + ' ')

sys.stdin = open('input.txt', 'rt')
tested_list = list(map(int, input().split()))
tested_list2 = tested_list.copy()
time_func(quick_sort)(tested_list)
assert tested_list == sorted(tested_list)
time_func(quick3_sort)(tested_list2)
assert tested_list2 == sorted(tested_list2)
sys.stdin.close()