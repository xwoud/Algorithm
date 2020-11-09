from __future__ import print_function
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]
count = [1]*(n+1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    adj[y].append(x)

for i in range(1,m+1,1):
    visited = [False] * (n + 1)
    need_visit = deque()
    need_visit.append(i)
    while need_visit:
        node = need_visit.popleft()
        if not(visited[node]):
            visited[node] = True
            for j in adj[node]:
                if not visited[j]:
                    need_visit.append(j)
                    count[i] += 1
m = max(count)

for i in range(1,m+1,1):
    if count[i] == m :
        print(i, end = " ")
