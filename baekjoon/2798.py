import sys

N,M = map(int, sys.stdin.readline().split())
r_answer = list(map(int, input().split()))
sum = 0
for i in range(0,len(r_answer)-2):
    for j in range(i+1, len(r_answer)-1):
        for t in range(j+1, len(r_answer)):
            test = r_answer[i] + r_answer[j] + r_answer[t]
            if test <= M :
                sum = max(test, sum)
print(sum)
