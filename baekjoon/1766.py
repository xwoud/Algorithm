import sys

N, M= map(int, sys.stdin.readline().split())
arr = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b] = a

answer = []

def myRole(v):
    k = arr[v]
    if k != 0:
        myRole(k)
    answer.append(v)
    return answer

for i in range(1,N+1,1):
    if i not in answer:
        myRole(i)

print(answer)
