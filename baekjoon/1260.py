from __future__ import print_function
import sys
from collections import deque
def dfs(v):
    visited.append(v)
    for i in adj[v]:
        if i not in visited:
            dfs(i)

def bfs(v):
    need_visit = deque()
    need_visit.append(v)
    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            for j in adj[node]:
                if j not in visited:
                    need_visit.append(j)


n,m,v = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = []
dfs(v)
for i in visited:
    print(i, end = " ")

print()

visited = []
bfs(v)
for j in visited:
    print(j, end= " ")


