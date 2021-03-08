import sys

def getPrimeNum(n):
    if n == 1 :
        return False
    elif n == 2 :
        return True
    for i in range(2, n):
        if n % i == 0 :
            return False
    return True

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
arr = list(range(M, N+1))
answer = []
for j in arr:
    if getPrimeNum(j):
        answer.append(j)
if len(answer) > 0 :
    print(sum(answer))
    print(answer[0])
else :
    print(-1)