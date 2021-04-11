import sys
import itertools

T = int(sys.stdin.readline())
item = list(map(int, input().split()))
answer = []

for test in list(itertools.permutations(item)) :

    my = 0
    test = list(test)
    for j in range(0,T-1):
        my += abs(test[j]-test[j+1])

    answer.append(my)

print(max(answer))

