import sys

N, M = map(int, sys.stdin.readline().split())
arr = [input() for _ in range(N)]
arr2 = [input() for _ in range(M)]

answer = list(set(arr) & set(arr2))

print(len(answer))
for i in sorted(answer):
    print(i)