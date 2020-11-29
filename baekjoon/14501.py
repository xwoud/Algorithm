from __future__ import print_function
import sys

n = int(sys.stdin.readline())
t = []
p = []
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)
    arr.append(b)
arr.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        arr[i] = arr[i + 1]
    else:
        arr[i] = max(arr[i + 1], p[i] + arr[i + t[i]])
print(arr[0])