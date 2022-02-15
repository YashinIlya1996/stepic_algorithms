from mybheap import MyBinaryHeap
from sys import stdin


input = stdin.readline
heap = MyBinaryHeap(maxheap=True)
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'Insert':
        heap.insert(int(command[1]))
    else:
        print(heap.pop_root())
