import sys

N = int(sys.stdin.readline())
haveNumber = list(map(int, input().split()))
M = int(sys.stdin.readline())
checkNumber = list(map(int, input().split()))

answer = {checkNumber[i]: 0 for i in range(len(checkNumber))}

for i in range(N):
    if haveNumber[i] in answer.keys():
        answer[haveNumber[i]] += 1


for j in answer.values():
    print(j, end=' ')