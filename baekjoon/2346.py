from sys import stdin
from collections import deque

N = int(stdin.readline())
q = deque(enumerate(map(int, stdin.readline().split())))
answer = []

while True:
    idx, paper = q.popleft()
    answer.append(idx + 1)

    if not q:
        break

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)
    print(q)

print(' '.join(map(str, answer)))