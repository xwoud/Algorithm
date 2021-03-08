import sys

n,m = map(int, sys.stdin.readline().split())

arr = []
for i in range(1,46,1):
    for _ in range(i):
        arr.append(i)

answer = arr[n-1:m]
print(sum(answer))