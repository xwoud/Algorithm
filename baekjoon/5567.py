from __future__ import print_function
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

friends = [[0]*n for _ in range(n)]
res = set()
f = list()
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    if a == 1:
        f.append(b-1)
        res.add(b-1)
    friends[a-1][b-1] = 1
    friends[b-1][a-1] = 1
while f:
    num = f.pop()
    for i in range(1,n):
        if friends[num][i] == 1:
            res.add(i)

print(len(res))