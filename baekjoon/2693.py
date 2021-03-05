import sys

N = int(sys.stdin.readline())

for _ in range(N):
    llists = list(map(int, input().split()))
    llists.sort()
    print(llists[-3])